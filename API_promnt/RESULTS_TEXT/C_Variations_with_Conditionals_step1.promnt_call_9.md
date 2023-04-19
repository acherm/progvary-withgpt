
#include <stdio.h>
#ifdef VAR1
double x = 1.0;
double y = 0x1p-53 + 0x1p-64;
double z = x + y;
#elif VAR2
float x = 1.0;
float y = 0x1p-53 + 0x1p-64;
float z = x + y;
#endif

// Print the value of z
printf("z = %a\n", z);

return 0;
