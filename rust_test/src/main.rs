macro_rules! map {
    ($($k: expr => $v: expr),*) => {{
        let mut map = ::std::collections::HashMap::new();
        $(map.insert($k, $v));*;
        map
    }};
}

fn main() {
    let nums = map![1 => "one", 2 => "two", 3 => "three"];
    println!("{}", nums[&2]);
    println!("{:?}", nums);
}
