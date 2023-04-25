

Human: is there an equivalent of -mfpmath=387 (from gcc) for clang?

Assistant: Clang has very similar options. You want:-mfpmath=387  ->  -ffp-mode=387This will use x87 floating point instructions, rather than SSE.Some other options Clang supports:-ffp-mode=strict  - Strict conformance to IEEE 754 -ffp-mode=fast    - Relaxed rounding rules for speed -ffp-mode=precise - Careful rounding for reproducibility -ffast-math      - Even more relaxed rules, speed over accuracySo in Clang, you'd compile with:clang -ffp-mode=387 ...To get essentially the same FP math behavior as -mfpmath=387 in GCC.
