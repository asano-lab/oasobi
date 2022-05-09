#include <stdio.h>
#include <string.h>
/* 第一コマンドライン引数に与えるCSVファイルをHTMLテーブルに変換して、標準出力するCプログラムです。
改行コードはCRLFとLFのみ動作確認済みです。

利用方法：
gcc -o convertcsv convertcsv.c
./convertcsv example1.csv > example1.html

入力例：example1.csv
出力例：
<table border=1>
<tr><td>4343</td><td>test"</td><td>row1</td><td>33</td><td></td></tr>
<tr><td>32</td><td>fa</td><td></td><td>fa</td><td></td></tr>
<tr><td>fas"d</td><td></td><td>32</td><td></td><td></td></tr>
<tr><td>ju,fd eiia fadd</td><td>23</td><td>fd</td><td>table'3'</td><td>fd</td></tr>
</table>

Nice to do：
・余力があれば、#でコメントしてある部分の処理を追加する

感想：
・標準出力かそれともファイルに出力させるのかどっちが使い勝手がいいのだろう？
・他にもっといいアルゴリズムがありそう。
    正規表現を使えるなら、\"([^\"]*)\"で一つのデータに分けれる。
*/
char *strtokc(char *str1, char *str2)
{
    /* strtokは標準Cライブラリ関数で文字列からトークンを取り出す（man strtokより）。
    これは連続する区切り文字を無視しないstrtok関数
    https：//gist.github.com/YasKamito/5513686be65a6dd1f6918c02080bb97e
    */
    static char *str = 0;
    if (str1)
        str = str1;
    else
        str1 = str;
    if (!str1)
        return (0);
    while (1)
    {
        if (!*str)
        {
            str = 0;
            return (str1);
        }
        if (*str == *str2)
        {
            *str++ = 0;
            return (str1);
        }
        str++;
    }
}
void strrep(char *str, const char *strsearch, const char *strnew)
{
    /* 検索文字列を置き換える関数
    渡辺研究室 名古屋大学。http：//www.is.nagoya-u.ac.jp/dep-cs/vi/graduates/04year/yabuta/program/C/strrep.txt
    引数：入力文字列（char型ポインタ）、検索文字列（char型ポインタ）、新しい文字列（char型ポインタ）
    返り値：なし
    */
    int targetlen = strlen(strsearch); //置換対象文字列の長さ
    int newlen = strlen(strnew);       //置換後文字列の長さ
    int _strlen = strlen(str);         //文字列の長さ
    char *replace_pos;                 //検索を開始する位置
    //置換文字列の場所を検索
    while (NULL != (replace_pos = strstr(str, strsearch)))
    {
        //文字列を挿入する場所を作成する
        memmove(replace_pos + newlen, replace_pos + targetlen, strlen(replace_pos) - targetlen);
        //置換文字列を挿入する
        memmove(replace_pos, strnew, newlen);
        //文字数が少なくなる場合、NULLコードの位置も変更
        if (targetlen > newlen)
        {
            *(str + _strlen - targetlen + newlen) = '\0';
            _strlen = strlen(str);
        }
    }
}
int strcount(char str[], char strsearch)
{
    /* 特定文字の数をカウントする関数
    引数：検索対象（char型配列）、検索したい文字（char型ポインタ）
    返り値：見つかった文字の数（int型数）
    */
    int i;
    int count = 0;
    for (i = 0; str[i] != '\0'; i++)
        if (str[i] == strsearch)
            count++;
    return count;
}
void tok2str(char *str, char *tok)
{
    /* トークンをコピー後、いらない文字列を消してstr変数をいい感じの文字列にする関数（トークンを書き換えるとおかしくなるので）
    引数：加工する・された文字列（char型ポインタ）、正規化したいトークン（char型ポインタ）
    返り値：なし
    */
    strcpy(str, tok);
    strrep(str, "\"\"", "_");
    strrep(str, "\"", "");
    strrep(str, "_", "\"");
}
void printtd(char *str, char *tok)
{
    /* テーブルデータを表示する関数
    引数：加工する・された文字列（char型ポインタ）、テーブルデータにしたいトークン（char型ポインタ）
    返り値：なし
    */
    if (strcount(tok, '\"') % 2 == 0)
    // トークンのダブルクオートの数が偶数のとき
    {
        tok2str(str, tok);
        printf("%s", str);
    }
    else
    // トークンのダブルクオートの数が奇数のとき
    {
        tok2str(str, tok);
        printf("%s,", str);
        while ((tok = strtokc(NULL, ",")) && (strcount(tok, '\"') % 2 == 0))
        // 順に取得するトークンのダブルクオートの数が偶数の間。
        //#適切なCSVファイルじゃないと無限ループに陥るかも？エラー処理を追加したい。
        {
            tok2str(str, tok);
            printf("%s,", str);
        }
        tok2str(str, tok);
        printf("%s", str);
    }
}
int main(int argc, char *argv[])
{
    /* main関数
    引数：入力CSVファイル名（第一コマンドライン引数）
    返り値：echo $?で確認できる終了ステータス（int型）
    */
    FILE *fp = fopen(argv[1], "r");               // 第一コマンドライン引数のCSVファイルを読み込む（ファイル型ポインタ）。
                                                  //#fopen_s()を使ってセキュアにして、さらにエラー処理を追加したい。
    char buflinestr[BUFSIZ];                      // テキストファイル中のある一行の文字列（char型配列）
    char bufstr[BUFSIZ];                          // 加工する・された文字列（char型配列）
    char *tok;                                    // トークン（char型ポインタ）
                                                  // strtok()系を使った後は参照元のオブジェクトを変更してはいけない。
    puts("<table border=1>");                     // puts()はOSによって出力される改行コードが異なる。
    while (fgets(buflinestr, BUFSIZ, fp) != NULL) // 一行ずつ取得。
    {
        tok = strtokc(buflinestr, ","); // カンマで区切られたトークンを取得
        printf("<tr>");
        printf("<td>");
        printtd(bufstr, tok);
        printf("</td>");
        while (tok = strtokc(NULL, ",")) // 取得するトークンがなくなるまで
        {
            printf("<td>");
            printtd(bufstr, tok);
            printf("</td>");
        }
        puts("</tr>");
    }
    puts("</table>");
    fclose(fp); //#fclose()のエラー処理を追加したい。
    return 0;
}
