# C Configurable Preprocessor Program.

#### You:
Write a configurable program in C language that uses preprocessor annotations for customization. With the annotation #define (C style), we consider four features and their selections, namely, Hello, Beautiful, Wonderful, and World... If the feature is selected, then we print the name of the feature. For instance, we could well print "Hello Beautiful World", "Hello World", "Hello", "World" etc.

#### ChatGPT:
Here's a C program that uses preprocessor annotations for customization based on the selected features:

```c
#include <stdio.h>

// Define features here (uncomment to select)
//#define HELLO
//#define BEAUTIFUL
//#define WONDERFUL
//#define WORLD

int main() {
    #ifdef HELLO
        printf("Hello");
        #if defined BEAUTIFUL || defined WONDERFUL || defined WORLD
            printf(" ");
        #endif
    #endif

    #ifdef BEAUTIFUL
        printf("Beautiful");
        #if defined WONDERFUL || defined WORLD
            printf(" ");
        #endif
    #endif

    #ifdef WONDERFUL
        printf("Wonderful");
        #ifdef WORLD
            printf(" ");
        #endif
    #endif

    #ifdef WORLD
        printf("World");
    #endif

    printf("\n");
    return 0;
}
```

To customize the output, uncomment the desired features by removing the '//' before the corresponding #define lines. The program will print the selected feature names in the order they are defined. For example, to print "Hello Beautiful World", uncomment the lines for HELLO, BEAUTIFUL, and WORLD. To print "Hello World", uncomment the lines for HELLO and WORLD.


#### You:
can you use another style for writing CPP instructions and consider this style:
first set a value to feature (true or false) eg #define Hello true
then using #if 

#### ChatGPT:
Sure, here's the modified C program that sets a boolean value (true or false) for each feature using preprocessor annotations:

```c
#include <stdio.h>

// Define features here (set to true or false)
#define HELLO true
#define BEAUTIFUL false
#define WONDERFUL false
#define WORLD true

int main() {
    #if HELLO
        printf("Hello");
        #if BEAUTIFUL || WONDERFUL || WORLD
            printf(" ");
        #endif
    #endif

    #if BEAUTIFUL
        printf("Beautiful");
        #if WONDERFUL || WORLD
            printf(" ");
        #endif
    #endif

    #if WONDERFUL
        printf("Wonderful");
        #if WORLD
            printf(" ");
        #endif
    #endif

    #if WORLD
        printf("World");
    #endif

    printf("\n");
    return 0;
}
```

To customize the output, set the desired features to true or false as needed. The program will print the selected feature names in the order they are defined. For example, to print "Hello Beautiful World", set HELLO, BEAUTIFUL, and WORLD to true. To print "Hello World", set HELLO and WORLD to true and the others to false.
