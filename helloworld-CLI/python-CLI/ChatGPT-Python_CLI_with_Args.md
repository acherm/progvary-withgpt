# Python CLI with Args

#### You:
Write a configurable Python program that implements four features and their selections, namely, Hello, Beautiful, Wonderful, and World... If the feature is selected, then we print the name of the feature. For instance, we could well print "Hello Beautiful World", "Hello World", "Hello", "World" etc. Please implement the four features as command-line parameters and the Python program as a CLI

#### ChatGPT:
You can create a Python script that accepts command-line arguments using the `argparse` module. Here's a simple script that takes four optional features as command-line parameters and prints them if they're selected:

```python
# features.py
import argparse

def main():
    parser = argparse.ArgumentParser(description='Select features to print.')

    parser.add_argument('--hello', action='store_true', help='Print "Hello"')
    parser.add_argument('--beautiful', action='store_true', help='Print "Beautiful"')
    parser.add_argument('--wonderful', action='store_true', help='Print "Wonderful"')
    parser.add_argument('--world', action='store_true', help='Print "World"')

    args = parser.parse_args()

    output = []

    if args.hello:
        output.append('Hello')
    if args.beautiful:
        output.append('Beautiful')
    if args.wonderful:
        output.append('Wonderful')
    if args.world:
        output.append('World')

    print(' '.join(output))

if __name__ == '__main__':
    main()
```

To run the script, save it as `features.py` and execute it from the command line:

```bash
python features.py --hello --beautiful --wonderful --world
```

This will print:

```
Hello Beautiful Wonderful World
```

You can choose any combination of features or even a single feature:

```bash
python features.py --hello
```

This will print:

```
Hello
```

The script can be easily extended to include more features if needed.


#### You:
Write a script that generates all possible combinations of features and calling the Python CLI

#### ChatGPT:
You can use the `subprocess` module to call the Python CLI with different combinations of features. To generate all possible combinations of features, you can use the `itertools` module. Here's a script that does that:

```python
# generate_combinations.py
import itertools
import subprocess

def generate_feature_combinations(features):
    combinations = []
    for length in range(len(features) + 1):
        for subset in itertools.combinations(features, length):
            combinations.append(subset)
    return combinations

def main():
    features = ['--hello', '--beautiful', '--wonderful', '--world']
    combinations = generate_feature_combinations(features)

    for combo in combinations:
        print(f"Running CLI with options: {' '.join(combo)}")
        subprocess.run(['python', 'features.py', *combo])

if __name__ == '__main__':
    main()
```

Make sure to save the `features.py` script from the previous answer, and then save this script as `generate_combinations.py`. Run it from the command line:

```bash
python generate_combinations.py
```

This script will generate all possible combinations of features and call the `features.py` script with the corresponding command-line arguments. You will see the output for each combination, like:

```
Running CLI with options: 
Running CLI with options: --hello
Hello
Running CLI with options: --beautiful
Beautiful
...
Running CLI with options: --hello --beautiful --wonderful --world
Hello Beautiful Wonderful World
```

This script can be easily extended to handle more features if needed.
