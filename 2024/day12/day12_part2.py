garden = []

with open("2024/inputs/day12.txt") as file:
    for line in file:
        garden.append(line.strip())
        
global visited 

visited = [[False for _ in range(len(garden[0]))] for _ in range(len(garden))]


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] 

width = len(garden[0])
height = len(garden)
 



def bfs(m, n):
    horizontal_sides = [[0 for _ in range(width)] for _ in range(height+1)]
    vertical_sides = [[0 for _ in range(height)] for _ in range(width+1)]
    area = 1
    connection = 0
    queue = [(m, n)]
    while queue:
        m, n = queue.pop(0)
        visited[m][n] = True
        
        horizontal_sides[n][m] += 1
        horizontal_sides[n+1][m] += -1
        
        vertical_sides[m][n] += 1 
        vertical_sides[m+1][n] += -1 
                
        if m < height - 1 and garden[m][n] == garden[m+1][n]:
            if not visited[m+1][n]:
                visited[m+1][n] = True
                queue.append((m+1, n))
                area += 1
            
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
    
    sides = 0
    for m in range(width+1):
        for n in range(height):
            if vertical_sides[m][n] != 0:
                if n+1 == height or vertical_sides[m][n+1] != vertical_sides[m][n]:
                    sides += 1                
            
    
    for n in range(height+1):
        for m in range(width):
            if horizontal_sides[n][m]:
                if m+1 == width or horizontal_sides[n][m+1] != horizontal_sides[n][m]:
                    sides += 1
                
    return sides, area

ans = 0

for m, row in enumerate(garden):
    for n, cell in enumerate(row):
        if not visited[m][n]:
            sides, area = bfs(m, n)
            ans += sides * area
            
print(ans)