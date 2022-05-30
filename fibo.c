#include <stdio.h>
#include <time.h>

// フィボナッチ数列
long fibo(int n)
{
    if (n <= 0)
    {
        return 0;
    }
    if (n == 1)
    {
        return 1;
    }
    return fibo(n - 1) + fibo(n - 2);
}

int main(void)
{
    int n = 39;
    time_t t0, t1;
    time(&t0);
    printf("fibo(%d) = %ld\n", n, fibo(n));
    time(&t1);
    printf("%ld 秒\n", t1 - t0);
    return 0;
}
