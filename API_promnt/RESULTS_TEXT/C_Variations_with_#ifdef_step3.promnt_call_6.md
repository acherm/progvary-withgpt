
You answer this:
You can use Python's `subprocess` module and the `pandas` library to run shell commands and compile/execute the C program with different configurations and write the results to a CSV file. Here's a script to accomplish this:

```python
import subprocess
import pandas as pd

def compile_and_run(compiler, flags):
    commands = [
        f"{compiler} {flags} -o assoc assoc.c",
    ]

    results = []
    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)

        binary = cmd.split()[-1]
        output = subprocess.check_output(f'./{binary}', shell=True).decode().strip()
        results.append(output)

    return results

def main():
    configurations = [
        ('gcc', ''),
        ('gcc', '-mfpmath=387'),
        ('clang', ''),
    ]

    data = []
    for compiler, flags in configurations:
        results = compile_and_run(compiler, flags)
        data.append({
            'compiler': compiler,
            'flags': flags,
            'type': 'real',
            'result': results[0],
        })

    df = pd.DataFrame(data)
    df.to_csv('results.csv', index=False)

if __name__ == '__main__':
    main()
```

This script will compile and run the C program with the specified configurations and write the results to a CSV file named `results.csv`.

Make sure the `assoc.c` file containing the C code is in the same directory as the Python script. Then run the Python script:

```sh
python3 compile_and_run.py
```

You can then open the `results.csv` file to see the results in the specified format.
