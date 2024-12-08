def parse_input(filename):
    grid = []
    with open("../../puzzles/04/" + filename, encoding="utf-8") as f:
        for line in f:
            grid.append([char for char in line.strip()])
    return grid


def out_of_bounds(i, j, rows, cols):
    return i < 0 or j < 0 or i >= rows or j >= cols


def count_all_occurrences(grid, word):
    directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def backtrack(index, i, j, rows, cols, current_dir):
        nonlocal count

        # pruning
        if out_of_bounds(i, j, rows, cols) or grid[i][j] != word[index]:
            return

        # success
        if index == len(word) - 1:
            count += 1
            return

        # exploration
        backtrack(
            index + 1, i + current_dir[0], j + current_dir[1], rows, cols, current_dir
        )

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                for d in directions:
                    backtrack(0, i, j, rows, cols, d)

    return count


def count_happy_x_occurrences(grid, center, neighbor1, neighbor2):
    rows = len(grid)
    cols = len(grid[0])
    diagonal_checks = ((neighbor1, neighbor2), (neighbor2, neighbor1))
    count = 0

    def meets_happy_x_condition(i, j):
        def makes_downward_diagonal(i, j):
            return (grid[i - 1][j + 1], grid[i + 1][j - 1]) in diagonal_checks

        def makes_upward_diagonal(i, j):
            return (grid[i - 1][j - 1], grid[i + 1][j + 1]) in diagonal_checks

        return (
            i > 0
            and j > 0
            and i < rows - 1
            and j < cols - 1
            and makes_downward_diagonal(i, j)
            and makes_upward_diagonal(i, j)
        )

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == center and meets_happy_x_condition(i, j):
                print(i, j)
                count += 1

    return count


grid = parse_input("input.txt")
print(count_all_occurrences(grid, "XMAS"))
print(count_happy_x_occurrences(grid, "A", "M", "S"))
