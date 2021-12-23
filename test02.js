const text = document.getElementById("text1");
// console.log(text);

let VALID_VALUES = ["0", "1"];

let DELETE_TYPES = ["deleteContentBackward", "deleteContentForward"];

let prev_value = text.value;

text.addEventListener("textInput", (e) => {
    console.log(e);
});

text.addEventListener("input", (e) => {
    console.log(e);
    console.log(prev_value);
    if (e.isComposing) {
        console.log(e.data);
        text.value = prev_value;
        return false;
    }
    else if (VALID_VALUES.includes(e.data)) {
        prev_value = text.value;
        console.log("有効な入力");
    }
    else if (DELETE_TYPES.includes(e.inputType)) {
        console.log("削除");
        text.value = prev_value.slice(0, -1);
        prev_value = text.value;
    }
    else {
        text.value = prev_value;
    }
});

text.addEventListener("compositionstart", (e) => {
    console.log("全角入力開始");
});

text.addEventListener("compositionend", (e) => {
    console.log("全角入力終了");
});
