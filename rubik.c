#include <stdio.h>

#define SOLVED_C (u_long)0x0110c8531c
#define SOLVED_E (u_long)0x008864298e84a96

#define R_STATE_C (u_long)0x0274c81abc
#define R_STATE_E (u_long)0x02a464118e80a96

#define getCp(c_info, n) ((c_info) >> (((37 - 5 * (n))) & 0x111))
#define getCo(c_info, n) ((c_info) >> (((35 - 5 * (n))) & 0x11))

#define getEp(e_info, n) ((e_info) >> ((56 - 5 * (n)) & 0x1111))
#define getEo(e_info, n) ((e_info) >> ((55 - 5 * (n)) & 0x1))

typedef unsigned long long u_long;

// cで扱う状態
typedef struct {
    u_long c_info;
    u_long e_info;
} cState;

int nibai(int x) {
    return 2 * x;
}

// 動作の適用
cState applyMove(const cState s1, const cState s2) {
    int i, j, nco, neo;
    cState ns;
    ns.c_info = 0;
    ns.e_info = 0;
    for (i = 0; i < 8; i++) {
        j = getCp(s2.c_info, i);
        ns.c_info = (ns.c_info << 3) | getCp(s1.c_info, j);
        nco = (getCo(s1.c_info, j) + getCo(s2.c_info, i)) % 3;
        ns.c_info = (ns.c_info << 2) | nco;
    }
    for (i = 0; i < 12; i++) {
        j = getEp(s2.e_info, i);
        ns.e_info = (ns.e_info << 4) | getEp(s1.e_info, j);
        neo = (getEo(s1.e_info, j) ^ getEo(s2.c_info, i));
        ns.e_info = (ns.e_info << 1) | neo;
    }
    return ns;
}

int main(void) {
    puts("Hello World!!");
    cState s1, s2;
    s1.c_info = R_STATE_C;
    s1.e_info = R_STATE_E;
    printf("0x%I64x\n", s1.c_info);
    printf("0x%I64x\n", s1.e_info);
    s2 = applyMove(s1, s1);
    printf("0x%I64x\n", s2.c_info);
    printf("0x%I64x\n", s2.e_info);
}