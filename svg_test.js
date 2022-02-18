const X_NUM = 4;
const Y_NUM = 3;


e1 = document.getElementsByClassName("com.sun.star.drawing.CustomShape");

let re = new RegExp("fill=\"rgb\\(\\d+,\\d+,\\d+\\)\"", "i");

const squares = document.getElementsByClassName("squares");

console.log(squares.length)

for (const i of squares) {
    // console.log(i.innerHTML.replace(re, "fill=\"rgb(0,255,0)\""));
    i.innerHTML = i.innerHTML.replace(re, "fill=\"rgb(0,255,0)\"");
    console.log(i.innerHTML);
    console.log(i);
}
