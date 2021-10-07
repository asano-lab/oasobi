let result;
let elem;

function init() {
    elem = document.getElementById("output");
    result = getData(-1);
}

function exec() {
    result = getData(result);
    elem.innerHTML = "結果" + result;
}