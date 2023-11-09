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