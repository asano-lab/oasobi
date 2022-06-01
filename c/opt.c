// Copyright
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc <= 1) {
        fprintf(stderr, "usage: %s <number>\n", argv[0]);
        return 1;
    }

    int n = strtol(argv[1], NULL, 0);
    if (n + 1 > n) {
        printf("%d > %d\n", n + 1, n);
    } else {  // else
        printf("%d < %d [Overflow!]\n", n + 1, n);
    }

    return 0;
}
