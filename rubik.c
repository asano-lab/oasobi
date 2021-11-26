#include <stdio.h>

typedef unsigned long long u_long;

typedef struct {
    u_long c_info;
    u_long e_info;
} cStatus;

int nibai(int x) {
    return 2 * x;
}

int main(void) {
    puts("Hello World!!");
    cStatus s;
    printf("%I64d\n", sizeof s);
}
