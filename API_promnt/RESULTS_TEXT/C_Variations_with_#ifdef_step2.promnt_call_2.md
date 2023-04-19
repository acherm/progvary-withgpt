
Here is an example of a Python script that compiles and executes the three variants of the program with and without the -mfpmath=387 flag, using both gcc and clang:

```python
import subprocess

# Define the flags to use
flags = ["-mfpmath=387", ""]

# Define the compilers to use
compilers = ["gcc", "clang"]

# Define the types to use
types = ["long double", "double", "float"]

# Create an empty list to store the results
results = []

# Iterate through the combinations of flags, compilers, and types
for flag in flags:
    for compiler in compilers:
        for type in types:
            # Set the output file name
            output_filename = f"{type.lower()}_{compiler}_{flag.replace('=', '')}.txt"

            # Compile the program using the specified compiler and flag
            command = f"{compiler} {flag} -o {output_filename} main.c"
            subprocess.run(command, shell=True)

            # Execute the program
            command = f"./{output_filename}"
            output = subprocess.check_output(command, shell=True).decode()

            # Store the results
            results.append({
                "flag": flag,
                "compiler": compiler,
                "type": type,
                "output": output
            })

# Create a CSV file to store the results
with open('results.csv', 'w') as f:
    # Write the header
    f.write("flag,compiler,type,output\n")

    # Write each result
    for result in results:
        f.write(f"{result['flag']},{result['compiler']},{result['type']},{result['output']}\n")
```
