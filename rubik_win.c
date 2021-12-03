#include <stdio.h>

#define SOLVED_C (u_long)0x0110c8531c
#define SOLVED_E (u_long)0x008864298e84a96

#define R_STATE_C (u_long)0x0274c81abc
#define R_STATE_E (u_long)0x02a464118e80a96

#define getCp(c_info, n) (((c_info) >> (37 - 5 * (n))) & 0b111)
#define getCo(c_info, n) (((c_info) >> ((35 - 5 * (n)))) & 0b11)

#define getEp(e_info, n) (((e_info) >> (56 - 5 * (n))) & 0b1111)
#define getEo(e_info, n) (((e_info) >> (55 - 5 * (n))) & 0b1)

// 5の倍数であること前提
#define getCp5(c_info, n) (((c_info) >> (37 - (n))) & 0b111)
#define getCo5(c_info, n) (((c_info) >> ((35 - (n)))) & 0b11)

#define getEp5(e_info, n) (((e_info) >> (56 - (n))) & 0b1111)
#define getEo5(e_info, n) (((e_info) >> (55 - (n))) & 0b1)

typedef unsigned long long u_long;

// 色変換のための状態
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

// 動作の適用
int applyMove(const u_long *s1, const u_long *s2, u_long *ns) {
    int i, j;
    ns[0] = 0;
    ns[1] = 0;
    for (i = 0; i < 40; i += 5) {
        j = getCp5(s2[0], i) * 5;
        ns[0] <<= 3;
        ns[0] |= getCp5(s1[0], j);
        ns[0] <<= 2;
        ns[0] |= (getCo5(s1[0], j) + getCo5(s2[0], i)) % 3;
    }
    for (i = 0; i < 60; i += 5) {
        j = getEp5(s2[1], i) * 5;
        ns[1] <<= 4;
        ns[1] |= getEp5(s1[1], j);
        ns[1] <<= 1;
        ns[1] |= getEo5(s1[1], j) ^ getEo5(s2[1], i);
    }
    return 0;
}

int main(void) {
    u_long rs[2], r2s[2];
    rs[0] = R_STATE_C;
    rs[1] = R_STATE_E;
    applyMove(rs, rs, r2s);
    printf("0x%I64x\n", r2s[0]);
    printf("0x%I64x\n", r2s[1]);
    printf("0x%I64x\n", CHANGE_COLOR[45]);
}
