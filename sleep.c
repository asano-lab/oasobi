#include <stdio.h>
#include <unistd.h>

int main(void) {
    printf("Hello World!!\n");
    for (int i = 0; i < 10; i++) {
        usleep(100000);
        printf("%d\n", i);
    }
    return 0;
}
