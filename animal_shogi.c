#include <stdio.h>
#include <stdlib.h>
#include "animal_shogi.h"

int main(void) {
    printf("Hello World!!\n");
    showBoard(INITIAL_BOARD);
    return 0;
}

void showBoard(long b) {
    u_char p;
    for (int i = 0; i < 4; i ++) {
        for (int j = 0; j < 3; j++) {
            p = (b >> (44 - i * 4 - j * 16)) & 0b1111;
            putchar(DISPLAY_PEACES[p & 0b0111]);
            if (p & 0b1000) {
                putchar('2');
            } else if (p) {
                putchar('1');
            } else {
                putchar(' ');
            }
            putchar(' ');
        }
        putchar(10);
    }
    putchar(10);
}
