#ifndef ANIMAL_SHOGI_H
#define ANIMAL_SHOGI_H

#define INITIAL_BOARD (long)0xa003c914b002

// 表示する文字
#define DISPLAY_PEACES " HGELC"

enum PEACES {EMPTY, CHICK, GIRAFFE, ELEPHANT, LION, CHICKEN};

void showBoard(long b);

#endif