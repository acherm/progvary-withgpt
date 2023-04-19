

#include <stdio.h>

#ifdef USE_DOUBLE
    typedef double real_t;
#elif defined(USE_FLOAT)
    typedef float real_t;
#else
    typedef long double real_t;
#endif

int main() {
    // Declare and initialize variables
    real_t x = 1.0;
    real_t y = 0x1p-53 + 0x1p-64;
    real_t z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}

To create the first variation with double, compile the program with:

gcc -DUSE_DOUBLE program.c -o program

To create the second variation with float, compile the program with:

gcc -DUSE_FLOAT program.c -o program
