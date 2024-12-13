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


ADD = 10000000000000

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_minimum(ax, ay, bx, by, px, py, a_weight, b_weight):
    px += ADD
    py += ADD
    ans = 0
    det = ax*by - ay*bx
    
    if det != 0:
        # if vector a and b are not parallel
        a, da = divmod(px*by-py*bx, det)
        b, db = divmod(py*ax-px*ay, det)
        if da == db == 0:
            return a_weight*a + b_weight*b
    else:       
        # if vector a and b are parallel
        # g = greatest common divisor of ax and bx
        g = gcd(ax, bx) 
        if px % g != 0:
            # no solution
            return 0
        else:
            # if px is divisible by g
            # lcm = least common multiple of ax and bx
            lcm = ax * bx // g
            
            # relation between a and b
            a_n = lcm // ax
            b_n = lcm // bx
            if a_weight * a_n > b_weight*b_n:
                # if a is more expensive than b
                # use b as much as possible
                
                # get the largest number of b and rest
                b, db = divmod(px, bx)
                # if rest is divisible by ax
                if db % ax == 0:
                    
                    a = db // ax
                    return a_weight * a + b_weight * b
                else:
                   for i in range(1, b_n):
                       if (px - i * bx) % ax == 0:
                           a = (px - i * bx) // ax
                           return a_weight * a + b_weight * (b-i)
                       else:
                            return 0
            else:
                a, da = divmod(px, ax)
                if da % bx == 0:
                    b = da // bx
                    return a_weight * a + b_weight*b
                else:
                    for i in range(1, a_n):
                        if (px - i * ax) % bx == 0:
                            b = (px - i * ax) // bx
                            return a_weight * (a-i) + b_weight*b
                        else:
                            return 0
    return 0        
         

                
ans = 0

for setting in settings:
    ax, ay, bx, by, px, py = setting
    ans += find_minimum(ax, ay, bx, by, px, py, 3, 1)
    
print(ans)
    
    

    
    
    # button_As.append(line)
    # Read the second line