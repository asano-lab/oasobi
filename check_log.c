#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>

typedef struct list {
    double lat;
    double lon;
    struct list *next;
} List;

List *START;

int main(int argc, char **argv) {
    FILE *fpr;
    char c;
    char buffer[256];

    int i, tmp1, tmp2;
    int status = 0;
    double f;

    if (argc != 2) {
        return -1;
    }

    if ((fpr = fopen(argv[1], "r")) == NULL) {
        printf("\a\"%s\" file open failed to read.\n", argv[1]);
        return -1;
    }

    c = getc(fpr);

    while (c != EOF) {
        // putchar(c);
        if (status == 0) {
            if (c == '$') {
                i = 0;
                status = 1;
            }
        }
        else if (status == 1) {
            if (c == "GPGGA,"[i++]) {
                if (i == 6) {
                    status = 2;
                }
            } else {
                status = 0;
            }
        } else if (status == 2) {
            if (c == ',') {
                status = 3;
                i = 0;
            }
        } else if (status == 3) {
            if (c == '.') {
                buffer[i] = '\0';
                tmp1 = strtol(buffer, NULL, 10);
                printf("%d.", tmp1);
                i = 0;
                status = 4;
            } else {
                buffer[i++] = c;
            }
        } else if (status == 4) {
            if (c == ',') {
                buffer[i] = '\0';
                tmp2 = strtol(buffer, NULL, 10);
                printf("%d\n", tmp2);
                i = 0;
                status = 0;
            } else {
                buffer[i++] = c;
            }
        }
        c = getc(fpr);
    }

    fclose(fpr);
    return 0;
}
