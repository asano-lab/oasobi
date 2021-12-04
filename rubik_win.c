#include <stdio.h>

#define SOLVED_C (u_long)0x0110c8531c
#define SOLVED_E (u_long)0x008864298e84a96

#define R_STATE_C (u_long)0x0274c81abc
#define R_STATE_E (u_long)0x02a464118e80a96

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

typedef unsigned long long u_long;

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
    0x8731403104, 0x9ca3b525073148,
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
    printf("0x%010I64x, 0x%015I64x\n", state[0], state[1]);
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

// 色変換
int changeColor(const u_long *src, u_long *dst, int ch_rule) {
    u_long tmpst[2];
    applyMove(src, CHANGE_COLOR + ch_rule * 2, tmpst);
    applyMove(REPLACE_PARTS + ch_rule * 2, tmpst, dst);
    return 0;
}

// 上下ミラー
int udMirror(const u_long *src, u_long *dst) {
    int i, j, cmn;
    u_long tmpst[2] = {0};
    for (i = 0; i < 8; i++) {
        j = UDM_CP[i] * 5;
        tmpst[0] = tmpst[0] << 3 | getCp5(src[0], j);
        tmpst[0] = tmpst[0] << 2 | (3 - getCo5(src[0], j)) % 3;
    }
    for (i = 0; i < 12; i++) {
        j = UDM_EP[i] * 5;
        tmpst[1] = tmpst[1] << 4 | getEp5(src[1], j);
        tmpst[1] = tmpst[1] << 1 | getEo5(src[1], j);
    }
    dst[0] = 0;
    dst[1] = 0;
    for (i = 0; i < 40; i += 5) {
        j = getCp5(tmpst[0], i);
        dst[0] = dst[0] << 3 | UDM_CP[j];
        dst[0] = dst[0] << 2 | getCo5(tmpst[0], i);
    }
    for (i = 0; i < 60; i += 5) {
        j = getEp5(tmpst[1], i);
        dst[1] = dst[1] << 4 | UDM_EP[j];
        dst[1] = dst[1] << 1 | getEo5(tmpst[1], i);
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

// 初期化関数
int init(void) {
    int i;
    for (i = 0; i < 46; i += 2) {
        createReplaceParts(CHANGE_COLOR + i, REPLACE_PARTS + i);
    }
    return 0;
}

int main(void) {
    u_long ss[2], sscc[2];
    // ss[0] = SCRAMBLED_STATE_C;
    // ss[1] = SCRAMBLED_STATE_E;
    ss[0] = SOLVED_C;
    ss[1] = SOLVED_E;
    init();
    printState(ss);
    udMirror(ss, sscc);
    printState(sscc);
    return 0;
}
