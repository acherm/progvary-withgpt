Write a configurable Rust program that implements four features and their selections, namely, Hello, Beautiful, Wonderful, and World... If the feature is selected, then we print the name of the feature. For instance, we could well print "Hello Beautiful World", "Hello World", "Hello", "World" etc. The four features should be implemented as compile-time features.

Sure! Here's an example implementation:

fn main() {
    let features = &["Hello", "Beautiful", "Wonderful", "World"];
    
    if cfg!(feature = "hello") {
        println!("Hello!");
    } else if cfg!(feature = "beautiful") {
        println!("Beautiful!");
    } else if cfg!(feature = "wonderful") {
        println!("Wonderful!");
    } else if cfg!(feature = "world") {
        println!("World!");
    }
}
This code defines an array features containing the names of our four features. Then it uses the cfg! macro to check for each feature at compile time and print out its corresponding message if it is selected. The messages are placed within an if statement with conditions like cfg!(feature = "foo") which will only evaluate to true if the "foo" feature has been enabled in your build environment (e.g., by passing --cfg feature=foo to rustc).
