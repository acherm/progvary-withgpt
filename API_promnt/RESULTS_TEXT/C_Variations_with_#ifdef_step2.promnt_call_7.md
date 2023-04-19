
Here is an example Python script that can be used to compile and execute the three variants of the program with and without the `-mfpmath=387` flag and using both GCC and Clang compilers:

```python
import subprocess
import csv

variations = [
    ("original", "gcc"),
    ("original", "clang"),
    ("double", "gcc"),
    ("double", "clang"),
    ("float", "gcc"),
    ("float", "clang"),
]

flags = ["", "-mfpmath=387"]

# Create CSV file
with open("output.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(["configuration", "output"])

    # Compile and execute each variation
    for variation, compiler in variations:
        for flag in flags:
            # Compile the program
            cmd = [
                compiler,
                flag,
                "-o",
                variation + "_" + compiler + "_" + flag.replace("=", "_"),
                "main.c",
            ]
            subprocess.run(cmd)

            # Execute the compiled program
            cmd = [variation + "_" + compiler + "_" + flag.replace("=", "_")]
            output = subprocess.check_output(cmd).decode("utf-8")

            # Write the result to the CSV file
            writer.writerow([variation + "_" + compiler + "_" + flag, output])

print("Done!")
```
