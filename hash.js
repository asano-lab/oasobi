"use strict"; // 厳格なエラーチェック?

{
    const SHA_OBJ = new jsSHA("SHA-256","TEXT");
    const TEST = document.getElementById("test");
    let FIELD;

    window.onload = () => {
        FIELD = document.getElementById("field");
        FIELD.addEventListener("input", hashCheck);

        // let _text = "ハッシュ関数";
        // SHA_OBJ.update(_text);
        // TEST.textContent = SHA_OBJ.getHash("HEX");

        // ハッシュ値を予め計算して記録
        TEST.textContent = "105c60d27a2bc2266c55b6a22e5c1bdbfbc1ef084dac2d1b07eccd3be76e47f8";
    }
    
    let hashCheck = () => {
        const _sha_obj = new jsSHA("SHA-256","TEXT");
        _sha_obj.update(FIELD.value);
        const _hash = _sha_obj.getHash("HEX");

        console.log(TEST.textContent);
        if (TEST.textContent == _hash) {
            console.log("正解");
        }
    }
}