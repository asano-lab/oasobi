let result;
let elem;

function init() {
    elem = document.getElementById("output");
    result = [0];
    // first = true;
    // console.log(first);
}

function exec() {
    getData(result);
    elem.innerHTML = "結果" + result;
    for (let i = 0; i < vertices.length; i++) {
        console.log(document.getElementById("line" + i));
    }
}

function testFunc() {
    console.log(hoge);
}