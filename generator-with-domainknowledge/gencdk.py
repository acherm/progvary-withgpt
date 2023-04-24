import subprocess
import csv

# C program code
c_program = '''
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

# Save the C program to a file
with open('floating_point_variants.c', 'w') as f:
    f.write(c_program)

# Compiler configurations
# compilers = [
#    ('gcc', '-mfpmath=387'),
#    ('gcc', ''),
#    ('clang', ''),
# ]

# Compiler configurations
compilers = [
    ('gcc', '-mfpmath=387'),
    ('gcc', ''),
    ('gcc', '-ffast-math'),
    ('gcc', '-fno-finite-math-only'),
    ('gcc', '-frounding-math'),
    ('gcc', '-funsafe-math-optimizations'),
    ('gcc', '-ffp-contract=fast'),
    ('gcc', '-ffp-contract=off'),
    ('clang', ''),
    ('clang', '-ffast-math'),
    ('clang', '-fno-finite-math-only'),
    ('clang', '-frounding-math'),
    ('clang', '-funsafe-math-optimizations'),
    ('clang', '-ffp-contract=fast'),
    ('clang', '-ffp-contract=off'),
]


# Type configurations
types = [
    ('USE_DOUBLE', 'double'),
    ('USE_FLOAT', 'float'),
    ('', 'long double'),
]

# Test each configuration and store the results
results = []

for compiler, compiler_flag in compilers:
    for type_flag, type_name in types:
        # Compile the C program
        compile_command = f"{compiler} -o floating_point_variants {compiler_flag} {'-D' + type_flag if type_flag else ''} floating_point_variants.c"
        subprocess.run(compile_command, shell=True, check=True)

        # Execute the compiled program
        execute_command = "./floating_point_variants"
        output = subprocess.check_output(execute_command, shell=True).decode().strip()

        # Add the result to the list
        results.append({
            'compiler': compiler,
            'compiler_flag': compiler_flag,
            'type_flag': type_flag,
            'type_name': type_name,
            'output': output,
        })

# Write the results to a CSV file
with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['compiler', 'compiler_flag', 'type_flag', 'type_name', 'output']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for result in results:
        writer.writerow(result)

print("Results saved to 'results.csv'")
