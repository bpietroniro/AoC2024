class Guard:
    # indices represents row and column changes for up, right, down, and left
    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)

    def __init__(self, direction, row, col, lab_area):
        self.direction = direction
        self.row = row
        self.col = col
        self.lab_area = lab_area

    def walk(self):
        self.lab_area.mark_visited(self.row, self.col)
        self.row += Guard.dr[self.direction]
        self.col += Guard.dc[self.direction]

    def backtrack(self):
        self.row -= Guard.dr[self.direction]
        self.col -= Guard.dc[self.direction]

    def turn(self):
        self.direction = (self.direction + 1) % 4

    def get_pos(self):
        return (self.row, self.col)

    def obstructed(self):
        return self.lab_area.grid[self.row][self.col] == "#"

    def exited(self):
        return self.lab_area.out_of_bounds(self.row, self.col)


class LabArea:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def out_of_bounds(self, row, col):
        return row < 0 or col < 0 or row >= self.rows or col >= self.cols

    def mark_visited(self, row, col):
        self.grid[row][col] = "X"

    def already_visited(self, row, col):
        return self.grid[row][col] == "X"


def parse_input(filename):
    grid = []
    start_pos = []

    with open("../../puzzles/06/" + filename) as f:
        for line in f:
            grid.append(list(line.rstrip()))
            try:
                j = line.index("^")
                i = len(grid) - 1
                start_pos.append(i)
                start_pos.append(j)
            except ValueError:
                continue

    return grid, start_pos


grid, start_pos = parse_input("input.txt")
lab_area = LabArea(grid)
guard = Guard(0, start_pos[0], start_pos[1], lab_area)

total = 0

while not guard.exited():
    if guard.obstructed():
        guard.backtrack()
        guard.turn()
    if not lab_area.already_visited(*guard.get_pos()):
        lab_area.mark_visited(*guard.get_pos())
        total += 1
    guard.walk()

print(total)
# path visualization
# print("\n".join(["".join(row) for row in grid]))
