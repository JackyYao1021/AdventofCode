import re

ROBOT_PATTERN = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')


robots = []
with open("2024/inputs/day14.txt") as file:
    for line in file:
        line = line.rstrip()
        x, y, vx, vy = map(int,(ROBOT_PATTERN.search(line).groups()))
        robots.append((x, y, vx, vy))
    
top_left = 0
top_right = 0
bottom_left = 0
bottom_right = 0
        
width = 101
height = 103


for robot in robots:
    x, y, vx, vy = robot
    x_f = (x + vx*seconds) % width
    y_f = (y + vy*seconds) % height
    if x_f < width//2 and y_f < height//2:
        top_left += 1
    elif x_f > width//2 and y_f < height//2:
        top_right += 1
    elif x_f < width//2 and y_f > height//2:
        bottom_left += 1
    elif x_f > width//2 and y_f > height//2:
        bottom_right += 1
# print(top_left, top_right, bottom_left, bottom_right)
print(top_left*top_right*bottom_left*bottom_right)
        
                      
        
    
    