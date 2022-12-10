file = open("day8-input.txt", "r")
lines = file.read().splitlines()

grid = []
for line in lines:
    row = []
    for height in line:
        row.append(int(height))
    grid.append(row)

print(grid)

visible_trees = 2*len(grid) + 2*len(grid[0]) - 4

for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        height = grid[row][col]

        left_trees = grid[row][: col]
        if all(height > tree for tree in left_trees):
            print(row,col,height,"taller than left")
            visible_trees += 1
            continue

        right_trees = grid[row][col + 1:]
        if all(height > tree for tree in right_trees):
            print(row,col,height,"taller than right")
            visible_trees += 1
            continue

        column = [x[col] for x in grid]
        top_trees = column[: row]
        if all(height > tree for tree in top_trees):
            print(row,col,height,"taller than top")
            visible_trees += 1
            continue

        bottom_trees = column[row + 1 : ]
        if all(height > tree for tree in bottom_trees):
            print(row,col,height,"taller than bottom")

            visible_trees += 1
            continue

print(visible_trees)