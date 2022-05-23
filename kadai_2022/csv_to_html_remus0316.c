#include <stdio.h>

int main() {
    FILE* f = fopen("csv.csv", "r");
    FILE* a = fopen("csv.html", "w");
    
    char line[500]={};
    int i=0;
    int j;
    int count=0;
    
    fprintf(a, "<table border><tr><td>");
    while ((line[i] = fgetc(f)) != EOF) {
        
        fputc(line[i], a);
        if (line[i]=='"'){
            count++; 
        }
        
        if (line[i]=='\n'){
            fprintf(a, "</td></tr><tr><td>");
        }
		if(count % 2 == 0){
            if (line[i]==','){
                fprintf(a, "</td><td>");
                }
        }

        i++;
    }
    fprintf(a, "</td></tr></table>");

    fclose(f);
    fclose(a);

	FILE* b = fopen("csv.html", "r");
	char c[500];
	char d[500];
	char e[500];
	char g[500];
	int k;
	count=0; 
	fgets( c, 500, b ); 
	fgets( d, 500, b );
	fgets( e, 500, b );
	fgets( g, 500, b );
	fclose(b);

	for(i=0;c[i]!='\0';i++){
		if(c[i]=='"'){
			count++;
		}
		if(count%2==0){
			if(c[i]==','){
				k=i;
				for(j=k;c[j]!='\0';j++){
				c[j]=c[j+1];
				}
			}
		}
	}
	for(i=0;c[i]!='\0';i++){
		if(c[i]=='>'){
			if(c[i+1]=='"'){
				k=i+1;
				for(j=k;c[j]!='\0';j++){
				c[j]=c[j+1];
				}
			}
		}
	}
	for(i=0;c[i]!='\0';i++){
		if(c[i]=='<'){
			if(c[i-1]=='"'){
				k=i-1;
				for(j=k;c[j]!='\0';j++){
				c[j]=c[j+1];
				}
			}
		}
	}	
	for(i=0;c[i]!='\0';i++){
		if(c[i]=='"'){
			if(c[i+1]=='"'){
				k=i;
				for(j=k;c[j]!='\0';j++){
					c[j]=c[j+1];
				}
			}
		}
	}

	for(i=0;d[i]!='\0';i++){
		if(d[i]=='"'){
			count++;
		}
		if(count%2==0){
			if(d[i]==','){
				k=i;
				for(j=k;d[j]!='\0';j++){
				d[j]=d[j+1];
				}
			}
		}
	}
	for(i=0;d[i]!='\0';i++){
		if(d[i]=='>'){
			if(d[i+1]=='"'){
				k=i+1;
				for(j=k;d[j]!='\0';j++){
				d[j]=d[j+1];
				}
			}
		}
	}
	for(i=0;d[i]!='\0';i++){
		if(d[i]=='<'){
			if(d[i-1]=='"'){
				k=i-1;
				for(j=k;d[j]!='\0';j++){
				d[j]=d[j+1];
				}
			}
		}
	}	
	for(i=0;d[i]!='\0';i++){
		if(d[i]=='"'){
			if(d[i+1]=='"'){
				k=i;
				for(j=k;d[j]!='\0';j++){
					d[j]=d[j+1];
				}
			}
		}
	}

	for(i=0;e[i]!='\0';i++){
		if(e[i]=='"'){
			count++;
		}
		if(count%2==0){
			if(e[i]==','){
				k=i;
				for(j=k;e[j]!='\0';j++){
				e[j]=e[j+1];
				}
			}
		}
	}
	for(i=0;e[i]!='\0';i++){
		if(e[i]=='>'){
			if(e[i+1]=='"'){
				k=i+1;
				for(j=k;e[j]!='\0';j++){
				e[j]=e[j+1];
				}
			}
		}
	}
	for(i=0;e[i]!='\0';i++){
		if(e[i]=='<'){
			if(e[i-1]=='"'){
				k=i-1;
				for(j=k;e[j]!='\0';j++){
				e[j]=e[j+1];
				}
			}
		}
	}	
	for(i=0;e[i]!='\0';i++){
		if(e[i]=='"'){
			if(e[i+1]=='"'){
				k=i;
				for(j=k;e[j]!='\0';j++){
					e[j]=e[j+1];
				}
			}
		}
	}

	for(i=0;g[i]!='\0';i++){
		if(g[i]=='"'){
			count++;
		}
		if(count%2==0){
			if(g[i]==','){
				k=i;
				for(j=k;g[j]!='\0';j++){
				g[j]=g[j+1];
				}
			}
		}
	}
	for(i=0;g[i]!='\0';i++){
		if(g[i]=='>'){
			if(g[i+1]=='"'){
				k=i+1;
				for(j=k;g[j]!='\0';j++){
				g[j]=g[j+1];
				}
			}
		}
	}
	for(i=0;g[i]!='\0';i++){
		if(g[i]=='<'){
			if(g[i-1]=='"'){
				k=i-1;
				for(j=k;g[j]!='\0';j++){
				g
				[j]=g[j+1];
				}
			}
		}
	}	
	for(i=0;g[i]!='\0';i++){
		if(g[i]=='"'){
			if(g[i+1]=='"'){
				k=i;
				for(j=k;g[j]!='\0';j++){
					g[j]=g[j+1];
				}
			}
		}
	}
	FILE* z = fopen("csv.html", "w");{
	fputs(c,z);
	fputs(d,z);
	fputs(e,z);
	fputs(g,z);
	}
	fclose(z);
	
    return 0;
}
