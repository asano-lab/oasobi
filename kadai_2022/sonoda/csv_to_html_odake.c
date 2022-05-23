#include <stdio.h>
#include <stdlib.h>

#define true 1
#define false 0

int main(int argc, char *argv[])
{
    FILE *csv_file;
    FILE *html_file;
    char *csv_file_name = "csv/sample001.csv";
    char *html_file_name = "html/sample001.html";
    char char_data;
    char write_text_first[] = "<!DOCTYPE html>\n<html>\n\t<table border=\"1\">\n";
    char write_text_end[] = "\t</table>\n</html>";
    char d_flag = false;   //ダブルクォーテーションが開いているかどうかを判断する
    char d_flag_c = false; //ダブルクォーテーションが連続しているかどうかを判断する

    if (argc == 3)
    {
        csv_file_name = argv[1];
        html_file_name = argv[2];
    }
    else if (argc != 1)
    {
        printf("引数が正しくありません。\n");
    }
    printf("入力ファイル：%s、出力ファイル：%s\n", csv_file_name, html_file_name);

    /////////////////////////////////////////////////////////
    //ファイルを開く
    /////////////////////////////////////////////////////////
    csv_file = fopen(csv_file_name, "r");
    html_file = fopen(html_file_name, "w");
    if (csv_file == NULL)
    {
        printf("%s が開けませんでした。\n", csv_file_name);
        return -1;
    }
    else if (html_file == NULL)
    {
        printf("%s が開けませんでした。\n", html_file_name);
        return -1;
    }
    else
    {
        printf("ファイルを正常に開くことができました\n");
    }
    /////////////////////////////////////////////////////////

    /////////////////////////////////////////////////////////
    //ファイルに書き込む
    /////////////////////////////////////////////////////////
    fprintf(html_file, "%s", write_text_first); //表の前までを書き込む

    fprintf(html_file, "\t<tr>\n\t\t<td>");
    while (true)
    {
        char_data = getc(csv_file);
        if (char_data == EOF)
        {
            fprintf(html_file, "</td>\n\t</tr>\n");
            break;
        }
        else if (char_data == ',' && d_flag == false)
        {
            fprintf(html_file, "</td>\n\t\t<td>");
            d_flag_c = false;
        }
        else if (char_data == '\n')
        {
            fprintf(html_file, "</td>\n\t</tr>\n\t<tr>\n\t\t<td>");
            d_flag_c = false;
        }
        else if (char_data == '\"')
        {
            d_flag = !d_flag;
            if (d_flag_c == true)
            {
                fprintf(html_file, "%c", char_data);
                d_flag_c = false;
            }
            else
            {
                d_flag_c = true;
            }
        }
        else
        {
            fprintf(html_file, "%c", char_data);
            d_flag_c = false;
        }
    }

    fprintf(html_file, "%s", write_text_end); //表の後ろを書き込む
    /////////////////////////////////////////////////////////

    fclose(csv_file);
    fclose(html_file);

    printf("終了しました\n");
}