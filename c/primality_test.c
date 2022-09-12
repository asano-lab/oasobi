#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define N 100

int main(void) {
    int i, j, n;
    u_int prime_numbers[N];
    bool prime_flag;
    prime_numbers[0] = 2;

    i = 1;
    for (n = 3; i < N; n++) {
        printf("%d: ", n);
        prime_flag = true;
        for (j = 0; j < i; j++) {
            if (n % prime_numbers[j] == 0) {
                printf("smallest prime factor is %d\n", prime_numbers[j]);
                prime_flag = false;
                break;
            }
        }
        if (prime_flag) {
            // printf("%d\n", n);
            printf("prime number\n");
            prime_numbers[i++] = n;
        }
    }
    return 0;
}