const text = document.getElementById("text1");
// console.log(text);

let VALID_VALUES = ["0", "1"];

let DELETE_TYPES = ["deleteContentBackward", "deleteContentForward"];

let prev_value = text.value;

let comp = false;

// text.addEventListener("textInput", (e) => {
//     console.log(e);
// });

text.addEventListener("input", (e) => {
    console.log(e);
    console.log(prev_value);
    if (e.data !== null) {
        console.log(e.data.length);
    }
    console.log(comp);

    if (e.isComposing) {
        console.log(e.data);
        text.value = prev_value;
        comp = true;
    }
    else if (VALID_VALUES.includes(e.data)) {
        prev_value = text.value;
        console.log("有効な入力");
        comp = false;
    }
    else if (DELETE_TYPES.includes(e.inputType)) {
        if (!comp) {
            console.log("削除");
            prev_value = text.value;
        }
    }
    else {
        text.value = prev_value;
        comp = false;
    }
});
