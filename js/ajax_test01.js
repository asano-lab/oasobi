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
        console.log(img_file);
        const encoded_file = base64Encode(img_file);
        console.log(encoded_file);
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

const base64Encode = (...parts) => {
    return new Promise(resolve => {
        const reader = new FileReader();
        reader.onload = () => {
            const offset = reader.result.indexOf(",") + 1;
            resolve(reader.result.slice(offset));
        };
        reader.readAsDataURL(new Blob(parts));
    });
}
  
function base64Decode(text, charset) {
    return fetch(`data:text/plain;charset=${charset};base64,` + text).then(response => response.text());
}

function base64DecodeAsBlob(text, type = "text/plain;charset=UTF-8") {
    return fetch(`data:${type};base64,` + text).then(response => response.blob());
} 