#include <stdio.h>
#include <string.h>

#define BUFFER_MAX 256

int main(int argc, char *argv[]) {
	if (argc > 1) {
		printf("arguments count: %d\n", argc);
	}
	char fname_html[FILENAME_MAX];
	char string[BUFFER_MAX];
	char cell[BUFFER_MAX];
	int cnt;
	int c = 1;
	int i;
	int j;

	FILE *fin = fopen("csv/sample001.csv", "rt");
	if (!fin) {
		perror("fopen");
		return 1;
	}
	snprintf(fname_html, FILENAME_MAX, "html/%s_sample001.html", argv[0]);
	FILE *fin_html = fopen(fname_html, "at+");
	if (!fin_html) {
		perror("fopen");
		return 1;
	}
	fprintf(fin_html,"<table border=\"1\">\n");
	while (fgets(string, BUFFER_MAX, fin) != NULL) {
		fprintf(fin_html, "<tr>\n");
        cnt = 0;
		for (i = 0; string[i] != 0x00; i++) {
			if (string[i]== '\"') {
				if (string[i + 1] != '\"') {
					if (c) {
						c = 0;
						cnt = i + 1;
					} else {
						c = 1;
					}
				} else {
					i++;
				}
			}
			if (string[i] == ','){
				if (c) {
					fprintf(fin_html, "<td>\n");
					if (i != 0 || cnt > 0) {
					    for (j = 0; j + cnt < i; j++) {
					    	if (string[j + cnt]=='\"') {
					    		if(string[j + cnt + 1]=='\"') {
					    			cell[j] = string[j + cnt];
								    cnt++;
								}
							} else {
								cell[j] = string[j + cnt];
							}
		                }
						if (cnt != i){
							fprintf(fin_html, "%s", cell);
						}
					    cnt = i + 1;
					    memset(cell, '\0', sizeof(cell));
				    }
				    fprintf(fin_html, "</td>\n");
				}
			}
		}

		fprintf(fin_html, "<td>\n");
		if (cnt != i) {
			for (j = 0; j + cnt < i - 1; j++) {
				if (string[j + cnt] == '\"') {
					if (string[j + cnt + 1] == '\"') {
						cell[j] = string[j + cnt];
						cnt++;
					}
				}
				else {
					cell[j] = string[j + cnt];
				}
			}
			if (cnt != i - 1) {
				fprintf(fin_html, "%s", cell);
			}
			cnt = i + 1;
			memset(cell, '\0', sizeof(cell));
		}
		fprintf(fin_html, "</td>\n");
		fprintf(fin_html, "</tr>\n");
	}

	fprintf(fin_html,"</table>");
	fclose(fin);
	fclose(fin_html);
	return 0;
}
