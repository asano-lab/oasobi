let xhttp;
let test_btn;
let send_btn;
let img_input;
let img_preview;
let img_file;
let form_data;
let blob_url;

const init = () => {
    img_input = document.getElementById("img_input");
    test_btn = document.getElementById("test_btn");
    send_btn = document.getElementById("send_btn");
    img_preview = document.getElementById("img_preview");
    form_data = new FormData();

    img_input.accept = "image/*"

    console.log(img_preview);
    console.log(form_data);

    test_btn.addEventListener("click", () => {
        loadDoc('cgi-bin/yeah.py?mode=mode', load);
    });

    img_input.addEventListener("input", (e) => {
        loadDoc('cgi-bin/now.py', load);
        // loadDoc('cgi-bin/test01.exe', load);
    });

    img_input.addEventListener("change", (e) => {
        img_file = e.target.files[0];
        // ファイルのブラウザ上でのURL
        blob_url = window.URL.createObjectURL(img_file);

        console.log(blob_url);
        img_preview.innerHTML = "<img src=\"%s\">".replace("%s", blob_url);
        console.log(img_preview);
    });

    send_btn.addEventListener("click", () => {
        toBase64Url(blob_url, (base64url) => {
            console.log("base64url", base64url);
        });
    });
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

function toBase64Url(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        var reader = new FileReader();
        reader.onloadend = function() {
            callback(reader.result);
        }
        reader.readAsDataURL(xhr.response);
    };
    xhr.open('GET', url);
    xhr.responseType = 'blob';
    // xhr.send();
}