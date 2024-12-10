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

mem = [[-1] * width for _ in range(height)]

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

def dfs(m, n):
    if mem[m][n] != -1:
        return mem[m][n]
    if grid[m][n] == 9:
        mem[m][n] = 1
        return 1
    ans = 0
    for neighbor in get_neighbors(m, n):
        if grid[neighbor[0]][neighbor[1]] == grid[m][n] + 1:
            ans += dfs(neighbor[0], neighbor[1])
    mem[m][n] = ans
    return ans

ans = 0
for start in starts:
    ans += dfs(start[0], start[1])
print(ans)