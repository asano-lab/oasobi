#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void) {
    char c;
    char date_str[3];
    int date_int;
    
    printf("日付を入力してください (MM/DD): ");
    for (int i = 0; i < 2; i++) {
        if (!isdigit(getchar())) {
            return -1;
        }
    }
    if (getchar() != '/') {
        return -1;
    }
    for (int i = 0; i < 2; i++) {
        if (!isdigit(c = getchar())) {
            return -1;
        }
        date_str[i] = c;
    }
    date_str[2] = '\0';
    if (getchar() != '\n') {
        while (getchar() != '\n');
        return -1;
    }

    printf("%s\n", date_str);
    return 0;
}
