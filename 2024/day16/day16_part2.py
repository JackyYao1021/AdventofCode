import sys
import heapq
grid = []

start_point = (0, 0)
end_point = (0, 0)
with open("2024/inputs/day16.txt") as file:
    for m, line in enumerate(file):
        grid.append(list(line.strip()))
        if "S" in line:
            start_point = (m, line.index("S"))
        if "E" in line:
            end_point = (m, line.index("E"))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

print(start_point, end_point)

visited = {}
pq = []

direction = 0
tiles = {}
min_cost = sys.maxsize
heapq.heappush(pq, (0, start_point[0], start_point[1], direction, []))


while pq:
    cost, m, n, direction, path = heapq.heappop(pq)
    if (m, n) == end_point:
        if cost <= min_cost:
            min_cost = cost
            if min_cost not in tiles:
                tiles[min_cost] = set()
            tiles[min_cost].update(path)
        continue
    
    if (m, n, direction) in visited and visited[m, n, direction] < cost:
        continue
    visited[m, n, direction] = cost
    for i in range(-1,2):
        new_direction = (direction + i) % 4
        new_m = m + directions[new_direction][0]
        new_n = n + directions[new_direction][1]
        if 0 <= new_m < len(grid) and 0 <= new_n < len(grid[0]) and grid[new_m][new_n] != "#":
            new_cost = cost + 1
            if direction != new_direction:
                new_cost += 1000
            
            heapq.heappush(pq, (new_cost, new_m, new_n, new_direction, path + [(m, n)]))

# print(tiles)

print(len(tiles[min_cost])+1)



