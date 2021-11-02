
let _main = () => {
    let x, y;
    setRange(-0.1, 1.1, -0.1, 1.1);
    axis('full', 0.5, 0.5, 0, 0);
    for (let i = 0; i < 10; i++) {
        x = Math.random();
        y = Math.random();
        dot(x, y);
    }
}

// 作成した関数をマクロに登録する
(function() {
    SVGGraph.registerMacro("main", _main);
})();
