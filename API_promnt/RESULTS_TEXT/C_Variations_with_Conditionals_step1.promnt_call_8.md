
#include <stdio.h>

#ifdef DOUBLE
    typedef double myType;
#elif FLOAT
    typedef float myType;
#else
    typedef long double myType;
#endif

int main() {
    // Declare and initialize variables
    myType x = 1.0;
    myType y = 0x1p-53 + 0x1p-64;
    myType z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}
