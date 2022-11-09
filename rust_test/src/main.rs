use std::thread;
use std::time::Duration;

fn fibo(n: i32) -> i32 {
    if n <= 0 {
        return 0;
    } else if n == 1 {
        return 1;
    }
    return fibo(n - 1) + fibo(n - 2);
}

fn main() {
    thread::spawn(|| {
        println!("{}", fibo(45));
    });

    println!("{}", fibo(45));
}
