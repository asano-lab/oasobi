#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void) {
    char c;
    char month_str[3];
    int month_int;
    char date_str[3];
    int date_int;
    
    printf("日付を入力してください (MM/DD): ");
    // 月の取得
    for (int i = 0; i < 2; i++) {
        if (!isdigit(c = getchar())) {
            return -1;
        }
        month_str[i] = c;
    }
    month_str[2] = '\0';
    month_int = strtol(month_str, NULL, 10);
    if (month_int < 1 || 12 < month_int) {
        return -1;
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
        return -1;
    }

    date_int = strtol(date_str, NULL, 10);
    if (date_int < 1 || 31 < date_int) {
        return -1;
    }
    printf("%02d/%02d\n", month_int, date_int);
    return 0;
}
