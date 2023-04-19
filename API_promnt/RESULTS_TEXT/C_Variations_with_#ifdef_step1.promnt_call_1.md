

#include <stdio.h>

#ifdef USE_DOUBLE
    typedef double REAL;
#elif defined USE_FLOAT
    typedef float REAL;
#else
    typedef long double REAL;
#endif

int main() {
    // Declare and initialize variables
    REAL x = 1.0;
    REAL y = 0x1p-53 + 0x1p-64;
    REAL z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}
