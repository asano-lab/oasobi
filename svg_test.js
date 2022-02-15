e1 = document.getElementsByClassName("com.sun.star.drawing.CustomShape");

let re = new RegExp('rgb\(\d+,\d+,\d+\)', "i");

const rect_fill = document.getElementsByClassName("rect_fill");

for (const i of rect_fill) {
    console.log(i);
    console.log(i.outerHTML);
    console.log(i.outerHTML.replace(re, "fill=\"rgb(0,255,0)\""));
}
