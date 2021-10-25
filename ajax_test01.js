let xhttp;
let test_btn;
let img_input;

const init = () => {
    img_input = document.getElementById("img_input");
    test_btn = document.getElementById("test_btn");
    console.log(test_btn);
    // console.log(img_input.clientHeight);
}

const loadDoc = (url, callBack) => {
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = () => {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            callBack(xhttp);
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}

const load = (xhttp) => {
    document.getElementById("change").innerHTML = xhttp.responseText;
}