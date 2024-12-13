import re

BUTTON_PATTERN = re.compile(r'Button \w: X\+(\d+), Y\+(\d+)')
PRIZE_PATTERN = re.compile(r'Prize: X=(\d+), Y=(\d+)')

settings = []
with open("2024/inputs/day13.txt") as file:
    # Read the first line
    blocks = file.read().split('\n\n')
    for block in blocks:
        lines = block.split('\n')
        ax, ay = BUTTON_PATTERN.search(lines[0]).groups()
        bx, by = BUTTON_PATTERN.search(lines[1]).groups()
        px, py = PRIZE_PATTERN.search(lines[2]).groups()
        settings.append(tuple(map(int, (ax, ay, bx, by, px, py))))


dp = [[-1 for _ in range(100)] for _ in range(100)]

def find_minimum(ax, ay, bx, by, px, py):
    best_result = 0
    for a in range(100):
        for b in range(100):
            if a*ax + b*bx > px or a*ay + b*by > py:
                break
            if a * ax + b * bx == px and a * ay + b * by == py:
                best_result = max(best_result, 3*a + b)
    return best_result
                
ans = 0

for setting in settings:
    ax, ay, bx, by, px, py = setting
    ans += find_minimum(ax, ay, bx, by, px, py)
print(ans)
    
    

    
    
    # button_As.append(line)
    # Read the second line