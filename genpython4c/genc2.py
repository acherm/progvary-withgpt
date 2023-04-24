import subprocess
import csv

c_program = r'''
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
'''

with open('variants.c', 'w') as f:
    f.write(c_program)

configs = [
    ('USE_DOUBLE', 'gcc', '-mfpmath=387'),
    ('USE_DOUBLE', 'gcc', ''),
    ('USE_FLOAT', 'gcc', '-mfpmath=387'),
    ('USE_FLOAT', 'gcc', ''),
    ('USE_LONG_DOUBLE', 'gcc', '-mfpmath=387'),
    ('USE_LONG_DOUBLE', 'gcc', ''),
    ('USE_DOUBLE', 'clang', ''),
    ('USE_FLOAT', 'clang', ''),
    ('USE_LONG_DOUBLE', 'clang', ''),
]

results = []

for config in configs:
    flag, compiler, mfpmath = config
    if compiler == 'clang' and mfpmath == '-mfpmath=387':
        continue
    cmd_compile = f'{compiler} -o variants {mfpmath} -D{flag} variants.c'
    cmd_run = './variants'
    subprocess.run(cmd_compile.split())
    output = subprocess.check_output(cmd_run.split()).decode('utf-8').strip()
    results.append((flag, mfpmath, compiler, output))

with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['flag', 'mfpmath', 'compiler', 'output']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        writer.writerow({'flag': result[0], 'mfpmath': result[1], 'compiler': result[2], 'output': result[3]})
