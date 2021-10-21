"use strict"; // 厳格なエラーチェック?

{
    const TEST = document.getElementById("test");
    const HASH_LIST = [
        // 「ハッシュ関数」のハッシュ値
        "105c60d27a2bc2266c55b6a22e5c1bdbfbc1ef084dac2d1b07eccd3be76e47f8", 
        // 「はっしゅかんすう」のハッシュ値
        "b101caf7405d2b771a5fbc7873382c349c661eb6c3cd331e1f80f5abfaa45c28"
    ]
    let FIELD;

    window.onload = () => {
        const _sha_obj = new jsSHA("SHA-256","TEXT");
        FIELD = document.getElementById("field");
        FIELD.addEventListener("input", hashCheck);

        let _text = "はっしゅかんすう";
        _sha_obj.update(_text);
        TEST.textContent = _sha_obj.getHash("HEX");

        // ハッシュ値を予め計算して記録
        // TEST.textContent = "105c60d27a2bc2266c55b6a22e5c1bdbfbc1ef084dac2d1b07eccd3be76e47f8";
    }
    
    let hashCheck = () => {
        const _sha_obj = new jsSHA("SHA-256","TEXT");
        _sha_obj.update(FIELD.value);
        const _hash = _sha_obj.getHash("HEX");

        // console.log(TEST.textContent);
        if (HASH_LIST.includes(_hash)) {
            console.log("正解");
        } else {
            console.log("不正解");
        }
    }
}