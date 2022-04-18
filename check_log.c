#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>

typedef struct list {
    double lat;
    double lon;
    struct list *next;
} List;

int main(int argc, char **argv) {
    FILE *fpr;
    char c;

    int status = 0;

    if (argc != 2) {
        return -1;
    }

    if ((fpr = fopen(argv[1], "r")) == NULL) {
        printf("\a\"%s\" file open failed to read.\n", argv[1]);
        return -1;
    }

    c = getc(fpr);
    
    while (c != EOF) {
        putchar(c);
        switch (status) {
            case 0: // データ開始
                if (c == '"') {
                    status = 1;
                    break;
                }
                if (c == ',') {
                    break;
                }
                if (c == '\n') {
                    break;
                }
                status = 3;
                break;
            case 1: // ダブルクォート内
                if (c == '"') {
                    status = 2;
                    break;
                } if (c == '\n') {
                    ;
                } else {
                    ;
                }
                break;
            case 2: // ダブルクォート外
                if (c == '"') {
                    status = 1;
                    break;
                }
                if (c == ',') {
                    status = 0;
                    break;
                }
                if (c == '\n') {
                    status = 0;
                    break;
                }
                break;
            case 3: // ダブルクォートなし
                if (c == '"') {
                    status = -1;
                    break;
                }
                if (c == ',') {
                    status = 0;
                    break;
                }
                if (c == '\n') {
                    status = 0;
                    break;
                }
                break;
            case 4: // 改行直後
                ;
            default:
                ;
        }
        c = getc(fpr);
    }

    fclose(fpr);
    return 0;
}
