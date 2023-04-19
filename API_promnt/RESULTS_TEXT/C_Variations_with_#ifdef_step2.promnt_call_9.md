
You can use the following Python script to compile and execute the three variants, with and without the `-mfpmath=387` flag, using the GNU Compiler Collection (GCC) and the Clang C compiler:

```python
import subprocess

# Define the compiler commands
gcc_cmd = "gcc -o {0} {1} -mfpmath=387"
clang_cmd = "clang -o {0} {1}"

# Define the commands to execute the programs
exec_cmd = "./{0}"

# List of flags to use
flags = ["", "-DUSE_DOUBLE", "-DUSE_FLOAT"]

# Output CSV file
output_file = "results.csv"

# Initialize the results list
results = []

# Iterate through the flags
for flag in flags:
    # Compile the program for GCC with -mfpmath=387
    gcc_out1 = subprocess.run([gcc_cmd.format("gcc_out1", flag), ""],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    exec_out1 = subprocess.run([exec_cmd.format("gcc_out1"), ""],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    results.append([flag, "yes", "gcc", exec_out1.stdout.decode("utf-8")])

    # Compile the program for GCC without -mfpmath=387
    gcc_out2 = subprocess.run([gcc_cmd.format("gcc_out2", flag), ""],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    exec_out2 = subprocess.run([exec_cmd.format("gcc_out2"), ""],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    results.append([flag, "no", "gcc", exec_out2.stdout.decode("utf-8")])

    # Compile the program
