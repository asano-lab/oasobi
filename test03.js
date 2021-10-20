
let _main = () => {
    setRange(-1.1, 1.1, -1.1, 1.1);
    axis('full', 0.5, 0.5, 0, 0);
    for (let i = 0; i < 10; i++) {
        console.log(Math.random());
    }
    return 0;
}

// 作成した関数をマクロに登録する
(function() {
    SVGGraph.registerMacro("main", _main);
})();
