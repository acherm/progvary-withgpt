
You answer this:
You can use the `pandas` library to write the CSV file. Here's a modified version of the script that uses `pandas`:

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

    df = pd.DataFrame(data, columns=['compiler', 'flags', 'type', 'result'])
    df.to_csv('results.csv', index=False)

if __name__ == '__main__':
    main()
```

This script will compile and run
