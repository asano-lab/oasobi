#include <stdio.h>
#include <stdlib.h>

#define SOLVED_C (u_long)0x0110c8531c
#define SOLVED_E (u_long)0x008864298e84a96

#define SCRAMBLED_STATE_C (u_long)0x83124d5bc2
#define SCRAMBLED_STATE_E (u_long)0x2cd140b8c2ba990

#define getCp(c_info, n) (((c_info) >> (37 - 5 * (n))) & 0b111)
#define getCo(c_info, n) (((c_info) >> ((35 - 5 * (n)))) & 0b11)

#define getEp(e_info, n) (((e_info) >> (56 - 5 * (n))) & 0b1111)
#define getEo(e_info, n) (((e_info) >> (55 - 5 * (n))) & 0b1)

// 5の倍数であること前提
#define getCp5(c_info, n) (((c_info) >> (37 - (n))) & 0b111)
#define getCo5(c_info, n) (((c_info) >> ((35 - (n)))) & 0b11)

#define getEp5(e_info, n) (((e_info) >> (56 - (n))) & 0b1111)
#define getEo5(e_info, n) (((e_info) >> (55 - (n))) & 0b1)

// 適当な位置に値を配置
#define putCp5(c_info, n, cp) ((c_info) | ((u_long)(cp) << (37 - (n))))
#define putCo5(c_info, n, co) ((c_info) | ((u_long)(co) << (35 - (n))))

#define putEp5(e_info, n, ep) ((e_info) | ((u_long)(ep) << (56 - (n))))
#define putEo5(e_info, n, eo) ((e_info) | ((u_long)(eo) << (55 - (n))))

// 基本操作18種 (それぞれ2つの整数)
// 初期は U, D, L, R, F, Bのみ
// 残りの順番は
// U2, U', D2, D', L2, L',
// R2, R', F2, F', B2, B'
u_long MOVES[36] = {
    0x600888531c, 0x008867214c84a96,
    0x0110ca6390, 0x008864298e952d0,
    0x91101ed30e, 0xb088e4298084a86,
    0x0274c81abc, 0x02a464118e80a96,
    0x011be85159, 0x009b5428ee848b6,
    0x2d90c1471c, 0x4c4861a98e0ca96
};

// 色変換のための状態
// UL, UR, UB, DF, DL, DR, DB,
// LU, LD, LF, LB, RU, RD, RF, RB,
// FU, FD, FL, FR, BU, BD, BL, BR
// の順
// それぞれ2つの数値からなる
u_long CHANGE_COLOR[46] = {
    0x60088e4298, 0x384657214cb4254,
    0x22180a6390, 0x194e1531c8952d0,
    0x43004c7214, 0x218026390aa5a12,
    0xa439820188, 0x100c485a924398a,
    0xc521c4100c, 0x28c27942d4521cc,
    0x8731403104, 0x09ca3b525073148,
    0xe629062080, 0x31040a4a166290e,
    0x4ebae35641, 0x5ceef254cd14409,
    0x0caa677749, 0x7de6b044493548d,
    0x2db2a147cd, 0x4c6ad1ccab0dcef,
    0x6fa22566c5, 0x6d6293dc2f2cc6b,
    0xeb93a904d5, 0xbbd733349502451,
    0xa9832d25dd, 0x9adf712411234d5,
    0x889beb1559, 0x8a5b50bcf71acb3,
    0xca8b6f3451, 0xab5312ac733bc37,
    0xd75c9ac826, 0x959caa99a488122,
    0x954c1ee92e, 0xb494e88920a91a6,
    0xf444dcd8aa, 0xa410cb85e798d65,
    0xb65458f9a2, 0x8518899563b9de1,
    0x7275d09ab2, 0x72a56692a648a20,
    0x306554bbba, 0x53ad24822269aa4,
    0x516d968a3e, 0x6221458e65786e7,
    0x137d12ab36, 0x4329079ee159663
};

// パーツの入れ替え法則
// 配列だけ定義し, 中身は関数で作成予定
u_long REPLACE_PARTS[46] = {0};

// 上下鏡写しの変換法則
int UDM_CP[8] = {4, 5, 6, 7, 0, 1, 2, 3};
int UDM_EP[12] = {0, 1, 2, 3, 8, 9, 10, 11, 4, 5, 6, 7};

void printState(const u_long *state) {
    printf("0x%010lx, 0x%015lx\n", state[0], state[1]);
}

// 動作の適用
int applyMove(const u_long *s1, const u_long *s2, u_long *ns) {
    int i, j;
    ns[0] = 0;
    ns[1] = 0;
    for (i = 0; i < 40; i += 5) {
        j = getCp5(s2[0], i) * 5;
        ns[0] = ns[0] << 3 | getCp5(s1[0], j);
        ns[0] = ns[0] << 2 | (getCo5(s1[0], j) + getCo5(s2[0], i)) % 3;
    }
    for (i = 0; i < 60; i += 5) {
        j = getEp5(s2[1], i) * 5;
        ns[1] = ns[1] << 4 | getEp5(s1[1], j);
        ns[1] = ns[1] << 1 | (getEo5(s1[1], j) ^ getEo5(s2[1], i));
    }
    return 0;
}

// 全18種の動作の適用
// dstsには長さ36のu_long配列を与える
int applyAllMoves(const u_long *src, u_long *dsts) {
    for (int i = 0; i <= 36; i += 2) {
        applyMove(src, MOVES + i, dsts + i);
    }
    return 0;
}

// 色変換
int changeColor(const u_long *src, u_long *dst, int ch_rule) {
    u_long tmp_st[2];
    applyMove(src, CHANGE_COLOR + ch_rule * 2, tmp_st);
    applyMove(REPLACE_PARTS + ch_rule * 2, tmp_st, dst);
    return 0;
}

// 上下ミラー
int udMirror(const u_long *src, u_long *dst) {
    int i, j;
    u_long tmp_st[2] = {0};
    for (i = 0; i < 8; i++) {
        j = UDM_CP[i] * 5;
        tmp_st[0] = tmp_st[0] << 3 | getCp5(src[0], j);
        tmp_st[0] = tmp_st[0] << 2 | (3 - getCo5(src[0], j)) % 3;
    }
    for (i = 0; i < 12; i++) {
        j = UDM_EP[i] * 5;
        tmp_st[1] = tmp_st[1] << 4 | getEp5(src[1], j);
        tmp_st[1] = tmp_st[1] << 1 | getEo5(src[1], j);
    }
    dst[0] = 0;
    dst[1] = 0;
    for (i = 0; i < 40; i += 5) {
        j = getCp5(tmp_st[0], i);
        dst[0] = dst[0] << 3 | UDM_CP[j];
        dst[0] = dst[0] << 2 | getCo5(tmp_st[0], i);
    }
    for (i = 0; i < 60; i += 5) {
        j = getEp5(tmp_st[1], i);
        dst[1] = dst[1] << 4 | UDM_EP[j];
        dst[1] = dst[1] << 1 | getEo5(tmp_st[1], i);
    }
    return 0;
}

// 位置変換からパーツ変換の計算
int createReplaceParts(const u_long *ch_pos, u_long *ch_parts) {
    int i, j;
    for (i = 0; i < 8; i++) {
        j = getCp(ch_pos[0], i) * 5;
        ch_parts[0] = putCp5(ch_parts[0], j, i);
        ch_parts[0] = putCo5(ch_parts[0], j, (3 - getCo(ch_pos[0], i)) % 3);
    }
    for (i = 0; i < 12; i++) {
        j = getEp(ch_pos[1], i) * 5;
        ch_parts[1] = putEp5(ch_parts[1], j, i);
        ch_parts[1] = putEo5(ch_parts[1], j, getEo(ch_pos[1], i));
    }
    return 0;
}

// 状態の比較, 最小値の更新
// 第一引数が第二引数以下の場合はそのまま
// 第一引数の方が大きかったら値を更新
int updateMinState(u_long *min_st, const u_long *target_st) {
    if (min_st[0] < target_st[0]) return 0;
    if (min_st[0] == target_st[0] && min_st[1] <= target_st[1]) return 0;
    min_st[0] = target_st[0];
    min_st[1] = target_st[1];
    return 1;
}

// 状態の正規化
// 色の変換, 鏡写し計48種を計算し, 最小の値を選択
// 与えたポインタの中身を直接書き換える
int normalState(u_long *st) {
    u_long origin[2], mirror[2], eq_st[2];
    // 変更前の状態を保存
    origin[0] = st[0];
    origin[1] = st[1];
    udMirror(origin, mirror);
    // ミラーと比較して小さい方をdstに格納
    updateMinState(st, mirror);
    // そのままとミラー両方で23種の色変換を行う
    for (int i = 0; i < 23; i++) {
        changeColor(origin, eq_st, i);
        updateMinState(st, eq_st);
        changeColor(mirror, eq_st, i);
        updateMinState(st, eq_st);
    }
    return 0;
}

// 全動作適用後それらを正規化してdstsに格納
int applyAllMovesNormal(const u_long *src, u_long *dsts) {
    // まずは普通に動作適用
    applyAllMoves(src, dsts);
    // 18状態すべて正規化
    for (int i = 0; i < 18; i++) {
        normalState(dsts + i * 2);
    }
    return 0;
}

// 初期化関数
int init(void) {
    int i, j;
    // 残りの基本操作を追加
    for (i = 0; i < 12; i += 2) {
        j = 12 + i * 2;
        applyMove(MOVES + i, MOVES + i, MOVES + j);
        applyMove(MOVES + i, MOVES + j, MOVES + j + 2);
    }
    for (i = 0; i < 46; i += 2) {
        createReplaceParts(CHANGE_COLOR + i, REPLACE_PARTS + i);
    }
    return 0;
}

int main(void) {
    u_long ss[2], sscc[2], nss[2];
    u_long aam[36] = {};
    ss[0] = SCRAMBLED_STATE_C;
    ss[1] = SCRAMBLED_STATE_E;
    ss[0] = SOLVED_C;
    ss[1] = SOLVED_E;

    init();
    // printState(ss);
    // applyAllMovesNormal(ss, aam);
    applyAllMoves(ss, aam);
    for (int i = 0; i < 36; i += 2) {
        printState(aam + i);
    }
    // normalState(ss);
    printState(ss);
    return 0;
}
