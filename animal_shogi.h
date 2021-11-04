#ifndef ANIMAL_SHOGI_H
#define ANIMAL_SHOGI_H

#define INITIAL_BOARD (u_long)0xa003c914b002

// 表示する文字
#define DISPLAY_PEACES " hgelc"

enum PEACES {EMPTY, CHICK, GIRAFFE, ELEPHANT, LION, CHICKEN};

void showBoard(u_long b);

#endif