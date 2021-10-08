let result;
let elem;
let first;

function init() {
    elem = document.getElementById("output");
    result = [0];
    first = true;
    console.log(first);
}

function exec() {
    getData(result);
    elem.innerHTML = "結果" + result;
}

function testFunc() {
    console.log(hoge);
}