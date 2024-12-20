import heapq

grid = []
start_point = (0, 0)
end_point = (0, 0)
with open("2024/inputs/day20.txt") as file:
    for m, line in enumerate(file):
        grid.append(list(line.strip()))
        if "S" in line:
            start_point = (m, line.index("S"))
        if "E" in line:
            end_point = (m, line.index("E"))
            
cost_grid = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

point = start_point
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cost_grid[point[0]][point[1]] = 0
visited = set()
while point != end_point:
    m, n = point
    for i in range(4):
        new_m = m + directions[i][0]
        new_n = n + directions[i][1]
        if grid[new_m][new_n] != "#" and (new_m, new_n) not in visited:
            visited.add(point)
            cost_grid[new_m][new_n] = cost_grid[m][n] + 1
            point = (new_m, new_n)
            break
visited.add(end_point)
ans = 0

# with open("2024/day20/outputs.txt", "w") as file:
#     for row in cost_grid:
#         for cell in row:
#             file.write(str(cell) + " ")
#         file.write("\n")

for point in visited:
    m, n = point
    for i in range(4):
        wall_m = m + directions[i][0]
        wall_n = n + directions[i][1]
        path_m = m + 2 * directions[i][0]
        path_n = n + 2 * directions[i][1]
        
        if 0 <= path_m < len(grid) and 0 <= path_n < len(grid[0]) and grid[wall_m][wall_n] == "#" and grid[path_m][path_n] != "#":
            if cost_grid[path_m][path_n] - 2 - cost_grid[m][n] >= 100:
                ans += 1
                
                
print(ans)
            



