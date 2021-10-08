
// 適当な関数
function hogeFunc(x, y) {
    let vx = fix(x, 0);
    let vy = fix(y, 0);
    dot(m.round(vx,2), m.round(vy,2), "dot", "("+x+","+y+")");
}

function main() {
    // console.log(setRange);
    setRange(-6, 6, -6, 6);
    axis('full',2,2,0,0);
    style.stroke = 'blue';
    plot('3cos(x)');
    Macro.myCommand(3, 4);
    style.stroke = 'red';
    style.strokeWidth = 2;
    let tmp_array = [0, 1, 0, 1, 0, 1];
    code2vertices(tmp_array);
    // console.log(1, 2);
    line(0, 0, 2, 2);
}

function code2vertices(code) {
    console.log(code.length);
}

(function() {
	SVGGraph.registerMacro("myCommand", hogeFunc);
    SVGGraph.registerMacro("main", main);
})();