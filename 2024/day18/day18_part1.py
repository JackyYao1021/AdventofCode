import heapq

grid = [["." for _ in range(71)] for _ in range(71)]

with open("2024/inputs/day18.txt") as file:
    for i in range(1024):
        x, y = map(int, file.readline().strip().split(","))
        grid[y][x] = "#"
        
def dijkstra(grid):
    start = (0, 0)
    end = (70, 70)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = {}
    pq = []
    heapq.heappush(pq, (0, start[0], start[1]))
    while pq:
        cost, m, n = heapq.heappop(pq)
        if (m, n) == end:
            return cost
        if (m, n) in visited and visited[m, n] <= cost:
            continue
        visited[m, n] = cost
        for direction in directions:
            new_m = m + direction[0]
            new_n = n + direction[1]
            if 0 <= new_m < len(grid) and 0 <= new_n < len(grid[0]) and grid[new_m][new_n] != "#":
                new_cost = cost + 1
                heapq.heappush(pq, (new_cost, new_m, new_n))
    return -1


    