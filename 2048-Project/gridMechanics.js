// Initialize variables

let grid = [[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]];

let score = 0;




function swipeleft() {

    for (let i = 0; i < length(array); i++) {

        // Slide each row left (individually)
        for (let addPos = 0, j = 0; j < length(array[i]); j++) {

            // Set up
            if (array[i][j] == 0)
                continue;
            let temp = array[i][j];
            array[i][j] = 0;

            // Slide left
            if (array[i][addPos] == 0)
                array[i][addPos] = temp;
            else if (array[i][addPos] == array[i][j]) {
                score += (array[i][addPos] += temp);
                addPos++;
            }
            else {
                addPos++;
                array[i][addPos] = temp;
            }
        }
    }

    return true; // when something changes
};



// [0, 2, 2, 2]
// [4, 2, 0, 0]

// array = [[w, x, y, z], [w, x, y, z], [w, x, y, z], [w, x, y, z]]
// for i in array[]{
//     if (w = x) {
//         w = w + x
//     }
//     newarry = [[w, x, y, z], [w, x, y, z], [w, x, y, z], [w, x, y, z]]
//     if (x = y) {
//         x = x + y
//     }
//     newarry = [[w, x, y, z], [w, x, y, z], [w, x, y, z], [w, x, y, z]]
//     if (y = z) {
//         y = y + z
//     }
//     newarry = [[w, x, y, z], [w, x, y, z], [w, x, y, z], [w, x, y, z]]
// }
// newarry = [[w, x, y, z], [w, x, y, z], [w, x, y, z], [w, x, y, z]]


array = newarray

}
// const { BlockList } = require("net");

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


function updatehtml() {// you can't do now
}
