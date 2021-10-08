
// 適当な関数
function hogeFunc(x, y) {
    let vx = fix(x, 0);
    let vy = fix(y, 0);
    dot(m.round(vx,2), m.round(vy,2), "dot", "("+x+","+y+")");
}

function main() {
    console.log(setRange);
    setRange(-6, 6, -6, 6);
    axis('full',2,2,0,0);
    style.stroke = 'blue';
    plot('3cos(x)');
    Macro.myCommand(3, 4);
    line(0, 0, 0, 1);
}

(function() {
	SVGGraph.registerMacro("myCommand", hogeFunc);
    SVGGraph.registerMacro("main", main);
})();