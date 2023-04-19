
#include <stdio.h>
#if defined VARIATION1
    typedef double xyz_type;
#elif defined VARIATION2
    typedef float xyz_type;
#endif

int main() {
    // Declare and initialize variables
    xyz_type x = 1.0;
    xyz_type y = 0x1p-53 + 0x1p-64;
    xyz_type z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}
