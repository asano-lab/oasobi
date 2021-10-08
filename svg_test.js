
function hogeFunc(x, y) {
    let vx = fix(x, 0);
    let vy = fix(y, 0);
    dot(m.round(vx,2), m.round(vy,2), "dot", "("+x+","+y+")");
}

(function() {
	SVGGraph.registerMacro("myCommand", hogeFunc);
})();