.

#include <stdio.h>

// Change type to double
#ifdef DOUBLE
    typedef double type;
#endif

// Change type to float
#ifdef FLOAT
    typedef float type;
#endif

int main() {
    // Declare and initialize variables
    type x = 1.0;
    type y = 0x1p-53 + 0x1p-64;
    type z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}
