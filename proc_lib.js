const hoge = "ほげ";

function getData(value) {
    value[0]++;
    // console.log(elem);
    testFunc();
}

function reset() {
    result = [0];
    getData(result);
    elem.innerHTML = "結果" + result;
}