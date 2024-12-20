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


# not used
def detect_road(point_A, point_B):
    path = []
    heapq.heappush(path, (0, 0, point_A))
    visited = set()
    while path:
        total, cost, point = heapq.heappop(path)
        visited.add(point)
        m, n = point
        for i in range(4):
            new_m = m + directions[i][0]
            new_n = n + directions[i][1]
            if point_B[0] == new_m and point_B[1] == new_n and cost + 1 <= 20:
                return cost + 1
            if 0 < new_m < len(grid) - 1 and 0 < new_n < len(grid[0]) and grid[new_m][new_n] == "#" and (new_m, new_n) not in visited:
                heapq.heappush(path, (cost + 1 + abs(new_m - point_B[0]) + abs(new_n - point_B[1]), cost + 1, (new_m, new_n)))
    return -1



visited = list(visited)
ans = 0

for i, point_A in enumerate(visited):
    for j in range(i + 1, len(visited)):
        point_B = visited[j]
        manhattan_distance = abs(point_A[0] - point_B[0]) + abs(point_A[1] - point_B[1])
        if manhattan_distance <= 20:
            print(point_A, point_B)
            if abs(cost_grid[point_A[0]][point_A[1]] - cost_grid[point_B[0]][point_B[1]]) - manhattan_distance >= 100:
                ans += 1
                    
print(ans)
            



