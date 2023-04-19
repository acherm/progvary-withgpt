

You answer this:
You can use the `-ffast-math` flag for both GCC and Clang to enable optimizations for floating point operations. This flag enables aggressive optimizations that may violate the IEEE 754 standard.

Here's the updated Python script with the `-ffast-math` flag added to the configurations:

```python
import subprocess
import pandas as pd

def compile_and_run(compiler, flags):
    commands = [
        f"{compiler} {flags} -o original approx.c",
        f"{compiler} {flags} -DUSE_DOUBLE -o double
