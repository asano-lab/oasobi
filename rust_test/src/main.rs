fn print2(i: i32, j: i32, k: i32) {
    println!("{}, {}, {}", i, j, k);
}

macro_rules! call_by_double {
    ($name: ident, $e: expr) => {
        $name($e, $e + 1, $e + 2)
    };
}

fn main() {
    call_by_double!(print2, 3); // -> 1, 1
}
