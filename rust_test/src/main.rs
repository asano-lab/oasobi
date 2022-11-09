use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    // --snip--

    let (tx, rx) = mpsc::channel();

    for i in 0..3 {
        let txi = mpsc::Sender::clone(&tx);
        let i_cp = i.clone();
        thread::spawn(move || {
            for j in 0..4 {
                txi.send(j + i_cp * 100).unwrap();
                thread::sleep(Duration::from_secs(1));
            }
        });
    }
    drop(tx);

    for received in rx {
        println!("Got: {}", received);
    }

    // --snip--
}
