// Initialize variables

let GRID_LENGTH = 4;

let grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
];

let score = 0;

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
            else if (newRow[addPos] == grid[i][j]) {
                score += (newRow[addPos] += grid[i][j]);
                addPos++;
            }
            else {
                addPos++;
                newRow[addPos] = grid[i][j];
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

// Handle all swipes with a button input to determine the swipe direction
// Returns 0 if nothing changed, 1 if something changed, 2 if game won, 3 if game lost
function swipe(button) {

    let changed = false;
    if (button == "left") {
        changed = swipe_left();
    } else if (button == "right") {
        changed = swipe_right();
    } else if (button == "up") {
        changed = swipe_up();
    } else if (button == "down") {
        changed = swipe_down();
    } else {
        console.log("Invalid button"); // ERROR CASE
    };
    if (changed == false) {
        return 0; // nothing changed
    }


    // generatea random new 2 or 4 in a random empty cell



    // check if gameover
    for (i in grid(i = 0, i++, i < len(grid))) {
        if (grid[i] == 2048) {
            return 2;
        } else if (changed == true) {

        } else {
            return 0;
        };
    };




    // updatehtml() // call this function

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



function updatehtml() {// you can't do now

}
