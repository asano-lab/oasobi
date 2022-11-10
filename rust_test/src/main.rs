macro_rules! ignore {
    ($pat: tt) => {};
}

macro_rules! match_vec {
    // `vec![]`パターンの末尾カンマに対応するために末尾カンマを取り除いて本体に渡すための節
    (let vec![$($pat:pat),*,] = $v:expr;) => (
        match_vec!(let vec![$($pat),*] = $v;)
    );
    // 本体
    (let vec![$($pat:pat),*] = $v:expr;) => (
        let ($($pat),*) = {
            // * exprで受けたので`vec![1, 2, 3]`などのまだ評価されていない式も来うる。
            //   一旦変数に格納して評価させる。
            // * ついでに`mut`をつけたりイテレータを取り出したり。
            let mut i = $v.into_iter();
            // * `$()*`を使いたいが`$pat`は使わないので`ignore`を使って無視する
            // * お粗末だが`next()`に対して`unwrap()`している。
            //   実行時のマッチ失敗panicを投げる余裕があるなら投げるべき。
            let ret = ($({ignore!($pat); i.next().unwrap()}),*);
            // 同じくvecが余った場合の検査を`assert!`に丸投げしている。
            assert!(i.next().is_none());
            ret
        };
    )
}

fn main() {
    let v = vec![1, 2, 3];
    match_vec! {
        let vec![x, y, z] = v;
    }
    // 上の式を展開するとこうなるはず。
    //
    // // 複数のパターンマッチをタプルのマッチに落とし込んでいる。
    // let (x, y, z) = {
    //   // (マニアックな話):Rustのマクロは衛生的なのでマクロ内で定義した`i`がgensym(rename)される。
    //   let mut i_xxx = v.into_iter();
    //   let ret = (
    //     {ignore!(x);i_xxx.next().unwrap()},
    //     {ignore!(y);i_xxx.next().unwrap()},
    //     {ignore!(z);i_xxx.next().unwrap()},
    //   );
    //   assert!(i_xxx.next().is_none());
    //   ret
    // };
    println!("x: {}, y: {}, z: {}", x, y, z); // -> x: 1, y: 2, z: 3
}
