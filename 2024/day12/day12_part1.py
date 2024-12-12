garden = []

with open("2024/inputs/day12.txt") as file:
    for line in file:
        garden.append(line.strip())
        
global visited 

visited = [[False for _ in range(len(garden[0]))] for _ in range(len(garden))]

width = len(garden[0])
height = len(garden)
 

def bfs(m, n):
    area = 1
    connection = 0
    queue = [(m, n)]
    while queue:
        m, n = queue.pop(0)
        visited[m][n] = True
        if m < height - 1 and garden[m][n] == garden[m+1][n]:
            if not visited[m+1][n]:
                visited[m+1][n] = True
                queue.append((m+1, n))
                area += 1
            connection += 1
            
        if n < width - 1 and garden[m][n] == garden[m][n+1]:
            if not visited[m][n+1]:
                visited[m][n+1] = True
                queue.append((m, n+1))
                area += 1
            connection += 1
        if m > 0 and garden[m][n] == garden[m-1][n]:
            if not visited[m-1][n]:
                visited[m-1][n] = True
                queue.append((m-1, n))
                area += 1
            connection += 1
        if n > 0 and garden[m][n] == garden[m][n-1]:
            if not visited[m][n-1]:
                visited[m][n-1] = True
                queue.append((m, n-1))
                area += 1
            connection += 1
        
    return connection//2, area
        
        
ans = 0

for m, row in enumerate(garden):
    for n, cell in enumerate(row):
        if not visited[m][n]:
            connection, area = bfs(m, n)
            ans+= area*(area*4 - connection*2)
            
print(ans)