
//Variation 1: Replace long double with double
#include <stdio.h>
#ifndef VARIATION
#define VARIATION 1
#endif

int main() {
    // Declare and initialize variables
#if VARIATION == 1
    double x = 1.0;
    double y = 0x1p-53 + 0x1p-64;
    double z = x + y;
#endif

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}

//Variation 2: Replace long double with float
#include <stdio.h>
#ifndef VARIATION
#define VARIATION 2
#endif

int main() {
    // Declare and initialize variables
#if VARIATION == 2
    float x = 1.0;
    float y = 0x1p-53 + 0x1p-64;
    float z = x + y;
#endif

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}
