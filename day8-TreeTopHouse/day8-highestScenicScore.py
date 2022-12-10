file = open("day8-input.txt", "r")
lines = file.read().splitlines()

grid = []
for line in lines:
    row = []
    for height in line:
        row.append(int(height))
    grid.append(row)

print(grid)

highest_scenic_score = 0

for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) - 1):
        height = grid[row][col]
        left_score = 1
        right_score = 1
        top_score = 1
        bottom_score =1


        left_trees = grid[row][1: col]
        for tree in left_trees[::-1]:
            if height > tree:
                left_score += 1
            else:
                break

        right_trees = grid[row][col + 1:-1]
        for tree in right_trees:
            if height > tree:
                right_score += 1
            else:
                break

        column = [x[col] for x in grid]
        top_trees = column[1: row]
        for tree in top_trees[::-1]:
            if height > tree:
                top_score += 1
            else:
                break

        bottom_trees = column[row + 1 : -1]
        for tree in bottom_trees:
            if height > tree:
                bottom_score += 1
            else:
                break
        
        scenic_score = top_score * bottom_score * left_score * right_score
        highest_scenic_score= max(scenic_score, highest_scenic_score)

print(highest_scenic_score)