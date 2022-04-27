#include <stdio.h>
#include <stdlib.h>

#define Num_Terminal 2
#define Num_Transpoder 1

#define print_size(x) printf("%ld\n", sizeof(x))
#define print_byte_array(A, n) do {for (int _ = 0; _ < (n); _++) printf("%02x ", (A)[_]); putchar(10);} while (0)

union position {
    struct {
        float x;
        float y;
        float z;
    };
    u_char bin[sizeof(float) * 3];
};

u_char Buffer_T_Terminal[Num_Terminal][64];

int main(void) {
    printf("%d %d\n", Num_Terminal, Num_Transpoder);
    printf("%ld\n", sizeof Buffer_T_Terminal);

    Buffer_T_Terminal[0][0] = 0xff;
    Buffer_T_Terminal[0][1] = 0x12;
    Buffer_T_Terminal[0][2] = 0x34;
    Buffer_T_Terminal[0][3] = 0x56;

    print_byte_array(Buffer_T_Terminal[0], 4);

    union position p;
    print_size(p);

    return 0;
}
