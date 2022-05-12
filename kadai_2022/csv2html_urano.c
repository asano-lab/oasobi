#include <stdio.h>
#include <string.h>

int main(void){
	char *string;
	char cell[256];
	int cnt;
	int c = 1;
	int i;
	int j;

	FILE *fin = fopen("test.csv","rt");
	if (!fin){
		perror("fopen");
		return 1;
	}
	FILE *fin_html = fopen("test.html","at+");
	if (!fin_html){
		perror("fopen");
		return 1;
	}
	fprintf(fin_html,"<table border=\"1\">\n",256);
	while (fgets(string,256,fin)!=NULL){
		fprintf(fin_html,"<tr>\n",256);
        cnt=0;
		for (i=0;string[i]!=0x00;i++){
			if (string[i]== '\"'){
				if (string[i+1]!= '\"'){
					if (c){
						c=0;
						cnt=i+1;
					} else{
						c=1;
					}
				} else{
					i++;
				}
			}
			if (string[i]==','){
				if (c){
					fprintf(fin_html,"<td>\n",256);
					if (i!=0 | cnt>0){
					    for (j=0;j+cnt<i;j++){
					    	if(string[j+cnt]=='\"'){
					    		if(string[j+cnt+1]=='\"'){
					    			cell[j]=string[j+cnt];
								    cnt++;
								}
							}else{
								cell[j]=string[j+cnt];
							}
		                }
						if(cnt!=i){
							fprintf(fin_html,cell,256);
						}
					    cnt=i+1;
					    memset(cell, '\0', sizeof(cell));
				    }
				    fprintf(fin_html,"</td>\n",256);
				}
			}
		}
		fprintf(fin_html,"<td>\n",256);
		if(cnt!=i){
			for (j=0;j+cnt<i-1;j++){
					    	if(string[j+cnt]=='\"'){
					    		if(string[j+cnt+1]=='\"'){
					    			cell[j]=string[j+cnt];
								    cnt++;
								}
							}else{
								cell[j]=string[j+cnt];
							}
		                }
						if(cnt!=i-1){
							fprintf(fin_html,cell,256);
						}
					    cnt=i+1;
					    memset(cell, '\0', sizeof(cell));
		}
		fprintf(fin_html,"</td>\n",256);
		fprintf(fin_html,"</tr>\n",256);
	}
	fprintf(fin_html,"</table>",256);
	fclose(fin);
	fclose(fin_html);
	return 0;
}
