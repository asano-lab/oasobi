#include <stdio.h>
#include <string.h>
#include <sys/stat.h>

int main(int argc, char **argv) {
    FILE *fpr;
    struct stat st;
    char c;

    int i;
    int status = 0;
    int last_slash = 0;
    int last_dot = -1;

    char dir_path[FILENAME_MAX];
    char fnamew[FILENAME_MAX];

    if (argc != 2) {
        return -1;
    }

    if ((fpr = fopen(argv[1], "r")) == NULL) {
        printf("\a\"%s\" file open failed.\n", argv[1]);
        return -1;
    }
    
    // printf("%ld\n", strlen(argv[1]));
    for (i = 0; (c = argv[1][i]) != '\0' && i < FILENAME_MAX - 1; i++) {
        fnamew[i] = c;
        if (c == '/') {
            last_slash = i;
        } else if (c == '.') {
            last_dot = i;
        }
    }
    fnamew[last_slash] = '\0';

    for (i = 0; i < 4; i++) {
        if (argv[1][last_dot + 1 + i] != "csv"[i]) {
            printf("\a\"%s\" is not csv file.\n", argv[1]);
            return -1;
        }
    }
    snprintf(dir_path, FILENAME_MAX, "%s/html", fnamew);

    // htmlディレクトリが存在しなければ作成
    if (stat(dir_path, &st) != 0) {
        if (mkdir(dir_path, 0775) == 0) {
            printf("\"%s\" directory was created.\n", dir_path);
        } else {
            printf("\"%s\" directory create failed.\n", dir_path);
            return -1;
        }
    }
    // 同名のファイルがあった場合
    else if ((st.st_mode & S_IFMT) != S_IFDIR) {
        printf("\"%s\" file exists!\n", dir_path);
        return -1;
    }
    
    snprintf(fnamew, FILENAME_MAX, "%s%s", dir_path, argv[1] + last_slash);
    puts(fnamew);

    putchar(10);
    printf("%d, %d\n", last_slash, last_dot);

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
                    printf("</td></tr><tr><td>");
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
                    printf("</td></tr><tr><td>");
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
                    printf("</td></tr><tr><td>");
                    status = 0;
                    break;
                }
                putchar(c);
                break;
            default:
                ;
        }
        c = getc(fpr);
    }
    printf("</td></tr></table></html>");

    fclose(fpr);
    return 0;
}
