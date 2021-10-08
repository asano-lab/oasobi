let result;
let elem;
// let graph;


function init() {
    elem = document.getElementById("output");
    graph = document.getElementById("Graph1");
    result = [0];
}

function exec() {
    getData(result);
    elem.innerHTML = "結果" + result;
    graph.width = 300;
    graph.script="setRange(-10, 10, -5, 5)";
    // console.log(graph);
}

function testFunc() {
    console.log(hoge);
}