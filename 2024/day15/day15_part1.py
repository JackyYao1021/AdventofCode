

grid = []
moves = []
robot_x = 0
robot_y = 0

def save_grid(grid):
    with open("2024/day15/day15_output.txt", "a") as file:
        for row in grid:
            file.write(''.join(row))
            file.write("\n")
        file.write("\n")

with open("2024/inputs/day15.txt") as file:
    blocks = file.read().split('\n\n')
    for m, line in enumerate(blocks[0].split('\n')):
        grid.append(list(line.strip()))
        for n, cell in enumerate(grid[m]):
            if cell == "@":
                robot_x = n
                robot_y = m
    moves = blocks[1].split('\n')
    
for moves_list in moves:
    for move in moves_list:
        if move == "^":
            for y in range(robot_y-1, -1, -1):
                if grid[y][robot_x] == "#":
                    break
                if grid[y][robot_x] == ".":
                    for y_back in range(y, robot_y):
                        grid[y_back][robot_x] = grid[y_back+1][robot_x]
                    grid[robot_y][robot_x] = "."
                    robot_y -= 1
                    break
        elif move == "v":
            for y in range(robot_y+1, len(grid)):
                if grid[y][robot_x] == "#":
                    break
                if grid[y][robot_x] == ".":
                    for y_back in range(y, robot_y, -1):
                        grid[y_back][robot_x] = grid[y_back-1][robot_x]
                    grid[robot_y][robot_x] = "."
                    robot_y += 1
                    break
        elif move == "<":
            for x in range(robot_x-1, -1, -1):
                if grid[robot_y][x] == "#":
                    break
                if grid[robot_y][x] == ".":
                    for x_back in range(x, robot_x):
                        grid[robot_y][x_back] = grid[robot_y][x_back+1]
                    grid[robot_y][robot_x] = "."
                    robot_x -= 1
                    break
        elif move == ">":
            for x in range(robot_x+1, len(grid[0])):
                if grid[robot_y][x] == "#":
                    break
                if grid[robot_y][x] == ".":
                    for x_back in range(x, robot_x, -1):
                        grid[robot_y][x_back] = grid[robot_y][x_back-1]
                    grid[robot_y][robot_x] = "."
                    robot_x += 1
                    break
    
ans = 0

for m, row in enumerate(grid):
    for n, cell in enumerate(row):
        if cell == "O":
            ans += 100 * m + n
    
print(ans)
    
    



                