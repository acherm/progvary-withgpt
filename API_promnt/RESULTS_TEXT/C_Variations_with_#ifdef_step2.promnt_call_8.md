
Here is an example Python script that can compile and execute the three variants of the program above with and without the -mfpmath=387 flag of GCC and with Clang:

```py
import subprocess
import csv

# Define the commands to be executed
cmds = [
    ["gcc -o original main.c", "./original"],
    ["gcc -DUSE_DOUBLE -o double_variation main.c", "./double_variation"],
    ["gcc -DUSE_FLOAT -o float_variation main.c", "./float_variation"],
    ["gcc -mfpmath=387 -o original_387 main.c", "./original_387"],
    ["gcc -mfpmath=387 -DUSE_DOUBLE -o double_variation_387 main.c", "./double_variation_387"],
    ["gcc -mfpmath=387 -DUSE_FLOAT -o float_variation_387 main.c", "./float_variation_387"],
    ["clang -o original_clang main.c", "./original_clang"],
    ["clang -DUSE_DOUBLE -o double_variation_clang main.c", "./double_variation_clang"],
    ["clang -DUSE_FLOAT -o float_variation_clang main.c", "./float_variation_clang"]
]

# Create a CSV to store the results
with open('variants_results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Configuration', 'Output'])

    # Execute the commands and save the results
    for cmd in cmds:
        # Compile the program
        output = subprocess.run(cmd[0], shell=True, capture_output=True)

        # Execute the program and save the output
        if output.returncode == 0:
            output = subprocess.run(cmd[1], shell=True, capture_output=True)

