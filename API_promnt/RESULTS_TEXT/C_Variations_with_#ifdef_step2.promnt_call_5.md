
Here's an example of a Python script that compiles and executes the three variants of the program above, with and without the -mfpmath=387 flag of gcc, and with clang:

```python
import subprocess

# Variables to store the results
results = []

# Compile and execute the original version using long double with gcc
p = subprocess.run(
    ["gcc", "-o", "original_gcc", "main.c"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Execute the program and get the output
output = subprocess.run(
    ["./original_gcc"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
).stdout.decode("utf-8")

# Append the results to the list
results.append({
    "flag": "gcc (no flags)",
    "compiler": "gcc",
    "output": output
})

# Compile and execute the original version using long double with gcc
# and the -mfpmath=387 flag
p = subprocess.run(
    ["gcc", "-mfpmath=387", "-o", "original_gcc_387", "main.c"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Execute the program and get the output
output = subprocess.run(
    ["./original_gcc_387"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
).stdout.decode("utf-8")

# Append the results to the list
results.append({
    "flag": "gcc (-mfpmath=387)",
    "compiler": "gcc",
    "output": output
})

# Compile and execute the variation using double with gcc
p = subprocess.run(
    ["gcc", "-DUSE_DOUBLE", "-o", "double_variation_gcc", "main.
