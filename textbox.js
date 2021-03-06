const VALID_VALUES = ["0", "1"];
const VALID_CODES = [
    "Digit0", "Digit1", "Backspace", "Delete",
    "ArrowLeft", "ArrowRight", "KeyA"
];

class MyTextBox {
    constructor(textbox) {

        this.textbox = textbox;

        // 変数初期化
        this.prev_value = this.textbox.value;
        this.getSelections();
        this.base = this.start;
        this.mdx = 0;
        // カーソル前後の文字列
        this.mae = this.prev_value.slice(0, this.start);
        this.ato = this.prev_value.slice(this.end, this.prev_value.length)

        // keydownイベントの処理
        this.textbox.addEventListener("keydown", (e) => {
    
            if (VALID_CODES.includes(e.code)) {
                this.getSelections();
                // console.log(this.start, this.end);
        
                this.mae = this.prev_value.slice(0, this.start);
                this.ato = this.prev_value.slice(this.end, this.prev_value.length);
        
                // Ctrl
                if (e.ctrlKey) {
                    // 全選択
                    if (e.code == "KeyA") {
                        this.setSelections(0, this.prev_value.length);
                        this.base = 0;
                    }
                }
                // Shift
                else if (e.shiftKey) {
                    if (e.code == "ArrowLeft") {
                        if (this.start == this.end) {
                            this.base = this.start;
                            this.setSelections(this.start - 1, this.base);
                        } else if (this.base < this.end) {
                            this.setSelections(this.base, this.end - 1);
                        } else if (this.start > 0) {
                            this.setSelections(this.start - 1, this.base);
                        }
                    }
                    else if (e.code == "ArrowRight") {
                        if (this.start == this.end) {
                            this.base = this.start;
                            this.setSelections(this.base, this.end + 1);
                        } else if (this.start < this.base) {
                            this.setSelections(this.start + 1, this.base);
                        }
                        else if (this.start < this.prev_value.length) {
                            this.setSelections(this.base, this.end + 1);
                        }
                    }
                }
                else if (e.code == "Digit0") {
                    this.textbox.value = this.mae + "0" + this.ato;
                    this.setSelections(this.start + 1, this.start + 1);
                } else if (e.code == "Digit1") {
                    this.textbox.value = this.mae + "1" + this.ato;
                    this.setSelections(this.start + 1, this.start + 1);
                } else if (e.code == "Backspace") {
                    if (this.start == this.end) {
                        this.textbox.value = this.mae.slice(0, -1) + this.ato;
                        if (this.start > 0) {
                            this.setSelections(this.start - 1, this.start - 1);
                        }
                    } else {
                        this.textbox.value = this.mae + this.ato;
                        this.setSelections(this.start, this.start);
                    }
                } else if (e.code == "Delete") {
                    if (this.start == this.end) {
                        this.textbox.value = this.mae + this.ato.slice(1, this.ato.length);
                    } else {
                        this.textbox.value = this.mae + this.ato;
                    }
                    this.setSelections(this.start, this.start);
                } else if (e.code == "ArrowLeft") {
                    if (this.start != this.end) {
                        this.setSelections(this.start, this.start);
                    } else if (this.start > 0) {
                        this.setSelections(this.start - 1, this.start - 1);
                    }
                } else if (e.code == "ArrowRight") {
                    if (this.start != this.end) {
                        this.setSelections(this.end, this.end);
                    } else if (this.start < this.prev_value.length) {
                        this.setSelections(this.start + 1, this.start + 1);
                    }
                }
                this.getSelections();
                this.prev_value = this.textbox.value;
            }
            // console.log(this.textbox.value.match(/^[01]+$/));
        });

        // 変なタイミングでselectイベントが発生するため無効化
        this.textbox.addEventListener("select", (e) => {
            this.resetSelections();
        });
        
        // valueは元に戻す
        this.textbox.addEventListener("input", (e) => {
            console.log(e);
            // 貼り付け
            if (e.inputType == "insertFromPaste") {
                if (this.textbox.value.match(/^[01]+$/)){
                    this.prev_value = this.textbox.value;
                }
                else {
                    this.textbox.value = this.prev_value;
                    this.resetSelections();
                }
            }
            // 切り取り
            else if (e.inputType == "deleteByCut") {
                this.prev_value = this.textbox.value;
            }
            // 戻す
            else if (e.inputType == "historyUndo") {
                this.prev_value = this.textbox.value;
            }
            else {
                this.resetSelections();
                this.textbox.value = this.prev_value;
            }
        });

        this.textbox.addEventListener("mousedown", (e) => {
            this.mdx = e.offsetX;
        });

        this.textbox.addEventListener("mouseout", (e) => {
            this.getSelections();
            if (this.mdx < e.offsetX) {
                this.base = this.start;
            } else {
                this.base = this.end;
            }
        });

        this.textbox.addEventListener("click", (e) => {
            // console.log(e);
            this.getSelections();
            // シフトが押されていなければbaseも移動
            if (!e.shiftKey) {
                if (this.mdx < e.offsetX) {
                    this.base = this.start;
                } else {
                    this.base = this.end;
                }
            }
        });
        
        this.textbox.addEventListener("dblclick", (e) => {
            this.setSelections(0, this.prev_value.length);
            this.getSelections();
            this.base = 0;
        });

        // 右クリック
        this.textbox.addEventListener("auxclick", (e) => {
            this.getSelections();
        });
    }

    // カーソル位置の取得
    getSelections() {
        this.start = this.textbox.selectionStart;
        this.end = this.textbox.selectionEnd;
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

    // カーソル位置を前の状態に戻す
    resetSelections() {
        this.setSelections(this.start, this.end);
    }
}

const text = document.getElementById("text1");

let password = document.getElementById("text2");

mtb = new MyTextBox(document.getElementById("text1"));

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
// console.log(all_events);

// for (const event of all_events) {
//     console.log(event);
//     text.addEventListener(event, (e) => {
//         console.log(event);
//         console.log(e);
//     });
// }
