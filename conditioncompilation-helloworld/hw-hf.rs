// eg rustc hw.rs --cfg 'feature="hello"'
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
