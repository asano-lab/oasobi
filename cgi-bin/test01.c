#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand(time(NULL));
    char str[] =
        "Content-type: text/html; charset=UTF-8\n"
        "<html>\n"
        "<head>\n"
        "<title>乱数を表示する</title>\n"
        "</head>\n"
        "<body>\n"
        "<h1>乱数</h1>\n"
        "<p>%d</p>\n"
        "</body>\n"
        "</html>\n";
    printf(str, rand());
    return 0;
}