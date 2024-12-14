import re

ROBOT_PATTERN = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')

width = 101
height = 103
grid = [[set() for _ in range(width)] for _ in range(height)]
robots = []
r_id = 0
with open("2024/inputs/day14.txt") as file:
    for line in file:
        line = line.rstrip()
        x, y, vx, vy = map(int,(ROBOT_PATTERN.search(line).groups()))
        robots.append((x, y, vx, vy))
        
        grid[y][x].add(r_id)
        r_id += 1

seconds = 0

def find_christmas_tree():
    max_continuous = 0
    for row in grid:
        continuous = 0
        for i in range(len(row)):
            if max_continuous >= 6:
                return max_continuous 
            if len(row[i]) == 0:
                max_continuous = max(max_continuous, continuous)
                continuous = 0
                continue
            else:
                continuous += 1
    return max_continuous
        

seconds = 0
while True:
    if find_christmas_tree() >= 8:
        break
    for r_id, robot in enumerate(robots):
        x, y, vx, vy = robot
        grid[y][x].remove(r_id)
        x = (x+vx) % width
        y = (y+vy) % height
        grid[y][x].add(r_id)
        robots[r_id] = (x, y, vx, vy)
    print(seconds)
    seconds += 1
    
print(seconds)
    