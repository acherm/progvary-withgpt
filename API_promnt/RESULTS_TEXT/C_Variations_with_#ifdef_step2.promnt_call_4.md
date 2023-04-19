
Here is an example Python script that compiles/executes the three variants of the program with and without the -mfpmath=387 flag and with both GCC and Clang:

```python
import os
import csv

# Variables
flags = ["-DUSE_DOUBLE", "-DUSE_FLOAT", ""]
mfpmath = ["-mfpmath=387", ""]
compilers = ["gcc", "clang"]

# Create a CSV file with the results
with open('results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    # Write the header
    writer.writerow(["Flag", "mfpmath", "Compiler", "Output"])

    # Compile and execute the program for each configuration
    for flag in flags:
        for mfp in mfpmath:
            for compiler in compilers:
                # Compile the program
                os.system(f"{compiler} {mfp} -o program {flag} main.c")

                # Execute the program
                output = os.popen("./program").read().strip()

                # Write the results to the CSV file
                writer.writerow([flag, mfp, compiler, output])
```
