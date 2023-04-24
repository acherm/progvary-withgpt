# Clang's equivalent for -mfpmath=387

#### You:
 is there an equivalent of -mfpmath=387 (from gcc) for clang?

#### ChatGPT:
Yes, there is an equivalent option in Clang to the `-mfpmath=387` option in GCC.

The equivalent option in Clang is `-mfp387`. This option sets the floating-point model to use the 387 floating-point unit, which is similar to the `-mfpmath=387` option in GCC.

Here's an example of how to use this option in Clang:

```
clang -mfp387 -c myfile.c
```

This command compiles the `myfile.c` file using the 387 floating-point unit.
