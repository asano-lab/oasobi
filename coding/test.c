#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    // long r;
    srandom((unsigned)time(NULL));
    for (int i = 0; i < 10; i++) {
        printf("%ld\n", random());
    }
    printf("%d\n", RAND_MAX);

    return 0;
}
