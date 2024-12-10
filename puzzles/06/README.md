# Part 1

## Approach

For some reason I feel like going a little OOP on this one.

### OOP design

#### Guard
static property: direction_list, a tuple of (dx, dy) pairs representing the four directions up, right, down, and left (in that order)
instance properties: lab_grid, direction, pos_x, pos_y
instance methods: turn, walk

`walk` means the guard adds to her `pos_x` and `pos_y` coordinates according to her current `direction`. It should also mark the previous position as "visited".

`turn` means the guard's direction changes to the next index of the direction tuple.

#### LabArea
instance properties: grid, rows, cols
instance methods: mark_visited, visited, out_of_bounds

### Input parsing

Parsing the lines of the input file into a 2D grid is straightforward. But another thing we have to do is find the starting position.

- For each line read, search for the `^` character
- If it's found, record the index it was found as the starting column, and the current row in the grid as the row