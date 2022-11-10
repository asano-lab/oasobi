fn print2(i: i32, j: i32, k: i32) {
    println!("{}, {}, {}", i, j, k);
}

macro_rules! call_by_double {
    ($name: ident, $e: expr) => {
        $name($e, $e + 1, $e + 2)
    };
}

macro_rules! bind {
    ($var: ident, $val: expr) => {
        let $var = $val;
    };
}
macro_rules! exact_one {
    () => {
        Some(1)
    };
}

macro_rules! two {
    ($x: ident) => (Some($x @ 2..=3))
}

macro_rules! three {
    ($x: ident) => (Some($x @ 4..=5))
}

macro_rules! many_or_none {
    () => {
        _
    };
}

fn main() {
    call_by_double!(print2, 3); // -> 1, 1
    bind!(x, 3729);
    println!("{}", x);
    // println!("{:?}", exact_one!());
    match Some(6) {
        exact_one!() => println!("exact one"),
        two!(x) => println!("a {}", x),
        three!(x) => println!("b {}", x),
        many_or_none!() => (),
    };
}
