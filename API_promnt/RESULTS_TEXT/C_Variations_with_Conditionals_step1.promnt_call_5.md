
#include <stdio.h>

// First Variation
#ifdef VARIATION1
    double x = 1.0;
    double y = 0x1p-53 + 0x1p-64;
    double z = x + y;
#endif

// Second Variation
#ifdef VARIATION2
    float x = 1.0;
    float y = 0x1p-53 + 0x1p-64;
    float z = x + y;
#endif

int main() {

    #ifdef VARIATION1
        printf("z (Variation1) = %a\n", z);
    #endif

    #ifdef VARIATION2
        printf("z (Variation2) = %a\n", z);
    #endif

    return 0;
}
