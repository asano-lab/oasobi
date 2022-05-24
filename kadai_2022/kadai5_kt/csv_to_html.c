/*
19T2805H ��������
�ۑ�5�FCSV��HTML�ɕϊ�����C����v���O����
*/


#include<stdio.h>

void main(){

    FILE *csv,*html;
    char *fname_csv = "test1.csv";
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

            // �Z���擪�Ɂu�h�v�����邩���`�F�b�N
            if((flag_td == 0) && (flag_wq == 0) && (buf[i] == '"')) flag_wq = 1;
            // �Z�������Ɂu�h�v�����邩���`�F�b�N
            if((flag_wq == 1) && (buf[i] == '"') && ((buf[i+1] == ',')||(buf[i+1] == NULL))) flag_wq = 0;


            // �u,�v��2���񂾎��̏���
            if((flag_td == 0) && (buf[i] == ',')){
                fprintf(html,"<td></td>");
            }
            // �u�h�v�ɋ��܂ꂽ���͒��́u,�v��HTML�ɏo��
            else if((flag_wq == 1 ) && (buf[i] == ',')){
                fprintf(html,"%c",buf[i]);
            }
            // �Z���擪�ł���΁u<td>�v��}��
            else if(flag_td == 0){
                flag_td = 1;
                fprintf(html,"<td>");
                // �擪�́u"�v������
                if((buf[i] == '"')){
                    printf("\n");
                }
                else{
                    fprintf(html,"%c",buf[i]);
                }
            }
            // �Z�������Ȃ�u</td>�v��}��
            else if((flag_td == 1 ) && (buf[i] == ',')){
                fprintf(html,"</td>");
                flag_td = 0;
            }
            // �u�h�v��2���񂾂Ƃ���1�ɂ܂Ƃ߂�
            else if((flag_wq == 1) && (buf[i] == '"') && (buf[i+1] == '"')){
                fprintf(html,"%c",buf[i]);
                i++;
            }
            // �����́u"�v������
            else if((flag_td == 1 ) && (flag_wq == 0 ) && (buf[i] == '"')){
                printf("\n");
            }
            // ��L�����ȊO�̕������HTML�ɏo��
            else{
                fprintf(html,"%c",buf[i]);
            }
            // ���̕����ֈړ�
            i++;
        }
        fprintf(html,"</tr>");
    }

    fprintf(html, "%s",end);

    fclose(csv);
    fclose(html);

    return 0;

}
