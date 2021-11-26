#include <stdio.h>

#define SOLVED_C 0x0110c8531c
#define SOLVED_E 0x008864298e84a96

typedef unsigned long long u_long;

typedef struct {
    u_long c_info;
    u_long e_info;
} cState;

int nibai(int x) {
    return 2 * x;
}

int main(void) {
    puts("Hello World!!");
    cState s;
    s.c_info = SOLVED_C;
    s.e_info = SOLVED_E;
    printf("0x%I64x\n", s.c_info);
    printf("0x%I64x\n", s.e_info);
}
