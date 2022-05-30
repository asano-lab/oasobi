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
	int cnt; // データ開始ポインタ
	int wq_closed = 1; // ダブルクォートが閉じているかどうか??
	int i;
	int j;

	FILE *fin = fopen("csv/sample002.csv", "rt");
	if (!fin) {
		perror("fopen");
		return 1;
	}
	snprintf(fname_html, FILENAME_MAX, "html/%s_sample002.html", argv[0]);
	FILE *fin_html = fopen(fname_html, "wt");
	if (!fin_html) {
		perror("fopen");
		return 1;
	}
	fprintf(fin_html,"<table border=\"1\">\n");
	// 行ごとの文字列をstringに格納
	while (fgets(string, BUFFER_MAX, fin) != NULL) {
		fprintf(fin_html, "<tr>\n");
        cnt = 0;
		// 行から1文字ずつ取得
		for (i = 0; string[i] != '\0'; i++) {
			printf("%c, %d\n", string[i], wq_closed);
			if (string[i]== '\"') {
				// ダブルクォートが連続したらフラグはそのまま
				if (string[i + 1] == '\"') {
					i++;
				}
				else {
					// 既に閉じていればデータ開始ポインタ更新
					if (wq_closed) {
						cnt = i + 1;
					}
					// フラグ切り替え
					wq_closed ^= 1;
				}
			}
			else if (string[i] == ',' && wq_closed) {
				fprintf(fin_html, "<td>\n");
				if (i != 0 || cnt > 0) {
					for (j = 0; j + cnt < i; j++) {
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
					if (cnt != i) {
						puts(cell);
						fprintf(fin_html, "%s", cell);
					}
					cnt = i + 1;
					memset(cell, '\0', sizeof(cell));
				}
				fprintf(fin_html, "</td>\n");
			}
		}
		// 行の処理終了
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
