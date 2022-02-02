#include <stdio.h>
#include <ctype.h>

int main(void) {
    char c;
    printf("日付を入力してください (MM/DD): ");
    if (!isdigit(getchar())) {
        puts("数値でない");
        return -1;
    }
    return 0;

}
