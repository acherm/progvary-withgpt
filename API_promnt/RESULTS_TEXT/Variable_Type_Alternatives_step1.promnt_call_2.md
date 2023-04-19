.

In order to achieve this, I can use conditional compilation. In this case, I would use the preprocessor directives #ifdef, #else, and #endif.

#include <stdio.h>

#ifdef USE_DOUBLE
    typedef double number_type;
#else
    #ifdef USE_FLOAT
        typedef float number_type;
    #else
        typedef long double number_type;
    #endif
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
In order to compile the program for double type, I would use the directive #define USE_DOUBLE, and for float type, I would use the directive #define USE_FLOAT. This would allow me to switch between the different types of variables at compile time.
