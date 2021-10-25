let xhttp;

const loadDoc = (url, callBack) => {
    xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = () => {
        console.log(this);
        console.log(xhttp);
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            callBack(xhttp);
        }
    };
    xhttp.open("GET",url,true);
    xhttp.send();
}
function load(xhttp) {
    document.getElementById("change").innerHTML = xhttp.responseText;
}