# Compile C Variants Python

#### You:
Here is a configurable C program representing 3 possible variants:
#include <stdio.h>

// Define the type to use as an alias
#ifdef USE_DOUBLE
    typedef double real;
#elif defined(USE_FLOAT)
    typedef float real;
#else
    typedef long double real;
#endif

int main() {
    // Declare and initialize variables
    real x = 1.0;
    real y = 0x1p-53 + 0x1p-64;
    real z = x + y;

    // Print the value of z
    #ifdef USE_DOUBLE
        printf("z (using double) = %a\n", z);
    #elif defined(USE_FLOAT)
        printf("z (using float) = %a\n", z);
    #else
        printf("z (using long double) = %La\n", z);
    #endif

    return 0;
}
Write a Python script that compiles/executes the three variants above, with and without the -mfpmath=387 of gcc... Compile also with clang. Synthesize all results in a CSV containing the configuration (flag, with or without -mfpmath=387, compiler) and the different outputs

#### ChatGPT:
To execute the given C program with different configurations, you can use the Python `subprocess` module to compile and run the code with different options. Here's a Python script that does that:

```python
import subprocess
import csv

# C program source code
c_code = '''
#include <stdio.h>

// Define the type to use as an alias
#ifdef USE_DOUBLE
    typedef double real;
#elif defined(USE_FLOAT)
    typedef float real;
#else
    typedef long double real;
#endif

int main() {
    // Declare and initialize variables
    real x = 1.0;
    real y = 0x1p-53 + 0x1p-64;
    real z = x + y;

    // Print the value of z
    #ifdef USE_DOUBLE
        printf("z (using double) = %a\\n", z);
    #elif defined(USE_FLOAT)
        printf("z (using float) = %a\\n", z);
    #else
        printf("z (using long double) = %La\\n", z);
    #endif

    return 0;
}
'''

# Create a temporary C file
with open('temp.c', 'w') as f:
    f.write(c_code)

# Compile and run configurations
compilers = ['gcc', 'clang']
flag_options = ['', '-mfpmath=387']
type_options = ['USE_DOUBLE', 'USE_FLOAT', '']

csv_data = [['flag', 'mfpmath', 'compiler', 'output']]

for compiler in compilers:
    for flag in type_options:
        for mfpmath in flag_options:
            compile_cmd = f"{compiler} -o temp {'' if mfpmath == '' else '-mfpmath=387'} {'-D' + flag if flag != '' else ''} temp.c"
            run_cmd = "./temp"

            # Compile the C program with the specific configuration
            subprocess.run(compile_cmd, shell=True, check=True)

            # Run the compiled program and capture the output
            result = subprocess.run(run_cmd, shell=True, check=True, capture_output=True, text=True)

            # Append the result to the csv_data
            csv_data.append([flag, mfpmath, compiler, result.stdout.strip()])

# Remove the temporary C file and executable
subprocess.run("rm temp.c temp", shell=True, check=True)

# Write the results to a CSV file
with open('results.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(csv_data)

print("Results saved in results.csv")
```

This script will compile and run the provided C program with different configurations (gcc/clang, with/without -mfpmath=387, and the three type options), capture the output, and save the results in a CSV file named `results.csv`.
