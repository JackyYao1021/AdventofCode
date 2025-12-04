with open('2025/inputs/day4.txt') as file:
    grid = [list(line.strip()) for line in file]
   
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
roll_positions = set()
removed = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            roll_positions.add((i, j))

def count_rolls(x, y):
    removed = set()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == '@':
                removed.add((nx, ny))
                
    return removed

pre_ans = -1
ans = []


while ans == [] or ans[-1] != 0: 
    positions = roll_positions.copy()
    for i, j in positions:
        near_rolls = count_rolls(i, j)
        if len(near_rolls) < 4:
            removed.add((i, j))
    ans.append(len(removed))
    roll_positions -= removed
    for (x, y) in (removed):
        grid[x][y] = '.'
    removed.clear()
            
print(ans[0])
print(sum(ans))