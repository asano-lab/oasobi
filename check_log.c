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

    int i;
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
        // putchar(c);
        if (status == 0) {
            if (c == '$') {
                i = 0;
                status = 1;
            }
        }
        else if (status == 1) {
            if (c == "GPGGA"[i++]) {
                putchar(c);
                if (i == 5) {
                    status = 2;
                    putchar(10);
                }
            } else {
                status = 0;
            }
        } else if (status == 2) {
            status = 0;
        }
        c = getc(fpr);
    }

    fclose(fpr);
    return 0;
}
