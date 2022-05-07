#include <stdio.h>
#include <string.h>
#include <sys/stat.h>

#define BUFFER_SIZE 18

int main(int argc, char **argv) {
    FILE *fpr, *fpw;
    struct stat st;
    char c;

    int i;
    int status = 0;
    int last_slash = -1;
    int last_dot = -1;

    char dir_path[BUFFER_SIZE];
    char fnamew[BUFFER_SIZE];

    // 引数が無い場合
    if (argc == 1) {
        printf("%s: missing file operand\n", argv[0]);
        return -1;
    }

    // ファイルが読み込めない
    if ((fpr = fopen(argv[1], "r")) == NULL) {
        printf("\a%s: cannot open '%s' for reading\n", argv[0], argv[1]);
        return -1;
    }
    
    for (i = 0; (c = argv[1][i]) != '\0' && i < BUFFER_SIZE - 1; i++) {
        fnamew[i] = c;
        if (c == '/') {
            last_slash = i;
        } else if (c == '.') {
            last_dot = i;
        }
    }
    fnamew[i] = '\0';
    puts(fnamew);

    // 拡張子チェック
    for (i = 0; i < 4; i++) {
        if (argv[1][last_dot + 1 + i] != "csv"[i]) {
            printf("\a\"%s\" is not csv file.\n", argv[1]);
            return -1;
        }
    }
    // 相対パス直下の場合はカレントディレクトリにhtmlディレクトリ作成
    if (last_slash < 0) {
        snprintf(dir_path, BUFFER_SIZE, "html");
    } else {
        fnamew[last_slash] = '\0';
        puts(fnamew + last_slash + 1);
        snprintf(dir_path, BUFFER_SIZE, "%s", fnamew);
        strncat(dir_path, "/html", strlen(dir_path) - 6);
    }
    puts(dir_path);

    // htmlディレクトリが存在しなければ作成
    if (stat(dir_path, &st) != 0) {
        if (mkdir(dir_path, 0775) == 0) {
            printf("directory '%s' was created\n", dir_path);
        } else {
            printf("\amkdir: cannot create directory '%s'\n", dir_path);
            return -1;
        }
    }
    // 同名のファイルがあった場合
    else if ((st.st_mode & S_IFMT) != S_IFDIR) {
        printf("\amkdir: cannot create directory '%s': File exists\n", dir_path);
        return -1;
    }

    argv[1][last_dot] = '\0';
    snprintf(fnamew, BUFFER_SIZE, "%s/%s.html", dir_path, argv[1] + last_slash + 1);

    if ((fpw = fopen(fnamew, "w")) == NULL) {
        printf("\a%s: cannot open '%s' for writing\n", argv[0], fnamew);
        return -1;
    }
    
    puts(fnamew);

    c = getc(fpr);
    fprintf(fpw, "<html><table border=1><tr><td>");
    while (c != EOF) {
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
            case 1: // ダブルクォート内
                if (c == '"') {
                    status = 2;
                    break;
                } if (c == '\n') {
                    fprintf(fpw, "<br>");
                } else {
                    putc(c, fpw);
                }
                break;
            case 2: // ダブルクォート外
                if (c == '"') {
                    status = 1;
                    putc(c, fpw); // エスケープ
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
            case 3: // ダブルクォートなし
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
            case 4: // 改行直後
                ;
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
