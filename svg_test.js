let num_input;
let rand_num_view;
let test_button;
let random_button;

let line_arr;

let random;

// htmlではこれだけ呼び出せばよい (多分)
function _main() {
    const now = new Date();
    const t0 = now.getTime();
    console.log(t0);
    random = new RandomMT(t0);

    num_input = document.getElementById("num1");
    test_button = document.getElementById("Button1");
    random_button = document.getElementById("Button2");

    // クリック時のアクションにマクロを登録
    test_button.onclick =  Macro.drawGraph;
    random_button.onclick = Macro.drawRandom;

    style.stroke = 'red';
    style.strokeWidth = 3;

    setRange(-1, 20, -3, 3);
    axis('full', 1, 1, 0, 0);

    line_arr = [];
    Macro.drawGraph();

    for (let i = 0; i < 10000; i++) {
        let rd = random.next();
        if (i >= 9990) {
            console.log(i, rd);
        }
    }
}

// 符号を頂点の座標に変換
function code2vertices(code) {
    if (!code.length) {
        return [];
    }
    let vertices = [[0, code[0], 1, code[0]]];
    for (let i = 1; i < code.length; i++) {
        vertices.push([i, code[i - 1], i, code[i]]);
        vertices.push([i, code[i], i + 1, code[i]]);
    }
    return vertices;
}

// 01の文字列を配列に変換
function str2bin(str) {
    let bin_arr = [];
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

// グラフ描画
function _drawGraph() {
    // 直前のグラフを削除
    for (let i = 0; i < line_arr.length; i++) {
        line_arr[i].remove();
    }
    line_arr = [];

    const tmp_array = str2bin(num_input.value);
    const vertices = code2vertices(tmp_array);
    let x1, y1, x2, y2;

    for (let i = 0; i < vertices.length; i++) {
        [x1, y1, x2, y2] = vertices[i]; // アンパック代入
        line_arr.push(line(x1, y1, x2, y2));
    }
}

// ランダムな波形を描画
function _drawRandom() {
    const r = random.next() & 0xfffff; // 20bit
    let r_str = r.toString(2);

    // 0埋め
    for (let i = r_str.length; i < 20; i++) {
        r_str = "0" + r_str;
    }
    num_input.value = r_str;

    Macro.drawGraph();
}