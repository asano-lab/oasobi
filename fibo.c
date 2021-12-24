#include <stdio.h>
#include <time.h>

long fibo(int n) {
    if (n <= 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    return fibo(n - 1) + fibo(n - 2);
}

int main(void) {
    time_t t0, t1;
    time(&t0);
    printf("%ld\n", fibo(47));
    time(&t1);
    printf("%ld 秒\n", t1 - t0);
    return 0;
}
