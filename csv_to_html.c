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
                } else {
                    status = 2;
                }
                break;
            case 1:
                if (c == '"') {
                    status = 0;
                }
                break;
            case 2:

                break;
            default:
                ;
        }
        // printf("%d", status);
        printf("%x ", c);
        // putchar(c);
        c = getc(fpr);
    }

    fclose(fpr);
    return 0;
}
