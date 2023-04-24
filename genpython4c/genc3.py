'''
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
Write a Python script that compiles/executes the three variants above, with and without the -mfpmath=387 of gcc... Compile also with clang (without -mfpmath=387 though). Synthesize all results in a CSV containing the configuration (flag, with or without -mfpmath=387, compiler) and the different outputs. 
Please use pandas library for writing the CSV... also the fieldnames of the CSV should be compiler, flags, type, and result.
'''

import os
import subprocess
import pandas as pd

def compile_and_run(compiler, flags, type_define):
    output_file = "main.exe" # review: Windows specific? why for this prompt and not others?
    compile_command = f"{compiler} {flags} -D{type_define} -o {output_file} main.c"
    os.system(compile_command)

    output = subprocess.check_output(output_file).decode("utf-8")
    result = output.split(" = ")[-1].strip()

    return {
        "compiler": compiler,
        "flags": flags,
        "type": type_define,
        "result": result
    }

def main():
    variants = ["USE_DOUBLE", "USE_FLOAT", "USE_LONG_DOUBLE"]
    compilers = [
        {"name": "gcc", "flags": ["-mfpmath=387", ""]},
        {"name": "clang", "flags": [""]}
    ]

    results = []

    for compiler in compilers:
        for flags in compiler["flags"]:
            for variant in variants:
                result = compile_and_run(compiler["name"], flags, variant)
                results.append(result)

    df = pd.DataFrame(results)
    df.to_csv("results.csv", index=False)

if __name__ == "__main__":
    main()
