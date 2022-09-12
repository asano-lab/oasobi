#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <sys/time.h>
#include <math.h>

#define N 1000

int main(void) {
    struct timeval t0, t1;
    double t0_sec, t1_sec;

    u_int i, j, n, sqrt_n;
    u_int prime_numbers[N];
    bool prime_flag;
    prime_numbers[0] = 2;

    gettimeofday(&t0, NULL);
    i = 1;
    printf("%d,%d\n", 1, 2);
    for (n = 3; i < N; n++) {
        sqrt_n = sqrt(n) + 1;
        // printf("%d: ", n);
        prime_flag = true;
        for (j = 0; j < i; j++) {
            if (n % prime_numbers[j] == 0) {
                // printf("smallest prime factor is %d\n", prime_numbers[j]);
                prime_flag = false;
                break;
            }
            if (prime_numbers[j] > sqrt_n) {
                break;
            }
        }
        if (prime_flag) {
            // printf("prime number\n");
            prime_numbers[i++] = n;
            printf("%d,%d\n", i, n);
        }
    }
    // putchar(10);
    gettimeofday(&t1, NULL);

    t0_sec = (double)t0.tv_sec + (double)t0.tv_usec * 1e-6;
    t1_sec = (double)t1.tv_sec + (double)t1.tv_usec * 1e-6;

    // printf("%d\n", prime_numbers[N - 1]);
    // printf("%f\n", t1_sec - t0_sec);
    return 0;
}