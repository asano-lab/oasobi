let xhttp;
let test_btn;
let img_input;

const init = () => {
    img_input = document.getElementById("img_input");
    test_btn = document.getElementById("test_btn");
    console.log(img_input);
    console.log(test_btn);

    test_btn.addEventListener("click", () => {
        loadDoc('cgi-bin/yeah.py?mode=mode', load);
    });

    img_input.addEventListener("input", () => {
        console.log(img_input.value);
        loadDoc('cgi-bin/now.py', load);
    });
    
    console.log(img_input);
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