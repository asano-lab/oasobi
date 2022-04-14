#include <stdio.h>

int main(int argc, char **argv) {
    FILE *fpr;
    char c;
    int status = 0;

    if (argc != 2) {
        return -1;
    }

    if ((fpr = fopen(argv[1], "r")) == NULL) {
        printf("\a%s file open failed\n", argv[1]);
        return -1;
    }

    c = getc(fpr);
    printf("<html><table border=1><tr><td>");
    while (c != EOF) {
        // putchar(c);
        switch (status) {
            case 0:
                if (c == '"') {
                    status = 1;
                    break;
                }
                if (c == ',') {
                    printf("</td><td>");
                    break;
                }
                if (c == '\n') {
                    printf("</tr><tr>");
                    break;
                }
                putchar(c);
                status = 3;
                break;
            case 1:
                if (c == '"') {
                    status = 2;
                    break;
                }
                putchar(c);
                break;
            case 2:
                if (c == '"') {
                    status = 1;
                    putchar(c);
                    break;
                }
                if (c == ',') {
                    printf("</td><td>");
                    status = 0;
                    break;
                }
                if (c == '\n') {
                    printf("</tr><tr>");
                    status = 0;
                    break;
                }
                break;
            case 3:
                if (c == '"') {
                    status = -1;
                    break;
                }
                if (c == ',') {
                    printf("</td><td>");
                    status = 0;
                    break;
                }
                if (c == '\n') {
                    printf("</tr><tr>");
                    status = 0;
                    break;
                }
                putchar(c);
                break;
            default:
                ;
        }
        // printf("%d", status);
        // printf("%x ", c);
        // putchar(c);
        c = getc(fpr);
    }
    printf("</td></tr></table></html>");

    fclose(fpr);
    return 0;
}
