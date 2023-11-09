// Initialize variables

let GRID_LENGTH = 4;

let grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
];

let score = 0;

// THERE ARE BUGS HERE THAT NEED TO BE FIXED (EX: 2, 2, 2, 8)
function swipe_left() {

    let changed = false;

    for (let i = 0; i < GRID_LENGTH; i++) {

        // Create the new row
        let newRow = [0, 0, 0, 0];

        // Slide each row left (individually)
        for (let addPos = 0, j = 0; j < GRID_LENGTH; j++) {

            // Ignore empty cells
            if (grid[i][j] == 0)
                continue;

            // Slide left
            if (newRow[addPos] == 0)
                newRow[addPos] = grid[i][j];
            else if (newRow[addPos] == newRow[j]) {
                score += (newRow[addPos] += grid[i][j]);
                addPos++;
            }
            else {
                addPos++;
                newRow[i][addPos] = grid[i][j];
            }
        }

        // Determine if anything changed & update the grid
        for (let j = 0; j < GRID_LENGTH; j++) {
            changed = changed || (newRow[j] != grid[i][j]);
            grid[i][j] = newRow[j];
        }
    }

    return changed;
};

// const { BlockList } = require("net");


function swipe(button) {
    if (button = ) {
        if (arr == arr1) {
            return false;
        } else {
            return true;
        }
    };
    // call the swipe[dir] function -> determine if anything changed (return if it did not)

    // generatea random new 2 or 4 in a random empty cell

    // check if gameover
    for (i in grid(i = 0, i++, i < len(grid))) {
        if (grid[i] == 2048) {
            return true;
        }
    };

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
