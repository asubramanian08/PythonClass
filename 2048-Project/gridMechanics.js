// Initialize variables

let grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
];

let score = 0;




function swipeleft() {

    let changed = false;

    for (let i = 0; i < length(array); i++) {

        // Create the new row
        let newRow = [0, 0, 0, 0];

        // Slide each row left (individually)
        for (let addPos = 0, j = 0; j < length(array[i]); j++) {

            // Ignore empty cells
            if (array[i][j] == 0)
                continue;

            // Slide left
            if (newRow[i][addPos] == 0)
                newRow[i][addPos] = array[i][j];
            else if (newRow[i][addPos] == newRow[i][j]) {
                score += (newRow[i][addPos] += array[i][j]);
                addPos++;
            }
            else {
                addPos++;
                newRow[i][addPos] = array[i][j];
            }
        }

        // Determine if anything changed
        changed = changed || (newRow != array[i]);

        // Update the row
        array[i] = newRow;
    }

    return true;
};

// const { BlockList } = require("net");


function after_every_move() {
    // generatea random new 2 or 4 in a random empty cell

    // check if gameover

    // updatehtml() // call this function

}


// swipeleft
window.addEventListener("keydown", (event) => { if (event.defaultPrevented) { return; } switch (event.key) { case "ArrowLeft": } });
// swiperight
window.addEventListener("keydown", (event) => { if (event.defaultPrevented) { return; } switch (event.key) { case "ArrowRight": } });
// swipeup
window.addEventListener("keydown", (event) => { if (event.defaultPrevented) { return; } switch (event.key) { case "ArrowUp": } });
// swipedown
window.addEventListener("keydown", (event) => { if (event.defaultPrevented) { return; } switch (event.key) { case "ArrowDown": } });



function updatehtml() {// you can't do now

}
