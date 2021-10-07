let result;
let elem;
let graph;

function init() {
    elem = document.getElementById("output");
    graph = document.getElementById("Graph1");
    console.log(graph);
    result = [0];
    

}

function exec() {
    getData(result);
    elem.innerHTML = "結果" + result;
}

function testFunc() {
    console.log(hoge);
}