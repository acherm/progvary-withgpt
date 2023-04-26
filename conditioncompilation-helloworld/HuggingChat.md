Write a configurable program in C++ language that uses preprocessor annotations for customization. With the annotation #define (C style), we consider four features and their selections, namely, Hello, Beautiful, Wonderful, and World... If the feature is selected, then we print the name of the feature. For instance, we could well print "Hello Beautiful World", "Hello World", "Hello", "World" etc.

Sure! Here's an example program in C++ using preprocessor annotations:

#include <iostream>

// Feature selection via preprocessor annotations
#ifdef HELLO_BEAUTIFUL_WORLD
  std::cout << "Hello Beautiful World!" << std::endl;
#elif defined(HELLO)
  std::cout << "Hello!" << std::endl;
#elif defined(WORLD)
  std::cout << "World!" << std::endl;
#else
  // Default behavior if none of the above are defined
  std::cout << "No features selected." << std::endl;
#endif

int main() { return 0; }
To use this program with different feature selections, you can define the appropriate macro before compiling or running the code:

// Define all features
gcc -D HELLO_BEAUTIFUL_WORLD=1 -DCSS=-DHELLO myprogram.cpp
// This will compile and run 'myprogram.cpp', which prints "Hello Beautiful World!"

// Select only some features
gcc -DBEAUTIFUL -DBCSS myprogram.cpp
// This will compile and run 'myprogram.cpp', which prints "Beautiful World!"

// Unselect certain features
gcc myprogram.cpp
// This will compile and run 'myprogram.cpp', which prints "No features selected." by default
