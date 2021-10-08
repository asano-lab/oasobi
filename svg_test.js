let num_input;
let test_button;

let vertices;

let line_arr = [];

// let first = true;

// 適当な関数
function hogeFunc() {
    for (let i = 0; i < line_arr.length; i++) {
        line_arr[i].remove();
    }
    // console.log(vertices.length);

    const tmp_array = str2bin(num_input.value);

    vertices = code2vertices(tmp_array);

    // console.log(tmp_array);

    line_arr = [];

    for (let i = 0; i < vertices.length; i++) {
        const [x1, y1, x2, y2] = vertices[i];
        line_arr.push(line(x1, y1, x2, y2));
    }
}

// htmlではこれだけ呼び出せばよい?
function main() {
    num_input = document.getElementById("num1");
    test_button = document.getElementById("Button3");

    test_button.onclick = Macro.hogeFunc;

    // const tmp_array = str2bin(num_input.value);
    // vertices = code2vertices(tmp_array);

    style.stroke = 'red';
    style.strokeWidth = 3;

    setRange(-6, 12, -4, 4);
    axis('full', 1, 1, 0, 0);

    Macro.hogeFunc();
}

// 符号を頂点の座標に変換
function code2vertices(code) {
    // console.log(code.length);
    let vertices = [[0, code[0], 1, code[0]]];
    for (let i = 1; i < code.length; i++) {
        vertices.push([i, code[i - 1], i, code[i]]);
        vertices.push([i, code[i], i + 1, code[i]]);
    }
    return vertices;
}

// 01の文字列を配列に変換
function str2bin(str) {
    bin_arr = [];
    for (let i = 0; i < str.length; i++) {
        if (str[i] == '0') {
            bin_arr.push(0);
        } else if (str[i] == '1') {
            bin_arr.push(1);
        }
        // 01以外が含まれていたら空配列を返す
        else {
            bin_arr = [];
            break;
        }
    }
    return bin_arr;
}

(function() {
	SVGGraph.registerMacro("hogeFunc", hogeFunc);
    SVGGraph.registerMacro("main", main);
})();