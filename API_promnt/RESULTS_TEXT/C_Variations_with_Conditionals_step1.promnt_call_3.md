
#ifdef DOUBLE
#include <stdio.h>
int main() {
    // Declare and initialize variables
    double x = 1.0;
    double y = 0x1p-53 + 0x1p-64;
    double z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
} 

#elif FLOAT
#include <stdio.h>
int main() {
    // Declare and initialize variables
    float x = 1.0;
    float y = 0x1p-53 + 0x1p-64;
    float z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
} 

#endif
