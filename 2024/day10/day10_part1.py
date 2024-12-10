grid = []
starts = set()
with open("2024/inputs/day10.txt") as file:
    for m, line in enumerate(file):
        grid.append(list(map(int, line.strip())))
        for n, value in enumerate(grid[m]):
            if value == 0:
                starts.add((m, n))
width = len(grid[0])
height = len(grid)

def get_neighbors(m, n):
    neighbors = []
    if m > 0:
        neighbors.append((m - 1, n))
    if m < height - 1:
        neighbors.append((m + 1, n))
    if n > 0:
        neighbors.append((m, n - 1))
    if n < width - 1:
        neighbors.append((m, n + 1))
    return neighbors

def bfs(start):
    visited = set()
    queue = [start]
    while queue:
        m, n = queue.pop(0)
        if grid[m][n] == 9:
            visited_ends.add((m, n))
        visited.add((m, n))
        for neighbor in get_neighbors(m, n):
            if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == grid[m][n] + 1:
                queue.append(neighbor)
        
ans = 0
for start in starts:
    visited_ends = set()
    bfs(start)
    print(visited_ends)
    ans += len(visited_ends)


print(ans)
