# C code conditional compilation.

#### You:
is there any issue with the following C code?
df_bin_default_columns default_style_cols[LAST_PLOT_STYLE + 1] = {
    // other elements here
    {HISTOGRAMS, 1, 0},
#ifdef WITH_IMAGE
    {IMAGE, 1, 2},
    {RGBIMAGE, 3, 2}
#endif
#ifdef EAM_OBJECTS
    , {CIRCLES, 2, 1},
#endif
};

#### ChatGPT:
There is a potential issue with the conditional compilation (using `#ifdef`) in the array initialization. If the `WITH_IMAGE` macro is not defined, and the `EAM_OBJECTS` macro is defined, you will have an extra comma before the `{CIRCLES, 2, 1}` element, which will lead to a compilation error.

To fix the issue, you can reorganize the conditional compilation as follows:

```c
df_bin_default_columns default_style_cols[LAST_PLOT_STYLE + 1] = {
    // other elements here
    {HISTOGRAMS, 1, 0},
#ifdef WITH_IMAGE
    {IMAGE, 1, 2},
    {RGBIMAGE, 3, 2},
#endif
#ifdef EAM_OBJECTS
    {CIRCLES, 2, 1},
#endif
};
```

This way, you avoid having an extra comma before the `{CIRCLES, 2, 1}` element when only the `EAM_OBJECTS` macro is defined.
