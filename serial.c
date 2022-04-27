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

void slip_enc(u_char *buf, int buf_len) {
    u_char tmp[Buffer_Max];
    int i, j;
    coppy_array(buf, tmp, buf_len);
    for (i = 0; i < buf_len; i++) {
        ;
    }
    print_byte_array(tmp, buf_len);
}

int main(void) {
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

    slip_enc(Buffer_T_Terminal[0], 5);

    return 0;
}
