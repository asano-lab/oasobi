/* som.c */
#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("som test 1\n");
    printf("som test 2\n");
    for (int i = 0; i < argc; i++) {
        printf("%s\n", argv[i]);
    }
    return 0;
}
