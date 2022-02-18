e1 = document.getElementsByClassName("com.sun.star.drawing.CustomShape");

let re = new RegExp("fill=\"rgb\\(\\d+,\\d+,\\d+\\)\"", "i");

const squares = document.getElementsByClassName("squares");

for (const i of squares) {
    console.log(i);
    console.log(i.innerHTML);
    // console.log(i.innerHTML.replace(re, "fill=\"rgb(0,255,0)\""));
    i.innerHTML = i.innerHTML.replace(re, "fill=\"rgb(0,255,0)\"");
    console.log(i.innerHTML);
    console.log(i);
}
