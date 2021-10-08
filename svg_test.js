let num_input;
let test_button;

// 適当な関数
function hogeFunc() {
    let x = 2;
    let y = 3;
    let vx = fix(x, 0);
    let vy = fix(y, 0);
    dot(m.round(vx,2), m.round(vy,2), "dot", "("+x+","+y+")");
}

function main() {
    num_input = document.getElementById("num1");
    test_button = document.getElementById("Button3");
    test_button.onclick = Macro.myCommand;
    
    console.log(typeof(num_input.value));
    console.log(num_input.value.length);

    setRange(-6, 10, -4, 4);
    axis('full', 1, 1, 0, 0);
    // Macro.myCommand(3, 4);
    style.stroke = 'red';
    style.strokeWidth = 3;
    let tmp_array = [1, 1, 0, 0, 0, 1];
    let vertices = code2vertices(tmp_array);
    for (let i = 0; i < vertices.length; i++) {
        const [x1, y1, x2, y2] = vertices[i];
        // console.log(x1, y1, x2, y2);
        line(x1, y1, x2, y2);
    }
}

function code2vertices(code) {
    console.log(code.length);
    let vertices = [[0, code[0], 1, code[0]]];
    for (let i = 1; i < code.length; i++) {
        vertices.push([i, code[i - 1], i, code[i]]);
        vertices.push([i, code[i], i + 1, code[i]]);
    }
    return vertices;
}

(function() {
	SVGGraph.registerMacro("myCommand", hogeFunc);
    SVGGraph.registerMacro("main", main);
})();