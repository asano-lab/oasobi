"use strict"; // 厳格なエラーチェック?

{
    const SHA_OBJ = new jsSHA("SHA-256","TEXT");
    const TEST = document.getElementById("test");
    let FIELD;

    window.onload = () => {
        FIELD = document.getElementById("field");
        FIELD.addEventListener("input", hashCheck);

        let _text = "ハッシュ関数";

        SHA_OBJ.update(_text);
        TEST.textContent = SHA_OBJ.getHash("HEX");
    }
    
    let hashCheck = () => {
        const _sha_obj = new jsSHA("SHA-256","TEXT");
        const _text = FIELD.value;
        _sha_obj.update(_text);
        console.log(_text);
        console.log(_sha_obj.getHash("HEX"));
    }
}