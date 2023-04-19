
Here is an example of a Python script that compiles/executes the three variants above, with and without the -mfpmath=387 flag:

```python
import subprocess

# Define the compiler and flags to use 
compiler = ["gcc", "clang"]
flags = ["", "-mfpmath=387"]
variations = ["original", "double_variation", "float_variation"] 

# Create a CSV file to store the results
csv_file = open("results.csv", "w")
csv_file.write("configuration,output\n")

# Compile and execute the program with different compilers and flags
for c in compiler:
    for f in flags:
        for v in variations:
            # Compile the program
            subprocess.run([c, f, "-o", v, v+".c"])
            # Execute the program and capture the output
            output = subprocess.run(["./"+v], capture_output=True).stdout.decode("utf-8").strip()
            # Write the configuration and output to the CSV
            csv_file.write("{},{}\n".format(c+" "+f+" "+v, output))

# Close the CSV file
csv_file.close()
```
