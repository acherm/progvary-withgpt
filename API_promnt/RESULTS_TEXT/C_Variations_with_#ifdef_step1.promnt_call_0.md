

#include <stdio.h>

#ifdef FLOAT_VARIATION
    typedef float my_type;
#elif DOUBLE_VARIATION
    typedef double my_type;
#else
    typedef long double my_type;
#endif

int main() {
    // Declare and initialize variables
    my_type x = 1.0;
    my_type y = 0x1p-53 + 0x1p-64;
    my_type z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}
