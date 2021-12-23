const text = document.getElementById("text1");
// console.log(text);

const VALID_VALUES = ["0", "1"];
const VALID_CODES = ["Digit0", "Digit1", "Backspace", "Delete"];

let DELETE_TYPES = ["deleteContentBackward", "deleteContentForward"];

let prev_value = text.value;

let comp = false;

text.addEventListener("textInput", (e) => {
    console.log(e);
    e.preventDefault();
});

text.addEventListener("input", (e) => {
    text.value = prev_value;
    // console.log(e);
    // console.log(prev_value);
    // if (e.data !== null) {
    //     console.log(e.data.length);
    // }
    // console.log(comp);

    // if (e.isComposing) {
    //     console.log(e.data);
    //     text.value = prev_value;
    //     if (e.data.length == 1) {
    //         comp = false;
    //     } else {
    //         comp = true;
    //     }
    // }
    // else if (VALID_VALUES.includes(e.data)) {
    //     prev_value = text.value;
    //     console.log("有効な入力");
    //     comp = false;
    // }
    // else if (DELETE_TYPES.includes(e.inputType)) {
    //     console.log("わーい");
    //     if (!comp) {
    //         console.log("削除");
    //         prev_value = text.value;
    //     } else {
    //         console.log("削除無効");
    //         text.value = prev_value;
    //     }
    // }
    // else {
    //     text.value = prev_value;
    //     comp = false;
    // }
});

text.addEventListener("keydown", (e) => {
    let mae, ato;
    start = text.selectionStart;
    end = text.selectionEnd;
    console.log(start, end);
    console.log(e);
    if (VALID_CODES.includes(e.code)) {
        mae = prev_value.slice(0, start);
        ato = prev_value.slice(end, prev_value.length);
        if (e.code == "Digit0") {
            text.value = mae + "0" + ato;
            text.selectionStart = start + 1;
            text.selectionEnd = start + 1;
        } else if (e.code == "Digit1") {
            text.value = mae + "1" + ato;
            text.selectionStart = start + 1;
            text.selectionEnd = start + 1;
        }
        if (e.code == "Backspace") {
            if (start == end) {
                text.value = mae.slice(0, -1) + ato;
                if (start > 0) {
                    text.selectionStart = start - 1;
                    text.selectionEnd = start - 1;
                }
            } else {
                text.value = mae + ato;
            }
        }
        prev_value = text.value;
        e.preventDefault();
    }
});
