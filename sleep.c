#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(void) {
    FILE *fp;
    char fname[FILENAME_MAX] = "sleep.txt";
    printf("Hello World!!\n");
    if ((fp = fopen(fname, "a")) == NULL) {
        printf("\a%s can't be opened!!\n", fname);
        return -1;
    }
    for (int i = 0; i < 10; i++) {
        usleep(100000);
        fprintf(fp, "%d\n", i);
    }
    fclose(fp);
    return 0;
}
