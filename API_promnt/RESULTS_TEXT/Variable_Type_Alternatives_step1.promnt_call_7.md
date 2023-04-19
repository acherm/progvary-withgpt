.

To create these variations, you can use the preprocessor directive #ifdef:

#include <stdio.h>

#ifdef USE_DOUBLE
    typedef double number_type;
#elif USE_FLOAT
    typedef float number_type;
#else
    typedef long double number_type;
#endif

int main() {
    // Declare and initialize variables
    number_type x = 1.0;
    number_type y = 0x1p-53 + 0x1p-64;
    number_type z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}

To use the program with double, compile with the following command:

$ gcc -DUSE_DOUBLE main.c

To use the program with float, compile with the following command:

$ gcc -DUSE_FLOAT main.c

To use the program with long double, compile with the following command:

$ gcc main.c
