# Variations using Conditional Compilation

#### You:
fn main() {
    // Declare and initialize variables
    let x: f64 = 1.0;
    let y: f64 = 1.0;
    let z: f64 = x + y;

    // Print the value of z
    println!("z = {:x?}", z);
} 
 I'd like to create variations over this program using conditional compilation. Specifically, I'd like to create a first variation that consists in replacing the type f64 by f32... and another alternative variation that consists in replacing f64 by f128

#### ChatGPT:
You can use conditional compilation with the `cfg` attribute and feature flags in your `Cargo.toml` file to create different variations of your program. Here's how you can achieve the two variations you mentioned:

1. In your `Cargo.toml` file, add the following under the `[features]` section:

```toml
[features]
default = []
f32 = []
f128 = []
```

2. Modify your `main.rs` file to use conditional compilation:

```rust
// Import f128 type if f128 feature is enabled
#[cfg(feature = "f128")]
use f128::f128;

fn main() {
    // Declare and initialize variables
    #[cfg(feature = "f32")]
    let (x, y): (f32, f32) = (1.0, 1.0);
    #[cfg(feature = "f128")]
    let (x, y): (f128, f128) = (f128!(1.0), f128!(1.0));
    #[cfg(not(any(feature = "f32", feature = "f128")))]
    let (x, y): (f64, f64) = (1.0, 1.0);

    let z = x + y;

    // Print the value of z
    println!("z = {:?}", z);
}
```

3. Add the `f128` crate to your `Cargo.toml` file since it's not included in the standard library:

```toml
[dependencies]
f128 = "0.2"
```

Now you can compile your program with different variations:

- For the default variation (f64), run `cargo build --bin your_bin_name`.
- For the f32 variation, run `cargo build --bin your_bin_name --features f32`.
- For the f128 variation, run `cargo build --bin your_bin_name --features f128`.
