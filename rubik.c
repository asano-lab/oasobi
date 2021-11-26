#include <stdio.h>

#define SOLVED_C (u_long)0x0110c8531c
#define SOLVED_E (u_long)0x008864298e84a96

#define R_STATE_C (u_long)0x0274c81abc
#define R_STATE_E (u_long)0x02a464118e80a96

#define getCp(c_info, n) (((c_info) >> (37 - 5 * (n))) & 0b111)
#define getCo(c_info, n) (((c_info) >> ((35 - 5 * (n)))) & 0b11)

#define getEp(e_info, n) (((e_info) >> (56 - 5 * (n))) & 0b1111)
#define getEo(e_info, n) (((e_info) >> (55 - 5 * (n))) & 0b1)

typedef unsigned long long u_long;

// 動作の適用
int applyMove(const u_long *s1, const u_long *s2, u_long *ns) {
    int i, j;
    ns[0] = 0;
    ns[1] = 0;
    for (i = 0; i < 8; i++) {
        j = getCp(s2[0], i);
        ns[0] <<= 3;
        ns[0] |= getCp(s1[0], j);
        ns[0] <<= 2;
        ns[0] |= (getCo(s1[0], j) + getCo(s2[0], i)) % 3;
    }
    for (i = 0; i < 12; i++) {
        j = getEp(s2[1], i);
        ns[1] <<= 4;
        ns[1] |= getEp(s1[1], j);
        ns[1] <<= 1;
        ns[1] |= getEo(s1[1], j) ^ getEo(s2[1], i);
    }
    printf("0x%I64x\n", ns[0]);
    printf("0x%I64x\n", ns[1]);
    return 0;
}

int main(void) {
    u_long rs[2], r2s[2];
    rs[0] = R_STATE_C;
    rs[1] = R_STATE_E;
    applyMove(rs, rs, r2s);
    printf("0x%I64x\n", r2s[0]);
    printf("0x%I64x\n", r2s[1]);
}
