use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        // スレッドからやあ(hi from the thread)
        let vals = vec![(0, 1), (2, 3)];

        for val in vals {
            tx.send(val).unwrap();
            // thread::sleep(Duration::from_millis(1000));
        }
    });

    thread::sleep(Duration::from_millis(1000));

    for received in rx {
        println!("Got: {:?}", received);
    }
}
