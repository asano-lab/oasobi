
let dec_p_but;
let num_p_input;
let num_points;

const _main = () => {
    dec_p_but = document.getElementById("dec_p_but");
    num_p_input = document.getElementById("num_p_input");
    console.log(dec_p_but);
    dec_p_but.addEventListener("click", Macro.decPoints);

    setRange(-0.1, 1.1, -0.1, 1.1);
    axis('full', 0.5, 0.5, 0, 0);
    Macro.decPoints();
}

const _decPoints = () => {
    let x, y;
    num_points = num_p_input.value;
    console.log(num_points);
    for (let i = 0; i < num_points; i++) {
        x = Math.random();
        y = Math.random();
        dot(x, y);
    }
}

// 作成した関数をマクロに登録する
(function() {
    SVGGraph.registerMacro("main", _main);
    SVGGraph.registerMacro("decPoints", _decPoints);
})();
