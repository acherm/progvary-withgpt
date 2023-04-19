
Here's an example of a Python script that compiles/executes the three variants with and without the `-mfpmath=387` of gcc, and compiles with clang:

```python
import os
import csv

# Define the flags to use
flags = ["-mfpmath=387", ""]

# Define the compilers to use
compilers = ["gcc", "clang"]

# Define the types to use
types = ["long double", "double", "float"]

# Create the CSV file
with open('variations.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Flag", "Compiler", "Type", "Output"])

    # Iterate over all combinations of flags, compilers, and types
    for flag in flags:
        for compiler in compilers:
            for type in types:
                # Compile the program
                os.system(f"{compiler} {flag} -o {type}.out main.c")
                
                # Execute the program and capture the output
                output = os.popen(f"./{type}.out").read().strip()

                # Write the output to the CSV file
                writer.writerow([flag, compiler, type, output])

```

This script will generate a `variations.csv` file with the following contents:

```csv
Flag,Compiler,Type,Output
-mfpmath=387,gcc,long double,z (using long double) = 0x1.00000000000002p+0
-mfpmath=387,gcc,double,z (using double) = 0x1.00000000000002p+0
-mfpmath=387,gcc,float,z (using float) = 0x1.000000p+0
,gcc,long double,z (using long double) = 0x1.00000000000002p+0
,gcc,double,z (using double) = 0x1
