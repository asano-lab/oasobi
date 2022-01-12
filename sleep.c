#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int writeFile(const char *fname, const char *str) {
    FILE *fp;
    if ((fp = fopen(fname, "a")) == NULL) {
        printf("\a%s can't be opened!!\n", fname);
        return -1;
    }
    fprintf(fp, "%s", str);
    fclose(fp);
    return 0;
}

int main(void) {
    char fname[FILENAME_MAX] = "sleep.txt";
    char str[BUFSIZ];
    char buf[BUFSIZ];
    char c;
    printf("Hello World!!\n");
    while ((c = getchar()) != '\n') {
        for (int i = 0; i < 10; i++) {
            usleep(500000);
            snprintf(str, BUFSIZ, "%c", c);
            writeFile(fname, str);
        }
        putchar(10);
    }
    return 0;
}
