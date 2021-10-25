
function loadDoc(url,callBack) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        callBack(this);
    }
    };
    xhttp.open("GET",url,true);
    xhttp.send();
}
function load(xhttp) {
    document.getElementById("change").innerHTML = xhttp.responseText;
}