
#include <stdio.h>
#ifdef DOUBLE
    typedef double datatype;
#elif FLOAT
    typedef float datatype;
#else
    typedef long double datatype;
#endif

int main() {
    // Declare and initialize variables
    datatype x = 1.0;
    datatype y = 0x1p-53 + 0x1p-64;
    datatype z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
}
