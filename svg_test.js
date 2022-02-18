const X_NUM = 4;
const Y_NUM = 3;

let BLOCK_OFFSET_X = 3400;
let BLOCK_OFFSET_Y = 3400;

let BLOCK_SIZE_X = 2600;
let BLOCK_SIZE_Y = 3600;

function init() {
    for (const i of squares) {
        // console.log(i.innerHTML.replace(re, "fill=\"rgb(0,255,0)\""));
        i.innerHTML = i.innerHTML.replace(re, "fill=\"rgb(255,255,0)\"");
        console.log(i.innerHTML);
        console.log(i);
    }
    console.log(squares.length);
}

e1 = document.getElementsByClassName("com.sun.star.drawing.CustomShape");

let re = new RegExp("fill=\"rgb\\(\\d+,\\d+,\\d+\\)\"", "i");

const squares = document.getElementsByClassName("squares");

document.addEventListener("DOMContentLoaded", init);
