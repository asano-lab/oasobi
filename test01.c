#include <stdio.h>
#include <stdlib.h>

int main(void) {
    u_short x, y;
    x = 0xffff;
    y = 24000;
    printf("x=%d, y=%d\n", x, y);
    printf("x/y=%f\n", (double)x / (double)y);
    double r;
    r = 0.0001;
    x *= r;
    y *= r;
    printf("x=%d, y=%d\n", x, y);
    printf("x/y=%f\n", (double)x / (double)y);
    return 0;
}
