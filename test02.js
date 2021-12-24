const text = document.getElementById("text1");
// console.log(text);

let password = document.getElementById("text2");

const VALID_VALUES = ["0", "1"];
const VALID_CODES = [
    "Digit0", "Digit1", "Backspace", "Delete",
    "ArrowLeft", "ArrowRight", "KeyA"
];

let DELETE_TYPES = ["deleteContentBackward", "deleteContentForward"];

let prev_value = text.value;

let comp = false;

let start, end, base;

const resetTextSelection = () => {
    text.selectionStart = start;
    text.selectionEnd = end;
};

const setTextSelection = (s1, s2) => {
    if (s1 < s2) {
        text.selectionStart = s1;
        text.selectionEnd = s2;
    } else {
        text.selectionStart = s2;
        text.selectionEnd = s1;
    }
};

const getTextSelection = () => {
    return [text.selectionStart, text.selectionEnd]
};

text.addEventListener("select", (e) => {
    console.log(e);
    setTextSelection(start, end);
});

text.addEventListener("input", (e) => {
    console.log(e);
    text.value = prev_value;
    // console.log(text.selectionStart);
    // console.log(text.selectionEnd);
    text.selectionStart = start;
    text.selectionEnd = end;
    // e.preventDefault();
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
    console.log(e);
    if (VALID_CODES.includes(e.code)) {
        [start, end] = getTextSelection();
        console.log(start, end);

        mae = prev_value.slice(0, start);
        ato = prev_value.slice(end, prev_value.length);

        if (e.code == "Digit0") {
            text.value = mae + "0" + ato;
            setTextSelection(start + 1, start + 1);
        } else if (e.code == "Digit1") {
            text.value = mae + "1" + ato;
            setTextSelection(start + 1, start + 1);
        } else if (e.code == "Backspace") {
            if (start == end) {
                text.value = mae.slice(0, -1) + ato;
                if (start > 0) {
                    setTextSelection(start - 1, start - 1);
                }
            } else {
                text.value = mae + ato;
                setTextSelection(start, start);
            }
        } else if (e.code == "Delete") {
            if (start == end) {
                text.value = mae + ato.slice(1, ato.length);
            } else {
                text.value = mae + ato;
            }
            setTextSelection(start, start);
        } else if (e.code == "ArrowLeft") {
            if (e.shiftKey) {
                if (start == end) {
                    base = start;
                    setTextSelection(start - 1, base);
                } else if (base < end) {
                    setTextSelection(base, end - 1);
                } else if (start > 0) {
                    setTextSelection(start - 1, base);
                }
            } else {
                if (start != end) {
                    setTextSelection(start, start);
                } else if (start > 0) {
                    setTextSelection(start - 1, start - 1);
                }
            }
        } else if (e.code == "ArrowRight") {
            if (e.shiftKey) {
                if (start == end) {
                    base = start;
                    setTextSelection(base, end + 1);
                } else if (start < base) {
                    setTextSelection(start + 1, base);
                }
                else if (start > 0) {
                    setTextSelection(base, end + 1);
                }
            } else {
                if (start != end) {
                    setTextSelection(end, end);
                } else if (start < prev_value.length) {
                    setTextSelection(start + 1, start + 1);
                }
            }
        } else if (e.code == "KeyA") {
            if (e.ctrlKey) {
                setTextSelection(0, prev_value.length);
            }
        }
        [start, end] = getTextSelection();
        prev_value = text.value;
    } else {
        text.value = prev_value;
    }
    e.preventDefault();
});

text.addEventListener("click", (e) => {
    console.log(e);
    [start, end] = getTextSelection();
});

password.addEventListener("input", (e) => {
    password.type = "text";
});

password.addEventListener("keydown", (e) => {
    password.type = "password";
});

function getAllEvents(element) {
    let result = [];
    for (const key in element) {
        if (key.indexOf('on') === 0) {
            result.push(key.slice(2, key.length));
        }
    }
    return result;
}

// let all_events = getAllEvents(text);
// for (const event of all_events) {
//     console.log(event);
//     text.addEventListener(event, (e) => {
//         console.log(event);
//         console.log(e);
//     });
// }
