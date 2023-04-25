# Fixing Function Call Error

#### You:
Is there any issue with this code: 
#ifdef CONFIG_ARCH_OMAP2420
void omap2_set_globals_242x(void)
{
    return;
}
#endif

#ifdef CONFIG_MACH_OMAP_H4
static void omap_h4_map_io(void)
{
    omap2_set_globals_242x(); // ERROR
}
#endif

int main(int argc, char** argv)
{
#ifdef CONFIG_MACH_OMAP_H4
    omap_h4_map_io();
#endif
}


#### ChatGPT:
The issue with this code is that the function call `omap2_set_globals_242x()` inside `omap_h4_map_io()` is causing a compile-time error because it is only defined when `CONFIG_ARCH_OMAP2420` is defined. However, the `omap_h4_map_io()` function is only defined when `CONFIG_MACH_OMAP_H4` is defined, which means that `omap2_set_globals_242x()` may not be defined at the point of the function call.

To fix this issue, you need to ensure that `omap2_set_globals_242x()` is defined whenever `omap_h4_map_io()` is defined. One way to achieve this is to include the definition of `omap2_set_globals_242x()` inside the `CONFIG_MACH_OMAP_H4` block as shown below:

```
#ifdef CONFIG_ARCH_OMAP2420
void omap2_set_globals_242x(void)
{
    return;
}
#endif

#ifdef CONFIG_MACH_OMAP_H4
static void omap_h4_map_io(void)
{
#ifdef CONFIG_ARCH_OMAP2420
    omap2_set_globals_242x();
#endif
}
#endif

int main(int argc, char** argv)
{
#ifdef CONFIG_MACH_OMAP_H4
    omap_h4_map_io();
#endif
}
```

By including the definition of `omap2_set_globals_242x()` inside the `CONFIG_MACH_OMAP_H4` block, you ensure that it is defined whenever `omap_h4_map_io()` is defined, avoiding the compile-time error.
