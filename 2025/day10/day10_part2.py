import re
from collections import defaultdict, deque
from z3 import *
pattern = r"\[[^\]]*\]|\((?:\d+,)*\d+\)|\{(?:\d+,)*\d+\}"


targets = []
buttons_list = []
voltages = []

with open("2025/inputs/day10.txt") as file:
    for line in file:
        tokens = re.findall(pattern, line)
        tmp_bottons = []
        for token in tokens:
            if token.startswith("["):
                target = 0
                
                for ch in list(reversed(token.strip("[]"))):
                    target <<= 1
                    if ch == "#":
                        target += 1
                targets.append(target)
            elif token.startswith("("):
                botton = list(map(int, token.strip("()").split(",")))
                tmp_bottons.append(botton)
            elif token.startswith("{"):
                voltage = list(map(int, token.strip("{}").split(",")))
                voltages.append(voltage)
                new_bottons = []
                for botton in tmp_bottons:
                    new_botton = list([0]*len(voltage))
                    for i in botton:
                        new_botton[i] = 1
                    new_bottons.append(tuple(new_botton))
                
        buttons_list.append(new_bottons)
    

def z3_solver(v, buttons):
    d = len(v)
    k = len(buttons)

    solver = Optimize()
    
    xs = [Int(f"x_{i}") for i in range(k)]
    for x in xs:
        solver.add(x >= 0)

    for dim in range(d):
        solver.add(
            sum(xs[i] * buttons[i][dim] for i in range(k)) == v[dim]
        )

    total_steps = sum(xs)
    h = solver.minimize(total_steps)
    
    solver.check()
    model = solver.model()
    return model.evaluate(total_steps).as_long()
    
    
ans = 0    

for v, bottons in zip(voltages, buttons_list):
    iteration = z3_solver(tuple(v), bottons)
    ans += iteration
print(ans)