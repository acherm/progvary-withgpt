
The float variant works in the same way as the double variant. The only difference is that the macro FLOAT is defined instead of the macro DOUBLE, and the typedef statement defines the type myfloat as float instead of double. When the macro FLOAT is defined, the program will use float instead of long double for the variables. Otherwise, the program will use long double.
