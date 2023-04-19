
The following Python script compiles and executes the three variants of the program, with and without the `-mfpmath=387` flag of GCC, as well as with Clang. It stores the configuration (flag, with or without `-mfpmath=387`, compiler) and the outputs in a CSV file.

```python
import subprocess

# Define the flags to be used
flags = ["-mfpmath=387", ""]

# Define the compilers to be used
compilers = ["gcc", "clang"]

# Open and prepare the CSV file
f = open("results.csv", "w")
f.write("Flag,Use_mfpmath,Compiler,Output\n")

# Loop through the flags and compilers
for flag in flags:
    for compiler in compilers:
        # Compile the program with the given flag and compiler
        command = "{} {} -o main main.c".format(compiler, flag)
        subprocess.run(command, shell=True)

        # Execute the program
        output = subprocess.check_output("./main", shell=True).decode('utf-8').strip()

        # Write the configuration and output to the CSV file
        f.write("{},{},{},{}\n".format(flag, flag != "", compiler, output))

# Close the CSV file
f.close()
```
