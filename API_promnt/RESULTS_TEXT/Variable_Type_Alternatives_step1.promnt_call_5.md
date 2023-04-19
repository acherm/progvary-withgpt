.

#include <stdio.h>
#ifdef DOUBLE
    typedef double number_t;
#elif FLOAT
    typedef float number_t;
#else
    typedef long double number_t;
#endif

int main() {
    // Declare and initialize variables
    number_t x = 1.0;
    number_t y = 0x1p-53 + 0x1p-64;
    number_t z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
} 
To compile with double, type the command:

gcc program.c -DDOUBLE
