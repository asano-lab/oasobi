let xhttp;
let test_btn;
let img_input;
let img_preview;

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
        // console.log("change", e);
        let f = e.target.files[0];
        console.log(f);

        // ファイルのブラウザ上でのURL
        let blobUrl = window.URL.createObjectURL(f);
        let gazou = document.createElement("img");

        console.log(blobUrl);
        gazou.src = blobUrl;
        img_preview.appendChild(gazou);
        console.log(img_preview);
        console.log(gazou.naturalHeight);
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