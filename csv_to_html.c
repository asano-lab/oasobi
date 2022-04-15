#include <stdio.h>
#include <string.h>
#include <sys/stat.h>

int main(int argc, char **argv) {
    FILE *fpr, *fpw;
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
        printf("\a\"%s\" file open failed to read.\n", argv[1]);
        return -1;
    }
    
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

    argv[1][last_dot] = '\0';
    snprintf(fnamew, FILENAME_MAX, "%s%s.html", dir_path, argv[1] + last_slash);

    if ((fpw = fopen(fnamew, "w")) == NULL) {
        printf("\a\"%s\" file open failed to write.\n", fnamew);
        return -1;
    }
    
    puts(fnamew);

    c = getc(fpr);
    fprintf(fpw, "<html><table border=1><tr><td>");
    while (c != EOF) {
        // putchar(c);
        switch (status) {
            case 0: // データ開始
                if (c == '"') {
                    status = 1;
                    break;
                }
                if (c == ',') {
                    fprintf(fpw, "</td><td>");
                    break;
                }
                if (c == '\n') {
                    fprintf(fpw, "</td></tr><tr><td>");
                    break;
                }
                putc(c, fpw);
                status = 3;
                break;
            case 1:
                if (c == '"') {
                    status = 2;
                    break;
                }
                putc(c, fpw);
                break;
            case 2:
                if (c == '"') {
                    status = 1;
                    putc(c, fpw);
                    break;
                }
                if (c == ',') {
                    fprintf(fpw, "</td><td>");
                    status = 0;
                    break;
                }
                if (c == '\n') {
                    fprintf(fpw, "</td></tr><tr><td>");
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
                    fprintf(fpw, "</td><td>");
                    status = 0;
                    break;
                }
                if (c == '\n') {
                    fprintf(fpw, "</td></tr><tr><td>");
                    status = 0;
                    break;
                }
                putc(c, fpw);
                break;
            default:
                ;
        }
        c = getc(fpr);
    }
    fprintf(fpw, "</td></tr></table></html>");

    fclose(fpr);
    fclose(fpw);
    return 0;
}
