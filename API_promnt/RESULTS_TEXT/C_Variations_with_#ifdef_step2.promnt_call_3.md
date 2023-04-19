
Here's an example Python script that can compile and execute the three variants of the program:

```python
import subprocess

# Declare the flags to use
flags = ["", "-mfpmath=387"]

# Declare the compilers to use
compilers = ["gcc", "clang"]

# Declare the file to compile
file = "main.c"

# Create the output CSV file
csv_file = "results.csv"
f = open(csv_file, "w")

# Write the CSV headers
f.write("Flag, mfpmath, Compiler, Output\n")

for flag in flags:
    for compiler in compilers:
        # Compile the file using the given flag and compiler
        output = subprocess.check_output([compiler, flag, file])

        # Execute the compiled program
        output = subprocess.check_output(["./a.out"])

        # Write the output to the CSV file
        f.write(f"{flag}, {mfpmath}, {compiler}, {output}\n")

# Close the CSV file
f.close()
```

This script will compile and execute the program with the specified flags and compilers, and then write the output to a CSV file called `results.csv`.
