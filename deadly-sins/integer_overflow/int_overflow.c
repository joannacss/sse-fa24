#include <stdio.h>

// Compiling: gcc -w -o int_overflow int_overflow.c
// The -w is to disable the warning (that's intentional)
int main(int argc, char *argv[]){
    // chars range from 0 to 255
    unsigned char a = -1; 
    unsigned char b = 256;
    printf("a=%d\n", a); // what would it print?
    printf("b=%d\n", b); // what would it print?


    // chars range from -128 to 127
    char c = 128; 
    char d = -129;
    printf("c=%d\n", c); // what would it print?
    printf("d=%d\n", d); // what would it print?

    printf("%d", sizeof(unsigned char));
    return 0;
}