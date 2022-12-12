from collections import deque

file = open("day12-input.txt", "r")
lines = file.read().splitlines()

alphabets = 'abcdefghijklmnopqrstuvwxyz'
grid = []
start=(0,0)
end=(0,0)
for currrent_row, line in enumerate(lines):
    row = list(line)
    if "S" in row:
        start = (currrent_row, row.index("S"))
        row[row.index("S")] = "a"
    if "E" in line:
        end = (currrent_row, row.index("E"))
        row[row.index("E")] = "z"

    grid.append(row)

num_rows = len(grid)
num_cols = len(grid[0])
queue = deque()
queue.appendleft((start[0], start[1], 0))

directions = [[0,1], [0, -1], [1,0], [-1,0]]
visited = set()

while len(queue) != 0:
    coord = queue.pop()
    if (coord[0],coord[1]) in visited: continue
    visited.add((coord[0], coord[1]))

    if (coord[0], coord[1]) == end:
        print(coord[2])
        break

    for dir in directions:
        nr, nc = coord[0] + dir[0], coord[1] + dir[1]

        if 0<= nr< num_rows and 0<= nc< num_cols:

            current_height = alphabets.index(grid[coord[0]][coord[1]])
            neighbour_height = alphabets.index(grid[nr][nc])
            if neighbour_height - current_height <= 1:
                queue.appendleft((nr, nc, coord[2]+1))