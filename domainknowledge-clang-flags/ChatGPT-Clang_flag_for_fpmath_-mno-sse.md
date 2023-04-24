# Clang flag for fpmath: -mno-sse.

#### You:
is there an equivalent of -mfpmath=387 (from gcc) for clang?

#### ChatGPT:
Yes, clang also provides a similar option to control the floating-point math unit used for code generation. The equivalent flag to `-mfpmath=387` in GCC for clang is `-mno-sse`. This flag disables the use of SSE instructions for floating-point math, and instead, the compiler will generate code targeting the x87 FPU (Floating-Point Unit), which is the same as the 387 FPU.

To use this flag, you can simply pass it as a command-line argument to clang when compiling your code:

```sh
clang -mno-sse your_source_file.c -o your_output_file
```

Keep in mind that this flag is relevant primarily for x86 and x86-64 platforms. Other platforms may have different flags or options for controlling the floating-point unit used for code generation.
