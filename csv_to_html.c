#include <stdio.h>

int main(int argc, char **argv) {
    FILE *fpr;
    char c;
    int status = 0;

    if (argc != 2) {
        return -1;
    }

    if ((fpr = fopen(argv[1], "r")) == NULL) {
        printf("\a%s file open failed\n", argv[1]);
        return -1;
    }

    c = getc(fpr);
    while (c != EOF) {
        // putchar(c);
        switch (status) {
            case 0:
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
            case 1:
                if (c == '"') {
                    status = 2;
                    break;
                }
                putchar(c);
                break;
            case 2:
                if (c == '"') {
                    status = 1;
                    putchar(c);
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
            case 3:
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
                putchar(c);
                break;
            default:
                ;
        }
        // printf("%d", status);
        // printf("%x ", c);
        // putchar(c);
        c = getc(fpr);
    }

    fclose(fpr);
    return 0;
}
