#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define EARTH_RADIUS 6371

#define PI 3.1415926535897932

#define deg_to_rad(x) ((x) / 180.0 * PI)

typedef struct list {
    double lat;
    double lon;
    struct list *next;
} List;

List *START;

// リスト全開放
void del_list() {
    List *crnt = START;
    List *dst;
    while (crnt != NULL) {
        // printf("%f, %f, %lx\n", crnt->lat, crnt->lon, (u_long)crnt->next);
        dst = crnt->next;
        free(crnt);
        crnt = dst;
    }
}

// 距離計算
double calc_dist() {
    List *l1 = START;
    List *l2 = l1->next;
    double b, c, alpha;
    double dist = 0.0;

    while (l2->next != NULL) {
        // printf("%f, %f, %lx, ", l1->lat, l1->lon, (u_long)l1->next);
        // printf("%f, %f, %lx\n", l2->lat, l2->lon, (u_long)l2->next);
        b = deg_to_rad(l1->lat);
        c = deg_to_rad(l2->lat);
        alpha = deg_to_rad(l2->lon - l1->lon);
        dist += EARTH_RADIUS * acos(sin(b) * sin(c) + cos(b) * cos(c) * cos(alpha));
        l1 = l2;
        l2 = l1->next;
    }
    return dist;
}

int main(int argc, char **argv) {
    FILE *fpr;
    char c;
    char buffer[256];

    int i, tmp1, tmp2;
    int status = 0;
    double f;

    START = (List*)malloc(sizeof(List));
    START->next = NULL;
    List *crnt = START;
    List *dst;

    if (argc != 2) {
        return -1;
    }

    if ((fpr = fopen(argv[1], "r")) == NULL) {
        printf("\a\"%s\" file open failed to read.\n", argv[1]);
        return -1;
    }

    c = getc(fpr);

    while (c != EOF) {
        // putchar(c);
        if (status == 0) {
            if (c == '$') {
                i = 0;
                status = 1;
            }
        }
        else if (status == 1) {
            if (c == "GPGGA,"[i++]) {
                if (i == 6) {
                    status = 2;
                }
            } else {
                status = 0;
            }
        } else if (status == 2) {
            if (c == ',') {
                status = 3;
                i = 0;
            }
        } else if (status == 3) {
            if (c == '.') {
                buffer[i] = '\0';
                tmp1 = strtol(buffer, NULL, 10);
                i = 0;
                status = 4;
            } else {
                buffer[i++] = c;
            }
        } else if (status == 4) {
            if (c == ',') {
                buffer[i] = '\0';
                tmp2 = strtol(buffer, NULL, 10);
                crnt->lat = (double)(tmp1 / 100) + ((double)(tmp1 % 100) + (double)tmp2 / 10000.0) / 60.0;
                i = 0;
                status = 5;
            } else {
                buffer[i++] = c;
            }
        } else if (status == 5) {
            if (c == 'S') {
                crnt->lat = -crnt->lat;
            } else if (c == ',') {
                status = 6;
            }
        } else if (status == 6) {
            if (c == '.') {
                buffer[i] = '\0';
                tmp1 = strtol(buffer, NULL, 10);
                i = 0;
                status = 7;
            } else {
                buffer[i++] = c;
            }
        } else if (status == 7) {
            if (c == ',') {
                buffer[i] = '\0';
                tmp2 = strtol(buffer, NULL, 10);
                crnt->lon = (double)(tmp1 / 100) + ((double)(tmp1 % 100) + (double)tmp2 / 10000.0) / 60.0;
                i = 0;
                status = 8;
            } else {
                buffer[i++] = c;
            }
        } else if (status == 8) {
            if (c == 'W') {
                crnt->lon = -crnt->lon;
            } else if (c == ',') {
                dst = (List*)malloc(sizeof(List));
                crnt->next = dst;
                crnt = dst;
                status = 0;
            }
        }
        c = getc(fpr);
    }
    f = calc_dist();
    printf("%f\n", f);

    // printf("################################################\n");
    del_list();

    fclose(fpr);
    return 0;
}
