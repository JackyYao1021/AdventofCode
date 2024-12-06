grid = []
start_i = 0
start_j = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open("2024/inputs/day6.txt") as file:
    for line in file:
        grid_line = list(line.strip())
        if '^' in grid_line:
            start_i = len(grid)
            start_j = grid_line.index('^')
        grid.append(grid_line)


def check_loop(i, j, new_obstacle_i, new_obstacle_j):
    visited = set()
    direction = 0    
    
    while True:               
        next_i = i + directions[direction][0]
        next_j = j + directions[direction][1]
        if (i, j, direction) in visited:
            return True
        
        if next_i < 0 or next_i >= len(grid) or next_j < 0 or next_j >= len(grid[0]):
            return False
        
        visited.add((i, j, direction))
        if grid[next_i][next_j] == "#" or (next_i == new_obstacle_i and next_j == new_obstacle_j):
            next_direction = (direction + 1) % 4
            direction = next_direction
            continue
        i = next_i
        j = next_j
   
    return False


ans = 0

i = start_i
j = start_j
direction = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(i, j)
        sum += check_loop(start_i, start_j, i, j)
        
print(ans)





    
    