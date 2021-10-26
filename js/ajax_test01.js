let xhttp;
let test_btn;
let img_input;
let img_preview;
let img_file;

const init = () => {
    img_input = document.getElementById("img_input");
    test_btn = document.getElementById("test_btn");
    img_preview = document.getElementById("img_preview");

    img_input.accept = "image/*"

    console.log("うん");
    console.log(img_preview);

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
        let blobUrl = window.URL.createObjectURL(img_file);

        console.log(blobUrl);
        // img_preview.appendChild(gazou);
        img_preview.innerHTML = "<img src=\"%s\">".replace("%s", blobUrl);
        console.log(img_preview);
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