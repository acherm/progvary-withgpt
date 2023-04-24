# GCC Clang C compilation.

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
Write a Python script that compiles/executes the three variants above, with and without the -mfpmath=387 of gcc... Compile also with clang (without -mfpmath=387 though). Synthesize all results in a CSV containing the configuration (flag, with or without -mfpmath=387, compiler) and the different outputs. Please use pandas library for writing the CSV... also the fieldnames of the CSV should be compiler, flags, type, and result.

#### ChatGPT:
Here's a Python script that compiles and executes the three variants of the C program using both GCC and Clang, with and without the `-mfpmath=387` flag. The script then synthesizes the results into a CSV file using the pandas library.

First, save the C code in a file named `main.c`.

```python
import os
import subprocess
import pandas as pd

def compile_and_run(compiler, flags, type_define):
    output_file = "main.exe"
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
```

This script creates a CSV file named `results.csv` containing the results for each configuration. The CSV will have the following columns: "compiler", "flags", "type", and "result".


#### You:
  File "/home/mathieuacher/cursor-tutor/genpython4c/genc3.py", line 67, in main
    result = compile_and_run(compiler["name"], flags, variant)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mathieuacher/cursor-tutor/genpython4c/genc3.py", line 45, in compile_and_run
    output = subprocess.check_output(output_file).decode("utf-8")
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/subprocess.py", line 466, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/subprocess.py", line 548, in run
    with Popen(*popenargs, **kwargs) as process:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/subprocess.py", line 1024, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/lib64/python3.11/subprocess.py", line 1901, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'main'

#### ChatGPT:
I apologize for the confusion. It seems like the script is unable to find the `main` executable after compilation. This could be due to a couple of reasons. Let's update the script to ensure the correct working directory and make the executable file compatible across different platforms.

```python
import os
import subprocess
import pandas as pd
import platform

def compile_and_run(compiler, flags, type_define):
    output_file = "main.exe" if platform.system() == "Windows" else "./main.out"
    compile_command = f"{compiler} {flags} -D{type_define} -o {output_file} main.c"
    os.system(compile_command)

    output = subprocess.check_output(output_file, shell=True).decode("utf-8")
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
```

This updated script should work correctly. If the issue persists, please let me know.
