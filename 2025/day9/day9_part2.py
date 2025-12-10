from shapely.geometry import Polygon

with open("2025/inputs/day9.txt") as file:
    points = [tuple(map(int, line.strip().split(","))) for line in file]

polygon_area = Polygon(points)

ans = 0
for x1, y1 in points:
    for x2, y2 in points:
        rectangle = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area <= ans:
            continue
        if polygon_area.contains(rectangle):
            ans = area

print(ans)
    