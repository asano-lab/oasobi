let xhttp;

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