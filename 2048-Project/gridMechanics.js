const { BlockList } = require("net");

array = [[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]];

var score = 0;

// swipeleft
window.addEventListener("keydown", (event) => { if (event.defaultPrevented) { return; } switch (event.key) { case "ArrowLeft": } });
// swiperight
window.addEventListener("keydown", (event) => { if (event.defaultPrevented) { return; } switch (event.key) { case "ArrowRight": } });
// swipeup
window.addEventListener("keydown", (event) => { if (event.defaultPrevented) { return; } switch (event.key) { case "ArrowUp": } });
// swipedown
window.addEventListener("keydown", (event) => { if (event.defaultPrevented) { return; } switch (event.key) { case "ArrowDown": } });


function after_every_move() {
    // update the score

    // generatea random new 2 or 4 in a random empty cell

    // check if gameover

    // updatehtml() // call this function

}

updatehtml // you can't do now

