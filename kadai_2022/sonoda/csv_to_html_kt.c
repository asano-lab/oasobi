/*
19T2805H 小柳太一
課題5：CSVをHTMLに変換するC言語プログラム
*/


#include<stdio.h>

void main(){

    FILE *csv,*html;
    char *fname_csv = "test.csv";
    char *fname_html = "csv_to_html.html";
    char buf[100];
    char first[100] = "<html><body><table border=1>";
    char end[100] = "</table></body></html>";
    int i,flag_td,flag_wq;

    csv = fopen(fname_csv, "r");
    html = fopen(fname_html,"w");

    fprintf(html, "%s",first);

    while( fgets( buf, 100, csv ) != NULL ){

        i = 0,flag_td = 0,flag_wq = 0;
        printf("%s", buf);
        fprintf(html,"<tr>");

        while(buf[i] != NULL){

            // セル先頭に「”」があるかをチェック
            if((flag_td == 0) && (flag_wq == 0) && (buf[i] == '"')) flag_wq = 1;
            // セル末尾に「”」があるかをチェック
            if((flag_wq == 1) && (buf[i] == '"') && ((buf[i+1] == ',')||(buf[i+1] == NULL))) flag_wq = 0;


            // 「,」が2つ並んだ時の処理
            if((flag_td == 0) && (buf[i] == ',')){
                fprintf(html,"<td></td>");
            }
            // 「”」に挟まれた文章中の「,」はHTMLに出力
            else if((flag_wq == 1 ) && (buf[i] == ',')){
                fprintf(html,"%c",buf[i]);
            }
            // セル先頭であれば「<td>」を挿入
            else if(flag_td == 0){
                flag_td = 1;
                fprintf(html,"<td>");
                // 先頭の「"」を消去
                if((buf[i] == '"')){
                    printf("\n");
                }
                else{
                    fprintf(html,"%c",buf[i]);
                }
            }
            // セル末尾なら「</td>」を挿入
            else if((flag_td == 1 ) && (buf[i] == ',')){
                fprintf(html,"</td>");
                flag_td = 0;
            }
            // 「”」が2つ並んだときは1つにまとめる
            else if((flag_wq == 1) && (buf[i] == '"') && (buf[i+1] == '"')){
                fprintf(html,"%c",buf[i]);
                i++;
            }
            // 末尾の「"」を消去
            else if((flag_td == 1 ) && (flag_wq == 0 ) && (buf[i] == '"')){
                printf("\n");
            }
            // 上記条件以外の文字列をHTMLに出力
            else{
                fprintf(html,"%c",buf[i]);
            }
            // 次の文字へ移動
            i++;
        }
        fprintf(html,"</tr>");
    }

    fprintf(html, "%s",end);

    fclose(csv);
    fclose(html);

    return 0;

}
