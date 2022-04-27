#include <stdio.h>
#include <stdlib.h>

#define Num_Terminal 2
#define Num_Transpoder 1

#define Buffer_Max 64

#define END 0xC0
#define ESC 0xDB
#define ESC_END 0xDC
#define ESC_ESC 0xDD

#define print_size(x) printf("%ld\n", sizeof(x))
#define print_byte_array(A, n) do {for (int _ = 0; _ < (n); _++) printf("%02x ", (A)[_]); putchar(10);} while (0)
#define coppy_array(src, dst, n) for (int _ = 0; _ < (n); _++) (dst)[_] = (src)[_]

union position {
    struct {
        float x;
        float y;
        float z;
    };
    u_char bin[sizeof(float)];
};

u_char Buffer_T_Terminal[Num_Terminal][Buffer_Max];
u_char Buffer_R_Terminal[Num_Terminal][Buffer_Max];

int slip_enc(u_char *buf, int p_len) {
    u_char tmp[Buffer_Max];
    int i, j;
    coppy_array(buf, tmp, p_len);

    j = 0;
    for (i = 0; i < p_len; i++) {
        if (tmp[i] == END) {
            buf[j++] = ESC;
            buf[j++] = ESC_END;
        }
        else if (tmp[i] == ESC) {
            buf[j++] = ESC;
            buf[j++] = ESC_ESC;
        }
        else {
            buf[j++] = tmp[i];
        }
        if (j >= Buffer_Max - 1) {
            return -1;
        }
    }
    buf[j++] = END;
    return j;
}

int slip_dec(u_char *buf) {
    int i, j, status;
    j = 0;
    status = 0;
    for (i = 0; buf[i] != END; i++) {
        if (status == 0) {
            if (buf[i] == ESC) {
                status = 1;
            }
            else {
                buf[j++] = buf[i];
            }
        }
        else {
            if (buf[i] == ESC_END) {
                buf[j++] = END;
            }
            else if (buf[i] == ESC_ESC) {
                buf[j++] = ESC;
            }
            else {
                return -1;
            }
            status = 0;
        }
    }
    return j - 1;
}

int main(void) {
    int n;
    // printf("%d %d\n", Num_Terminal, Num_Transpoder);
    printf("%ld\n", sizeof Buffer_T_Terminal);

    Buffer_T_Terminal[0][0] = 0x12;
    Buffer_T_Terminal[0][1] = 0xC0;
    Buffer_T_Terminal[0][2] = 0x56;
    Buffer_T_Terminal[0][3] = 0xDB;
    Buffer_T_Terminal[0][4] = 0x9A;

    print_byte_array(Buffer_T_Terminal[0], 4);

    union position p;
    p.x = 1.1f;
    p.y = 2.2f;
    p.z = 0.0f;
    // printf("%f %f %f\n", p.x, p.y, p.z);

    print_byte_array(p.bin, 12);
    // print_size(p.z);

    n = slip_enc(Buffer_T_Terminal[0], 5);
    print_byte_array(Buffer_T_Terminal[0], n);

    coppy_array(Buffer_T_Terminal[0], Buffer_R_Terminal[1], Buffer_Max);

    print_byte_array(Buffer_R_Terminal[1], Buffer_Max);
    
    n = slip_dec(Buffer_R_Terminal[1]);
    print_byte_array(Buffer_R_Terminal[1], n);

    return 0;
}
