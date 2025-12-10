with open("2025/inputs/day9.txt") as file:
    points = [tuple(map(int, line.strip().split(","))) for line in file]

ans = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        ans = max(ans, (abs(points[i][0] - points[j][0])+1) * (abs(points[i][1] - points[j][1])+1))

print(ans)
    