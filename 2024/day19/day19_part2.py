from collections import defaultdict

towels = []
designs = []
with open("2024/inputs/day19.txt") as file:
    blocks = file.read().split('\n\n')
    
    line = blocks[0].split('\n')[0]
    towels = list(line.split(', '))
    print(towels)
    for i, line in enumerate(blocks[1].split('\n')):
        designs.append(line)
        
    # print(designs)
    
mem = defaultdict(int)
def check_design(design):
    if design in mem:
        return mem[design]
    for i, towel in enumerate(towels):
        if design == towel:
            mem[design] += 1
        if design.startswith(towel):
            if check_design(design[len(towel):]):
                mem[design] += mem[design[len(towel):]]

    return mem[design]

ans = 0
for design in designs:
    ans += check_design(design)
print(ans)
        