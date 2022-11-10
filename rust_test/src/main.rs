macro_rules! add {
    ($e1: expr, $e2: expr) => {
        $e1 + $e2
    };
}

fn main() {
    let ret = add!(1, 2);
    println!("{}", ret); // -> 3
}
