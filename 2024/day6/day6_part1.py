grid = []
start_i = 0
start_j = 0

def count_paths(i, j, grid, direction):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = directions[direction]
    visited = set()
    visited.add((i, j))
    leave = False
    while True:
        i += direction[0]
        j += direction[1]
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            leave = True
            break
        if grid[i][j] == "#":
            break
        visited.add((i, j))
    return visited, i-direction[0], j-direction[1], leave


with open("2024/inputs/day6.txt") as file:
    for line in file:
        grid_line = list(line.strip())
        if '^' in grid_line:
            start_i = len(grid)
            start_j = grid_line.index('^')
        grid.append(grid_line)

total_visited = set()

i = start_i
j = start_j
direction = 0
while True:
    visited, i, j, leave = count_paths(i, j, grid, direction)
    total_visited = total_visited.union(visited)
    direction = (direction + 1) % 4
    if leave:
        break
print(len(total_visited))





    
    