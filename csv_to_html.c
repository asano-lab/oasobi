#include <stdio.h>

int main(int argc, char **argv) {
    FILE *fp;
    char c;

    if (argc != 3) {
        return -1;
    }

    if ((fp = fopen(argv[1], "r")) == NULL) {
        printf("\a%s file open failed\n", argv[1]);
        return -1;
    }

    c = getc(fp);
    while (c != EOF) {
        c = getc(fp);
        putchar(c);
    }

    fclose(fp);
    return 0;
}
