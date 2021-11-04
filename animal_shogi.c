#include <stdio.h>
#include <stdlib.h>
#include "animal_shogi.h"

int main(void) {
    showBoard(INITIAL_BOARD);
    return 0;
}

// 盤面表示
void showBoard(u_long b) {
    int i, j;
    u_char p, own_p, own_p_num;
    own_p = b >> 48;
    printf("E: ");
    for (i = 0; i < 3; i++) {
        own_p_num = own_p >> (i * 2);
        for (j = 0; j < own_p_num; j++) {
            putchar(DISPLAY_PEACES[i]);
            printf("2 ");
        }
    }
    putchar(10);
    for (i = 0; i < 4; i ++) {
        for (j = 0; j < 3; j++) {
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
    own_p = b >> 54;
    printf("D: ");
    for (i = 0; i < 3; i++) {
        own_p_num = own_p >> (i * 2);
        for (j = 0; j < own_p_num; j++) {
            putchar(DISPLAY_PEACES[i]);
            printf("1 ");
        }
    }
    putchar(10);
}
