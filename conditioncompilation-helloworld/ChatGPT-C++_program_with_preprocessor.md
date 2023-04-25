# C++ program with preprocessor.

#### You:
Write a configurable program in C++ language that uses preprocessor annotations for customization. With the annotation #define (C style), we consider four features and their selections, namely, Hello, Beautiful, Wonderful, and World... If the feature is selected, then we print the name of the feature. For instance, we could well print "Hello Beautiful World", "Hello World", "Hello", "World" etc.

#### ChatGPT:
Below is a C++ program using preprocessor directives to customize the output based on the selected features.

```cpp
#include <iostream>

// Define the features you want to use
// Uncomment the features you want to include in the output

//#define HELLO
//#define BEAUTIFUL
//#define WONDERFUL
//#define WORLD

int main() {
    std::string output = "";

    #ifdef HELLO
        output += "Hello ";
    #endif

    #ifdef BEAUTIFUL
        output += "Beautiful ";
    #endif

    #ifdef WONDERFUL
        output += "Wonderful ";
    #endif

    #ifdef WORLD
        output += "World";
    #endif

    if (!output.empty()) {
        std::cout << output << std::endl;
    } else {
        std::cout << "No features selected!" << std::endl;
    }

    return 0;
}
```

To select a feature, simply uncomment the corresponding `#define` line, for example:

```cpp
#define HELLO
//#define BEAUTIFUL
//#define WONDERFUL
#define WORLD
```

With these settings, the program will output "Hello World". To get different outputs, uncomment or comment the desired features. If none of the features are selected, the program will output "No features selected!".


#### You:
can you write a script that generate all possible variants?

#### ChatGPT:
Here's a Python script that generates and compiles all possible variants of the C++ program. It creates separate files for each combination of features and runs them to display their respective outputs. This script requires Python 3 and the `subprocess` module.

```python
import os
import itertools
import subprocess

features = ['HELLO', 'BEAUTIFUL', 'WONDERFUL', 'WORLD']
combinations = [()]
for i in range(1, len(features) + 1):
    combinations.extend(list(itertools.combinations(features, i)))

cpp_template = '''\
#include <iostream>

{feature_defines}

int main() {{
    std::string output = "";

    #ifdef HELLO
        output += "Hello ";
    #endif

    #ifdef BEAUTIFUL
        output += "Beautiful ";
    #endif

    #ifdef WONDERFUL
        output += "Wonderful ";
    #endif

    #ifdef WORLD
        output += "World";
    #endif

    if (!output.empty()) {{
        std::cout << output << std::endl;
    }} else {{
        std::cout << "No features selected!" << std::endl;
    }}

    return 0;
}}
'''

for i, combination in enumerate(combinations):
    feature_defines = '\n'.join(f'#define {feature}' for feature in combination)
    cpp_code = cpp_template.format(feature_defines=feature_defines)
    file_name = f"output_variant_{i}.cpp"

    with open(file_name, 'w') as file:
        file.write(cpp_code)

    subprocess.run(["g++", "-std=c++11", "-o", f"output_variant_{i}", file_name])
    print(f"Running variant {i}: {' '.join(combination)}")
    subprocess.run([f"./output_variant_{i}"])
    print()

    os.remove(file_name)
    os.remove(f"output_variant_{i}")
```

This script will generate all possible combinations of the features, create a C++ file for each, compile the files, and then run the resulting executables. The script also cleans up the generated files when it's done. Note that the script assumes you have the GNU Compiler Collection (GCC) installed on your system and available in your `PATH`.
