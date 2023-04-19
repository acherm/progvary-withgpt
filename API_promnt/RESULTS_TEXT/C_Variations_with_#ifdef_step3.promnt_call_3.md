
You answer this:
You can use Python's `pandas` module to write the CSV. Here's a script to accomplish this:

```python
import pandas as pd
import subprocess

def compile_and_run(compiler, flags):
    commands = [
        f"{compiler} {flags} -o original assoc.c",
        f"{compiler} {flags} -DUSE_DOUBLE -o double_variation assoc.c",
        f"{compiler} {flags} -DUSE_FLOAT -o float_variation assoc.c",
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
            'type': 'original',
            'result': results[0],
        })
        data.append({
            'compiler': compiler,
            'flags': flags,
            'type': 'double',
            'result': results[1],
        })
        data.append({
            'compiler': compiler,
            'flags': flags,
            'type': 'float',
            'result': results[2],
        })

    df = pd.DataFrame(data)
    df.to_csv('results.csv', index=False)

if __name__ == '__main__':
    main()
```

This script will compile and run the three variants of the C program with the specified configurations and write the results to a CSV file named `results.csv
