# Rust Configurable Feature Program

#### You:
Write a configurable Rust program that implements four features and their selections, namely, Hello, Beautiful, Wonderful, and World... If the feature is selected, then we print the name of the feature. For instance, we could well print "Hello Beautiful World", "Hello World", "Hello", "World" etc. The four features should be implemented as compile-time features.  

#### ChatGPT:
To implement this in Rust, you can use the `cfg` attribute to enable or disable the features at compile-time. You need to define the features in your `Cargo.toml` file and then use the `cfg` attribute in your `main.rs` file to selectively print the feature names based on the selected features.

Here is an example of how to implement this:

1. First, open your `Cargo.toml` file and add the following lines under the `[features]` section:

```toml
[features]
default = []
hello = []
beautiful = []
wonderful = []
world = []
```

2. Next, create the `main.rs` file and add the following code:

```rust
fn main() {
    #[cfg(feature = "hello")]
    print!("Hello ");

    #[cfg(feature = "beautiful")]
    print!("Beautiful ");

    #[cfg(feature = "wonderful")]
    print!("Wonderful ");

    #[cfg(feature = "world")]
    print!("World");

    println!();
}
```

3. Now, you can compile your program with different feature selections. For example:

- To compile with the `hello` and `world` features:

  ```
  cargo run --features "hello world"
  ```

- To compile with the `hello`, `beautiful`, and `world` features:

  ```
  cargo run --features "hello beautiful world"
  ```

- To compile with all four features:

  ```
  cargo run --features "hello beautiful wonderful world"
  ```

When you compile and run your program with different feature selections, you will see the respective output:

```
Hello World
Hello Beautiful World
Hello Beautiful Wonderful World
```
