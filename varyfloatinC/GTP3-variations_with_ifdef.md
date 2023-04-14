# C Variations with #ifdef

#### You:
I have the following program:
#include <stdio.h>

int main() {
    // Declare and initialize variables
    long double x = 1.0;
    long double y = 0x1p-53 + 0x1p-64;
    long double z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
} and I'd like to create variations over this program using conditional compilation and #ifdef cpp directives... specifically, I'd like to create a first variation that consists in replacing the type long double by double... and another alternative variation that consists in replacing long double by float...

#### GPT3:
// Version using double
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

// Version using float
#ifdef FLOAT
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

