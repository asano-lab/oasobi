const X_NUM = 4;
const Y_NUM = 6;

let BLOCK_OFFSET_X = 3400;
let BLOCK_OFFSET_Y = 3400;

let BLOCK_SIZE_X = 2600;
let BLOCK_SIZE_Y = 1600;

let re = new RegExp("fill=\"rgb\\(\\d+,\\d+,\\d+\\)\"", "i");

let main_svg;

const squares = document.getElementsByClassName("squares");
console.log("wasshoi");

function init() {
    console.log("yeah");
    let i, j, x1, y1, x2, y2;
    main_svg = document.getElementById("main_svg")
    console.log(main_svg);
    main_svg.innerHTML = "";
    for (i = 0; i < X_NUM; i++) {
        for (j = 0; j < Y_NUM; j++) {
            x1 = BLOCK_OFFSET_X + BLOCK_SIZE_X * i;
            x2 = x1 + BLOCK_SIZE_X;
            y1 = BLOCK_OFFSET_Y + BLOCK_SIZE_Y * j;
            y2 = y1 + BLOCK_SIZE_Y;
            main_svg.innerHTML += `<g class="squares"><path fill="rgb(178,178,178)" stroke="rgb(52,101,164)" stroke-width="212" stroke-linejoin="round" d="M ${x1},${y1} L ${x2},${y1} ${x2},${y2} ${x1},${y2} Z"/></g>`;
        }
    }
    // console.log(main_svg.innerHTML);
    for (const i of squares) {
        // console.log(i.innerHTML.replace(re, "fill=\"rgb(0,255,0)\""));
        i.innerHTML = i.innerHTML.replace(re, "fill=\"rgb(255,255,0)\"");
        // console.log(i.innerHTML);
        console.log(i);
    }
    console.log(squares.length);
}

document.addEventListener("DOMContentLoaded", init);
