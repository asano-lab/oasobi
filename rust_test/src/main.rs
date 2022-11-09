use std::sync::mpsc;
use std::thread;
use std::time;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
        // valは{}
        // println!("val is {}", val);
    });
    // thread::sleep(time::Duration::from_millis(1));

    let received = rx.try_recv().unwrap();
    println!("Got: {}", received);
}
