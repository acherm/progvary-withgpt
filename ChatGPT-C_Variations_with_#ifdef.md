# C Variations with #ifdef

#### You:
I have the following program #include <stdio.h>



int main() {
    // Declare and initialize variables
    long double x = 1.0;
    long double y = 0x1p-53 + 0x1p-64;
    long double z = x + y;

    // Print the value of z
    printf("z = %a\n", z);

    return 0;
} and I'd like to create variations over this program using conditional compilation and #ifdef cpp directives... specifically, I'd like to create a first variation that consists in replacing the type long double by double... and another alternative variation that consists in replacing long double by float

#### ChatGPT:
You can use the preprocessor directives `#ifdef`, `#elif`, and `#endif` to create conditional compilation. Here's an example that shows how to create the variations you mentioned:

```c
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
```

To compile and run the different variations, you can use the following commands:

1. For the original version using `long double`:

```
gcc -o original main.c
./original
```

2. For the variation using `double`:

```
gcc -DUSE_DOUBLE -o double_variation main.c
./double_variation
```

3. For the variation using `float`:

```
gcc -DUSE_FLOAT -o float_variation main.c
./float_variation
```

These commands will compile and run the different variations of the program according to the defined type.


#### You:
write a Python script that compiles/executes the three variants above, with and without the -mfpmath=387 of gcc... Compile also with clang. Synthesize all results in a CSV containing the configuration (flag, with or without -mfpmath=387, compiler) and the different outputs

#### ChatGPT:
You can use Python's `subprocess` module to run shell commands and compile/execute the three variants of the C program with different configurations. Here's a script to accomplish this:

```python
import subprocess
import csv

def compile_and_run(compiler, flags):
    commands = [
        f"{compiler} {flags} -o original main.c",
        f"{compiler} {flags} -DUSE_DOUBLE -o double_variation main.c",
        f"{compiler} {flags} -DUSE_FLOAT -o float_variation main.c",
    ]

    results = []
    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)

        binary = cmd.split()[-1]
        output = subprocess.check_output(f'./{binary}', shell=True).decode().strip()
        results.append(output)

    return results

def main():
    configurations = [
        ('gcc', ''),
        ('gcc', '-mfpmath=387'),
        ('clang', ''),
    ]

    with open('results.csv', 'w', newline='') as csvfile:
        fieldnames = ['compiler', 'flags', 'original', 'double', 'float']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for compiler, flags in configurations:
            results = compile_and_run(compiler, flags)
            writer.writerow({
                'compiler': compiler,
                'flags': flags,
                'original': results[0],
                'double': results[1],
                'float': results[2],
            })

if __name__ == '__main__':
    main()
```

This script will compile and run the three variants of the C program with the specified configurations and write the results to a CSV file named `results.csv`.

Make sure the `main.c` file containing the C code is in the same directory as the Python script. Then run the Python script:

```sh
python3 compile_and_run.py
```

You can then open the `results.csv` file to see the results in the specified format.


#### You:
please use pandas for writing the CSV... also the fieldnames should be compiler, flags, type, and result. The C file to compile is assoc.c

#### ChatGPT:
Here's the updated Python script using `pandas` to write the CSV and the updated fieldnames. Also, it now assumes the C file to compile is named `assoc.c`:

```python
import subprocess
import pandas as pd

def compile_and_run(compiler, flags):
    commands = [
        f"{compiler} {flags} -o original assoc.c",
        f"{compiler} {flags} -DUSE_DOUBLE -o double_variation assoc.c",
        f"{compiler} {flags} -DUSE_FLOAT -o float_variation assoc.c",
    ]

    results = []
    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)

        binary = cmd.split()[-1]
        output = subprocess.check_output(f'./{binary}', shell=True).decode().strip()
        results.append(output)

    return results

def main():
    configurations = [
        ('gcc', ''),
        ('gcc', '-mfpmath=387'),
        ('clang', ''),
    ]

    data = []

    for compiler, flags in configurations:
        results = compile_and_run(compiler, flags)
        data.extend([
            {'compiler': compiler, 'flags': flags, 'type': 'original', 'result': results[0]},
            {'compiler': compiler, 'flags': flags, 'type': 'double', 'result': results[1]},
            {'compiler': compiler, 'flags': flags, 'type': 'float', 'result': results[2]},
        ])

    df = pd.DataFrame(data)
    df.to_csv('results.csv', index=False)

if __name__ == '__main__':
    main()
```

Make sure the `assoc.c` file containing the C code is in the same directory as the Python script. Then run the Python script:

```sh
python3 compile_and_run.py
```

You can then open the `results.csv` file to see the results in the specified format.


#### You:
can you think about gcc flags or clang flags that could be combined/used and have an influence on floating point operations? Please implement them in the Python code. Note: I've made a mistake, it's not assoc.c, it's approx.c

#### ChatGPT:
Certainly! Here's a list of additional flags that could influence floating-point operations:

1. `-ffast-math`: This flag enables aggressive optimizations that can produce faster code but may not strictly adhere to the IEEE 754 standard for floating-point arithmetic.
2. `-fno-signed-zeros`: This flag allows the compiler to assume that signed zeros (+0 and -0) are not distinguishable and can be treated as the same value.
3. `-fno-trapping-math`: This flag tells the compiler to assume that floating-point operations do not generate user-visible traps.
4. `-fno-rounding-math`: This flag allows the compiler to assume that floating-point rounding is not observable.

Here's the updated Python script with additional flag combinations and the corrected filename `approx.c`:

```python
import subprocess
import pandas as pd

def compile_and_run(compiler, flags):
    commands = [
        f"{compiler} {flags} -o original approx.c",
        f"{compiler} {flags} -DUSE_DOUBLE -o double_variation approx.c",
        f"{compiler} {flags} -DUSE_FLOAT -o float_variation approx.c",
    ]

    results = []
    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)

        binary = cmd.split()[-1]
        output = subprocess.check_output(f'./{binary}', shell=True).decode().strip()
        results.append(output)

    return results

def main():
    configurations = [
        ('gcc', ''),
        ('gcc', '-mfpmath=387'),
        ('gcc', '-ffast-math'),
        ('gcc', '-fno-signed-zeros'),
        ('gcc', '-fno-trapping-math'),
        ('gcc', '-fno-rounding-math'),
        ('clang', ''),
        ('clang', '-ffast-math'),
        ('clang', '-fno-signed-zeros'),
        ('clang', '-fno-trapping-math'),
        ('clang', '-fno-rounding-math'),
    ]

    data = []

    for compiler, flags in configurations:
        results = compile_and_run(compiler, flags)
        data.extend([
            {'compiler': compiler, 'flags': flags, 'type': 'original', 'result': results[0]},
            {'compiler': compiler, 'flags': flags, 'type': 'double', 'result': results[1]},
            {'compiler': compiler, 'flags': flags, 'type': 'float', 'result': results[2]},
        ])

    df = pd.DataFrame(data)
    df.to_csv('results.csv', index=False)

if __name__ == '__main__':
    main()
```

Make sure the `approx.c` file containing the C code is in the same directory as the Python script. Then run the Python script:

```sh
python3 compile_and_run.py
```

You can then open the `results.csv` file to see the results in the specified format.
