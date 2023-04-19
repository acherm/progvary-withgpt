
#include <stdio.h>
#ifdef USE_DOUBLE
    typedef double x_type;
#elif defined(USE_FLOAT)
    typedef float x_type;
#else
    typedef long double x_type;
#endif

int main() {
    // Declare and initialize variables
    x_type x = 1.0;
    x_type y = 0x1p-53 + 0x1p-64;
    x_type z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}
