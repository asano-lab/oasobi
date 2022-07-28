#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <unistd.h>

// サンプル数の設定
#define NUM_SAMPLE 100

// 1回の試行におけるループ数
#define NUM_LOOP 10000

// 忘れないように定義しておく
#define builtin_popcount(x) __builtin_popcount(x)

#define timeval_to_double(tv) \
    (((double)(tv).tv_sec + (double)(tv).tv_usec * 1e-6))

// 指定したビットを取得
#define getBit(x, n) (((x) >> (n)) & 1)

// double型の乱数を生成 [0.0, 1.0]
#define randDouble() ((double)rand_r(&seed) / RAND_MAX)

// 4ビットの乱数を生成
#define rand4Bit() (rand_r(&seed) & 0b1111)

// 各ビットのエラー率が一定の通信路
// 引数はチャンネルの入力, 入力長, エラー率
// エラー率は, 予め RAND_MAX で乗算された int 型とする
#define binary_simmetric_channel(x, nc, e_prob_int) ((x) ^ makeErrorBits(nc, e_prob_int))

// (7, 4)ハミング符号の符号化関数
// 入力は4ビット, 出力は7ビットに固定
// ほとんどパリティ作成なので, マクロに変更
// unsigned int型の入力が望ましい
#define encHamCode7_4(msg) (((msg) << 3) | makeParityHamCode7_4(msg))

// ファイルの格納先
#define path_format "./dat/e_prob%02d.txt"

// テスト用のパス
#define test_path_format "./test/e_prob%02d.txt"

u_int seed;

// 32ビットのバイナリ表示
void printBin32(u_int x) {
    for (int i = 31; i >= 0; i--) {
        printf("%d", getBit(x, i));
    }
    putchar(10);
}

// ビット数を柔軟に変えられるバイナリ表示関数 (最大32ビット)
void printBinN(u_int x, int n) {
    for (int i = n - 1; i >= 0; i--) {
        printf("%d", getBit(x, i));
    }
    putchar(10);
}

// エラービット列の作成
// ビット毎独立で, 同じ確率でエラーを発生させる
// エラー率は, 予め RAND_MAX で乗算された int 型とする
u_int makeErrorBits(int n, int e_prob_int) {
    u_int err = 0;
    for (int i = 0; i < n; i++) {
        err <<= 1;
        // 比較演算で得られるブール値をそのまま加える
        // 乱数がエラー率以下なら1, それ以外は0
        // int 型にする際, 小数点以下切り捨てなので等号含む
        err |= (rand_r(&seed) <= e_prob_int);
    }
    return err;
}

// (3, 1)繰り返し符号の符号化関数
//  第2引数はメッセージのビット長を与える
u_int encRepCode3(u_int msg, int nm) {
    u_int code = 0;
    int i, j, b;
    for (i = 0; i < nm; i++) {
        b = getBit(msg, i);
        for (j = 0; j < 3; j++) {
            code |= b << (i * 3 + j);
        }
    }
    return code;
}

// (3, 1)繰り返し符号の復号関数
// 第2引数はメッセージのビット長を与える
u_int decRepCode3(u_int rsv, int nm) {
    u_int msg = 0;
    int i, j, s;
    for (i = 0; i < nm; i++) {
        s = 0;
        for (j = 0; j < 3; j++) {
            s += getBit(rsv, i * 3 + j);
        }
        if (s >= 2) {
            msg |= 1 << i;
        }
    }
    return msg;
}

// パリティビットの作成
// 入力4ビット, パリティ3ビット
u_int makeParityHamCode7_4(u_int msg) {
    u_int parity;
    u_char b1, b2, b3, b4;
    b1 = getBit(msg, 3);
    b2 = getBit(msg, 2);
    b3 = getBit(msg, 1);
    b4 = msg & 1;
    parity = (b1 ^ b3 ^ b4) << 2;
    parity |= (b1 ^ b2 ^ b4) << 1;
    parity |= b1 ^ b2 ^ b3;
    return parity;
}

// (7, 4)ハミング符号の復号関数
// 入力は7ビット, 出力は4ビットに固定
u_int decHamCode7_4(u_int rsv) {
    u_int err;
    // パリティを再計算し, 受信パリティと比較
    // シンドロームからエラー位置の特定
    switch (makeParityHamCode7_4(rsv >> 3) ^ (rsv & 0b111)) {
        case 0b000: err = 0b0000000; break;
        case 0b111: err = 0b1000000; break;
        case 0b011: err = 0b0100000; break;
        case 0b101: err = 0b0010000; break;
        case 0b110: err = 0b0001000; break;
        case 0b100: err = 0b0000100; break;
        case 0b010: err = 0b0000010; break;
        case 0b001: err = 0b0000001; break;
        default   : err = 0b1111111; break; // でたらめ
    }
    return (rsv ^ err) >> 3;
}

// エラー率の比較
// エラー率は, 予め RAND_MAX で乗算された int 型とする
int compareErrorProb(int loop, int e_prob_int, FILE *fpw) {
    int i;
    u_int tmsg, tcode, rcode, rmsg;
    int ne_err = 0, rep_err = 0, ham_err = 0;
    for (i = 0; i < loop; i++) {
        // メッセージは乱数で作って共有
        tmsg = rand4Bit();

        // 符号化なし
        rmsg = binary_simmetric_channel(tmsg, 4, e_prob_int);
        // エラー数のカウント
        if (tmsg != rmsg) {
            ne_err++;
        }
        
        // (3, 1)繰り返し符号
        tcode = encRepCode3(tmsg, 4);
        rcode = binary_simmetric_channel(tcode, 12, e_prob_int);
        rmsg = decRepCode3(rcode, 4);
        if (tmsg != rmsg) {
            rep_err++;
        }
        
        // (4, 7)ハミング符号
        tcode = encHamCode7_4(tmsg);
        rcode = binary_simmetric_channel(tcode, 7, e_prob_int);
        rmsg = decHamCode7_4(rcode);
        if (tmsg != rmsg) {
            ham_err++;
        }
    }
    // printf("%d %d %d\n", ne_err, rep_err, ham_err);
    // 改行コードを windows に合わせる
    fprintf(fpw, "%d %d %d\r\n", ne_err, rep_err, ham_err);

    return 0;
}

// ビットエラー率の比較
// エラー率は, 予め RAND_MAX で乗算された int 型とする
int compareBER(int loop, int r_max_int, FILE *fpw) {
    int i;
    u_int tmsg, tcode, rcode, rmsg;
    // 誤りビット数の総計
    int ne_bes = 0, rep_bes = 0, ham_bes = 0;
    for (i = 0; i < loop; i++) {
        // メッセージは乱数で作って共有
        tmsg = rand4Bit();

        // 符号化なし
        rmsg = binary_simmetric_channel(tmsg, 4, r_max_int);
        // エラービット数のカウント
        ne_bes += builtin_popcount(tmsg ^ rmsg);
        
        // (3, 1)繰り返し符号
        tcode = encRepCode3(tmsg, 4);
        rcode = binary_simmetric_channel(tcode, 12, r_max_int);
        rmsg = decRepCode3(rcode, 4);
        rep_bes += builtin_popcount(tmsg ^ rmsg);
        
        // (4, 7)ハミング符号
        tcode = encHamCode7_4(tmsg);
        rcode = binary_simmetric_channel(tcode, 7, r_max_int);
        rmsg = decHamCode7_4(rcode);
        ham_bes += builtin_popcount(tmsg ^ rmsg);
    }
    // printf("%d %d %d\n", ne_err, rep_err, ham_err);
    // fprintf(stdout, "%d %d %d\r\n", ne_bes, rep_bes, ham_bes);
    // 改行コードを windows に合わせる
    fprintf(fpw, "%d %d %d\r\n", ne_bes, rep_bes, ham_bes);

    return 0;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        puts("引数不足");
        return -1;
    }
    struct timeval tv0, tv1;
    u_char tmsg, rmsg, e_vec;
    int ret, r_max_int, loop;
    double e_prob, e_prob_true;
    e_prob = 1e-3;
    ret = gettimeofday(&tv0, NULL);
    seed = time(NULL) & 0xffffffff;

    loop = 1e8;
    r_max_int = RAND_MAX * e_prob;
    // 量子化誤差を見る
    e_prob_true = (double)r_max_int / (double)RAND_MAX;
    printf("%.20e, %.20e, %d\n", e_prob, e_prob_true, r_max_int);
    compareBER(loop, r_max_int, stdout);
    ret = gettimeofday(&tv1, NULL);
    printf("%f\n", timeval_to_double(tv1) - timeval_to_double(tv0));
    return ret;
}
