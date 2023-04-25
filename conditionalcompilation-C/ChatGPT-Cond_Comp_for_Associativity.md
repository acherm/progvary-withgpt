# Cond Comp for Associativity

#### You:
I have the following C function: 
int associativity_test()
{
  double x = uniform; double y = uniform; double z = uniform;
  return x+(y+z) == (x+y)+z;
}
I'd like to create two variants of associativity_test: one with the following relation, called inverse multiplication, (x * z) / (y * z) == x / y ; another with the relation (x * z * math.pi) / (y * z * math.pi) == (x / y) called the inverse multiplication with pi. Show me only the code of associativity_test using conditional compilation

#### ChatGPT:
You can use conditional compilation with preprocessor directives in C to create the two variants of `associativity_test`. Here's an example with `ASSOCIATIVITY_TYPE` as the conditional variable:

```c
#include <math.h>
#include <stdbool.h>

// Use this define to change the associativity test type
// #define ASSOCIATIVITY_TYPE 1 // for inverse multiplication
// #define ASSOCIATIVITY_TYPE 2 // for inverse multiplication with pi

int associativity_test()
{
    double x = uniform; double y = uniform; double z = uniform;

    #if ASSOCIATIVITY_TYPE == 1
        bool result = (x * z) / (y * z) == x / y;
    #elif ASSOCIATIVITY_TYPE == 2
        bool result = (x * z * M_PI) / (y * z * M_PI) == x / y;
    #else
        #error "Invalid ASSOCIATIVITY_TYPE value"
    #endif

    return result;
}
```

To use the first variant (inverse multiplication), uncomment the line `#define ASSOCIATIVITY_TYPE 1`. To use the second variant (inverse multiplication with pi), uncomment the line `#define ASSOCIATIVITY_TYPE 2`.

Keep in mind that this code assumes the `uniform` values are already provided. If you want to generate random numbers, you can use the `rand()` function in C combined with a scaling factor to get values between 0 and 1.


#### You:
please allows the possibility to have the x+(y+z) == (x+y)+z; relation 

#### ChatGPT:
Sure, you can add the original relation to the conditional compilation. I've added it as an option with `ASSOCIATIVITY_TYPE` set to 0:

```c
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

// Use this define to change the associativity test type
// #define ASSOCIATIVITY_TYPE 0 // for x+(y+z) == (x+y)+z
// #define ASSOCIATIVITY_TYPE 1 // for inverse multiplication
// #define ASSOCIATIVITY_TYPE 2 // for inverse multiplication with pi

double uniform_random() {
    return (double)rand() / (double)RAND_MAX;
}

int associativity_test()
{
    double x = uniform_random(); double y = uniform_random(); double z = uniform_random();
    bool result;

    #if ASSOCIATIVITY_TYPE == 0
        result = x + (y + z) == (x + y) + z;
    #elif ASSOCIATIVITY_TYPE == 1
        result = (x * z) / (y * z) == x / y;
    #elif ASSOCIATIVITY_TYPE == 2
        result = (x * z * M_PI) / (y * z * M_PI) == x / y;
    #else
        #error "Invalid ASSOCIATIVITY_TYPE value"
    #endif

    return result;
}
```

To use the original relation (x+(y+z) == (x+y)+z), uncomment the line `#define ASSOCIATIVITY_TYPE 0`.

Don't forget to call `srand(time(NULL));` once in your `main` function before calling `associativity_test()` to seed the random number generator.


#### You:
ok, now provide an implementation of associativity_test() and supporting the three relations, but this time using a parameter and without conditional compilation

#### ChatGPT:
Here's an implementation of `associativity_test()` that takes an integer parameter `associativity_type` to determine which relation to test:

```c
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

// The three different associativity tests
#define ASSOCIATIVITY_TYPE_ADDITION 0
#define ASSOCIATIVITY_TYPE_INVERSE_MULT 1
#define ASSOCIATIVITY_TYPE_INVERSE_MULT_PI 2

double uniform_random() {
    return (double)rand() / (double)RAND_MAX;
}

int associativity_test(int associativity_type)
{
    double x = uniform_random(); double y = uniform_random(); double z = uniform_random();
    bool result;

    switch (associativity_type) {
        case ASSOCIATIVITY_TYPE_ADDITION:
            result = x + (y + z) == (x + y) + z;
            break;
        case ASSOCIATIVITY_TYPE_INVERSE_MULT:
            result = (x * z) / (y * z) == x / y;
            break;
        case ASSOCIATIVITY_TYPE_INVERSE_MULT_PI:
            result = (x * z * M_PI) / (y * z * M_PI) == x / y;
            break;
        default:
            // Return an error value or handle the invalid parameter in some way
            return -1;
    }

    return result;
}

int main() {
    srand(time(NULL));

    int result = associativity_test(ASSOCIATIVITY_TYPE_ADDITION);
    // ... do something with the result

    return 0;
}
```

The `associativity_test()` function now takes a parameter `associativity_type` which can be one of the defined constants `ASSOCIATIVITY_TYPE_ADDITION`, `ASSOCIATIVITY_TYPE_INVERSE_MULT`, or `ASSOCIATIVITY_TYPE_INVERSE_MULT_PI`. The function uses a `switch` statement to handle the different test cases.
