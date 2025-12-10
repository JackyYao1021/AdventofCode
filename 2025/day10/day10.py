import re
pattern = r"\[[^\]]*\]|\((?:\d+,)*\d+\)|\{(?:\d+,)*\d+\}"


targets = []
buttons_list = []
valtages = []

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
                botton = 0
                for i in map(int, token.strip("()").split(",")):
                    botton |= 1 << i
                tmp_bottons.append(botton)
            elif token.startswith("{"):
                valtages.append(list(map(int, token.strip("{}").split(","))))
                
        buttons_list.append(tmp_bottons)
    

def bfs(t, bottons):
    states = [0]
    iteration = 0
    while True:
        iteration += 1
        new_states = set()
        for state in states:
            for botton in bottons:
                new_state = state ^ botton
                if new_state == t:
                    return iteration
                else:
                    new_states.add(new_state)
        states = list(new_states)
    
    
ans = 0    

for t, bottons in zip(targets, buttons_list):
    iteration = bfs(t, bottons)
    ans += iteration
print(ans)