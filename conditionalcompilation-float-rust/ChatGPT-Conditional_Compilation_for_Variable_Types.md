# Conditional Compilation for Variable Types.

#### You:
fn main() {
    // Declare and initialize variables
    let x: f64 = 1.0;
    let y: f64 = 1.0;
    let z: f64 = x + y;

    // Print the value of z
    println!("z = {:x?}", z);
} 
 I'd like to create variation over this program using conditional compilation. Specifically, I'd like to create a variation that consists in replacing the type f64 by f32... 

#### ChatGPT:
To create a variation of this program using conditional compilation, you can use the `cfg` attribute to conditionally include or exclude code based on a configuration flag. In this case, we can use a custom configuration flag, such as `use_f32`, to switch between `f64` and `f32` types.

Here's how you can modify the program to achieve this:

```rust
// main.rs

// Declare and initialize variables
#[cfg(not(use_f32))]
fn main() {
    let x: f64 = 1.0;
    let y: f64 = 1.0;
    let z: f64 = x + y;

    // Print the value of z
    println!("z = {:x?}", z);
}

#[cfg(use_f32)]
fn main() {
    let x: f32 = 1.0;
    let y: f32 = 1.0;
    let z: f32 = x + y;

    // Print the value of z
    println!("z = {:x?}", z);
}
```

Now, you can compile the program with the `f64` variation by default. To compile the program with the `f32` variation, pass the `--cfg` flag to `rustc` or include a `build.rs` script to set the configuration flag:

1. Using `rustc` directly:

```sh
rustc --cfg 'use_f32' main.rs
```

2. Using `cargo` and a `build.rs` script:

```rust
// build.rs

fn main() {
    println!("cargo:rustc-cfg=use_f32");
}
```

Include this `build.rs` script in your project root, and the `f32` variation will be compiled when running `cargo build` or `cargo run`.

Keep in mind that using a `build.rs` script is more appropriate for more complex build configurations. For simple cases like this, using `rustc` directly is sufficient.
