
let _main = () => {
    console.log("yeah");
    setRange(-1.1, 1.1, -2.2, 2.2);
    axis('full', 1, 1, 0, 0);
    return 0;
}

// 作成した関数をマクロに登録する
(function() {
    SVGGraph.registerMacro("main", _main);
})();
