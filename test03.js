
let dec_p_but;
let num_p_input;
let num_points;
let el_points;

const _main = () => {
    dec_p_but = document.getElementById("dec_p_but");
    num_p_input = document.getElementById("num_p_input");
    dec_p_but.addEventListener("click", Macro.decPoints);

    el_points = [];

    setRange(-0.1, 1.1, -0.1, 1.1);
    axis('full', 0.5, 0.5, 0, 0);
    Macro.decPoints();
}

const _decPoints = () => {
    let x, y;
    for (let i = 0; i < el_points.length; i++) {
        el_points[i].remove();
    }
    num_points = num_p_input.value;
    console.log(num_points);
    for (let i = 0; i < num_points; i++) {
        x = Math.random();
        y = Math.random();
        el_points.push(dot(x, y));
    }
}

// 作成した関数をマクロに登録する
(function() {
    SVGGraph.registerMacro("main", _main);
    SVGGraph.registerMacro("decPoints", _decPoints);
})();
