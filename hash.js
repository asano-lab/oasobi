"use strict"; // 厳格なエラーチェック?

{
    const SHA_OBJ = new jsSHA("SHA-256","TEXT");
    const TEST = document.getElementById("test");
    let FIELD;

    let hashCheck = () => {
        console.log("あ");
    }

    window.onload = () => {
        FIELD = document.getElementById("field");
        FIELD.addEventListener("input", hashCheck);

        let _text = "ハッシュ関数";

        SHA_OBJ.update(_text);
        TEST.textContent = SHA_OBJ.getHash("HEX");
    }
}