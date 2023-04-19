

#include <stdio.h>

#ifdef FIRST_VARIATION
    typedef double num_type;
#elif SECOND_VARIATION
    typedef float num_type;
#else
    typedef long double num_type;
#endif

int main() {
    // Declare and initialize variables
    num_type x = 1.0;
    num_type y = 0x1p-53 + 0x1p-64;
    num_type z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}
