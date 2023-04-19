
// Variation 1 - Replace type long double with double
#include <stdio.h>
#ifdef VARIATION_1
    #define TYPE double
#else
    #define TYPE long double
#endif
int main() {
    // Declare and initialize variables
    TYPE x = 1.0;
    TYPE y = 0x1p-53 + 0x1p-64;
    TYPE z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}

// Variation 2 - Replace type long double with float
#include <stdio.h>
#ifdef VARIATION_2
    #define TYPE float
#else
    #define TYPE long double
#endif
int main() {
    // Declare and initialize variables
    TYPE x = 1.0;
    TYPE y = 0x1p-53 + 0x1p-64;
    TYPE z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}
