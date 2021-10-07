let result;
let elem;

function init() {
    elem = document.getElementById("output");
    result = [0];
    init2();
}

function exec() {
    getData(result);
    elem.innerHTML = "結果" + result;
}

function testFunc() {
    console.log(hoge);
}