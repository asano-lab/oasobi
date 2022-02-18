let X_NUM = 6;
let Y_NUM = 6;

let BLOCK_OFFSET_X = 1000;
let BLOCK_OFFSET_Y = 1000;

let BLOCK_SIZE_X = 1600;
let BLOCK_SIZE_Y = 1600;

let FONT_SIZE = 800;

let current_coordinates;

let height_max = 3;

let maru;

const re_fill = new RegExp('fill="rgb\\(\\d+,\\d+,\\d+\\)"', "i");
const re_stroke = new RegExp('stroke="rgb\\(\\d+,\\d+,\\d+\\)"', "i");

const main_svg = document.getElementById("main_svg");

const squares = document.getElementsByClassName("squares");

const square_texts = document.getElementsByClassName("square_texts");

function num_to_coordinates(n) {
    return [Math.floor(n / Y_NUM), n % Y_NUM];
}

function is_neighbor(coo) {
    let dx_abs, dy_abs;
    dx_abs = Math.abs(coo[0] - current_coordinates[0]);
    dy_abs = Math.abs(coo[1] - current_coordinates[1]);
    // console.log(dx_abs, dy_abs);
    if (dx_abs > 1 || dy_abs > 1) {
        return false;
    }
    if (dx_abs == dy_abs) {
        return false;
    }
    return true;
}

function move(n) {
    let coo = num_to_coordinates(n);
    if (!is_neighbor(coo)) {
        return;
    }
    current_coordinates = coo;
    console.log(current_coordinates);
    maru.innerHTML = maru.innerHTML.replace(/cx="\d+"/, `cx="${BLOCK_OFFSET_X + BLOCK_SIZE_X * (coo[0] + 0.5)}"`);
}

function init() {
    let x1, y1, x2, y2, xm, ym;
    let sq, sqt;
    current_coordinates = [2, 4];
    main_svg.innerHTML = "";
    for (let i = 0; i < X_NUM; i++) {
        for (let j = 0; j < Y_NUM; j++) {
            x1 = BLOCK_OFFSET_X + BLOCK_SIZE_X * i;
            x2 = x1 + BLOCK_SIZE_X;
            y1 = BLOCK_OFFSET_Y + BLOCK_SIZE_Y * j;
            y2 = y1 + BLOCK_SIZE_Y;
            xm = (x1 + x2) / 2;
            ym = (y1 + y2) / 2;
            main_svg.innerHTML += `<g class="squares"><path fill="rgb(178,178,178)" stroke="rgb(52,101,164)" stroke-width="100" stroke-linejoin="round" d="M ${x1},${y1} L ${x2},${y1} ${x2},${y2} ${x1},${y2} Z"/></g>`;
            if (i == current_coordinates[0] && j == current_coordinates[1]) {
                main_svg.innerHTML +=  `<g id="maru"><circle cx="${xm}" cy="${ym}" r="500" stroke="None" fill="rgb(255,0,0)" stroke-width="5"/></g>`;
            }
            main_svg.innerHTML += `<text x="${xm}" y="${ym + FONT_SIZE / 2 - 100}" font-size="${FONT_SIZE}" stroke="black" text-anchor="middle" stroke-width="0.5" class="square_texts">1</text>`;
        }
    }
    maru = document.getElementById("maru");
    // console.log(main_svg.innerHTML);
    for (let i = 0; i < squares.length; i++) {
        sq = squares[i];
        sqt = square_texts[i];
        // console.log(i.innerHTML.replace(re, "fill=\"rgb(0,255,0)\""));
        sq.innerHTML = sq.innerHTML.replace(re_fill, 'fill="rgb(255,255,255)"');
        sq.innerHTML = sq.innerHTML.replace(re_stroke, 'stroke="rgb(50,50,50)"');
        sq.addEventListener("click", (e) => {
            move(i);
        });
        sqt.addEventListener("click", (e) => {
            move(i);
        });
    }
    console.log(main_svg);
    console.log(square_texts.length);
    console.log(squares.length);
    console.log(maru);
}

document.addEventListener("DOMContentLoaded", init);
