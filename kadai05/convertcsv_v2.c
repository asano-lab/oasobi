#include "lib/mylib.h"

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
        while ((tok = strtokc(NULL, ","))) // 取得するトークンがなくなるまで
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
