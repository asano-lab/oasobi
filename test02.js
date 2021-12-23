const text = document.getElementById("text1");
// console.log(text);

let VALID_VALUES = ["0", "1"];

let DELETE_TYPES = ["deleteContentBackward"];

let prev_value = "";

text.addEventListener("input", (e) => {
    console.log(e);
    if (VALID_VALUES.includes(e.data)) {
        prev_value = text.value;
    }
    else if (DELETE_TYPES.includes(e.inputType)) {
        prev_value = text.value;
    }
    else {
        text.value = prev_value;
    }
});
