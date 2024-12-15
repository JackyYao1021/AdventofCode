

grid = []
moves = []
robot_x = 0
robot_y = 0

SAVE_GRID = False

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
    
    
## generate new grid
new_grid = []
for row in grid:
    new_row = []
    for cell in row:
        if cell == "@":
            new_row.append("@")
            new_row.append(".")
        elif cell == "#":
            new_row.append("#")
            new_row.append("#")
        elif cell == ".":
            new_row.append(".")
            new_row.append(".")
        else:
            new_row.append("[")
            new_row.append("]")
    new_grid.append(new_row)
    
grid = new_grid
robot_x = robot_x * 2

if SAVE_GRID:
    save_grid(grid)
    
    
for moves_list in moves:
    for move in moves_list:
        cant_move = False
        if move == "^":
            inflenced_columns = [[robot_x]]
            for y in range(robot_y-1, -1, -1):
                new_inflenced_columns = set()
                all_empty = True
                for inflenced_column in inflenced_columns[-1]:
                    if grid[y][inflenced_column] == "[":
                        new_inflenced_columns.add(inflenced_column)
                        new_inflenced_columns.add(inflenced_column+1)
                        all_empty = False
                    if grid[y][inflenced_column] == "]":
                        new_inflenced_columns.add(inflenced_column)
                        new_inflenced_columns.add(inflenced_column-1)
                        all_empty = False
                    if grid[y][inflenced_column] == "#":    
                        all_empty = False        
                        cant_move = True
                        break
                inflenced_columns.append(list(new_inflenced_columns))
            
                if all_empty:
                    for y_back in range(y, robot_y):
                        for inflenced_column in inflenced_columns[-2+y-y_back]:
                            grid[y_back][inflenced_column] = grid[y_back+1][inflenced_column]
                            grid[y_back+1][inflenced_column] = "."
                    grid[robot_y][robot_x] = "."
                    robot_y -= 1       
                    grid[robot_y][robot_x] = "@"
                    break
                if cant_move:
                    break
            if SAVE_GRID:
                save_grid(grid)
                    
        elif move == "v":
            inflenced_columns = [[robot_x]]
            for y in range(robot_y+1, len(grid)):
                new_inflenced_columns = set()
                all_empty = True
                for inflenced_column in inflenced_columns[-1]:
                    if grid[y][inflenced_column] == "[":
                        new_inflenced_columns.add(inflenced_column)
                        new_inflenced_columns.add(inflenced_column+1)
                        all_empty = False
                    if grid[y][inflenced_column] == "]":
                        new_inflenced_columns.add(inflenced_column)
                        new_inflenced_columns.add(inflenced_column-1)
                        all_empty = False
                    if grid[y][inflenced_column] == "#":    
                        all_empty = False       
                        new_inflenced_columns=set() 
                        cant_move = True
                        break
                    
                inflenced_columns.append(list(new_inflenced_columns))
                
                if all_empty:
                    for y_back in range(y, robot_y, -1):
                        for inflenced_column in inflenced_columns[-2-y+y_back]:
                            grid[y_back][inflenced_column] = grid[y_back-1][inflenced_column]
                            grid[y_back-1][inflenced_column] = "."
                    grid[robot_y][robot_x] = "."
                    robot_y += 1
                    grid[robot_y][robot_x] = "@"
                    break
                if cant_move:
                    break    
            if SAVE_GRID:        
                save_grid(grid)
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
            if SAVE_GRID:
                save_grid(grid)
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
            if SAVE_GRID:
                save_grid(grid)
                
                                    
                            
                
            
    
ans = 0

for m, row in enumerate(grid):
    for n, cell in enumerate(row):
        if cell == "[":
            ans += 100 * m + n
    
print(ans)
    
    



                