let xhttp;
let test_btn;
let img_input;
let img_preview;

const init = () => {
    img_input = document.getElementById("img_input");
    test_btn = document.getElementById("test_btn");
    img_preview = document.getElementById("img_preview");

    // img_input.accept = ".png, .jpg, .jpeg";
    img_input.accept = "image/*"

    console.log("うん");

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
        console.log(blobUrl);
        img_preview.src = blobUrl;
        console.log(img_preview);
        console.log(img_preview.naturalWidth);
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