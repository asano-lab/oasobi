const VALID_VALUES = ["0", "1"];
const VALID_CODES = [
    "Digit0", "Digit1", "Backspace", "Delete",
    "ArrowLeft", "ArrowRight", "KeyA"
];

class MyTextBox {
    constructor(textbox) {

        this.textbox = textbox;

        // 変数初期化
        this.prev_value = textbox.value;
        this.start = this.textbox.selectionStart;
        this.end = this.textbox.selectionEnd;
        this.base = this.start;

        // keydownイベントの処理
        this.textbox.addEventListener("keydown", (e) => {
            // カーソル前後の文字列
            let mae, ato;
            console.log(e);
    
            if (VALID_CODES.includes(e.code)) {
                [this.start, this.end] = this.getSelections();
                console.log(this.start, this.end);
        
                mae = this.prev_value.slice(0, this.start);
                ato = this.prev_value.slice(this.end, this.prev_value.length);
        
                if (e.code == "Digit0") {
                    this.textbox.value = mae + "0" + ato;
                    this.setSelections(this.start + 1, this.start + 1);
                } else if (e.code == "Digit1") {
                    this.textbox.value = mae + "1" + ato;
                    this.setSelections(this.start + 1, this.start + 1);
                } else if (e.code == "Backspace") {
                    if (this.start == this.end) {
                        this.textbox.value = mae.slice(0, -1) + ato;
                        if (start > 0) {
                            this.setSelections(this.start - 1, this.start - 1);
                        }
                    } else {
                        this.textbox.value = mae + ato;
                        this.setSelections(this.start, this.start);
                    }
                } else if (e.code == "Delete") {
                    if (this.start == this.end) {
                        this.textbox.value = mae + ato.slice(1, ato.length);
                    } else {
                        this.textbox.value = mae + ato;
                    }
                    this.setSelections(this.start, this.start);
                } else if (e.code == "ArrowLeft") {
                    if (e.shiftKey) {
                        if (this.start == this.end) {
                            this.base = this.start;
                            this.setSelections(this.start - 1, this.base);
                        } else if (this.base < this.end) {
                            this.setSelections(this.base, this.end - 1);
                        } else if (this.start > 0) {
                            this.setSelections(this.start - 1, this.base);
                        }
                    } else {
                        if (this.start != this.end) {
                            this.setSelections(this.start, this.start);
                        } else if (this.start > 0) {
                            this.setSelections(this.start - 1, this.start - 1);
                        }
                    }
                } else if (e.code == "ArrowRight") {
                    if (e.shiftKey) {
                        if (this.start == this.end) {
                            this.base = this.start;
                            this.setSelections(this.base, this.end + 1);
                        } else if (this.start < this.base) {
                            this.setSelections(this.start + 1, this.base);
                        }
                        else if (this.start > 0) {
                            this.setSelections(this.base, this.end + 1);
                        }
                    } else {
                        if (this.start != this.end) {
                            this.setSelections(this.end, this.end);
                        } else if (this.start < this.prev_value.length) {
                            this.setSelections(this.start + 1, this.start + 1);
                        }
                    }
                } else if (e.code == "KeyA") {
                    if (e.ctrlKey) {
                        this.setSelections(0, this.prev_value.length);
                    }
                }
                [this.start, this.end] = this.getSelections();
                this.prev_value = this.textbox.value;
            }
        });

        this.textbox.addEventListener("select", () => {
            this.setSelections(this.start, this.end);
        });

        this.textbox.addEventListener("input", () => {
            this.setSelections(this.start, this.end);
            this.textbox.value = this.prev_value;
        });
    }

    // カーソル位置の取得
    getSelections() {
        return [this.textbox.selectionStart, this.textbox.selectionEnd]
    }
    
    // カーソル位置の設定
    setSelections(s1, s2) {
        if (s1 < s2) {
            this.textbox.selectionStart = s1;
            this.textbox.selectionEnd = s2;
        } else {
            this.textbox.selectionStart = s2;
            this.textbox.selectionEnd = s1;
        }
    }
}

const text = document.getElementById("text1");
// console.log(text);

let password = document.getElementById("text2");

let DELETE_TYPES = ["deleteContentBackward", "deleteContentForward"];

let prev_value = text.value;

let comp = false;

mtb = new MyTextBox(document.getElementById("text1"));

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

let all_events = getAllEvents(text);
console.log(all_events);

for (const event of all_events) {
    console.log(event);
    text.addEventListener(event, (e) => {
        console.log(event);
        console.log(e);
    });
}
