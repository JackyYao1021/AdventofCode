from collections import defaultdict

spliters = []
start = 0
with open("2025/inputs/day7.txt") as file:
    for line in file:
        data = line.strip()
        spliters_in_line = set()
        for i, a in enumerate(data):
            if a == "S":
                start = i
            elif a == "^":
                spliters_in_line.add(i)
        spliters.append(spliters_in_line)
     
tachyon_beams = set()
tachyon_beams.add(start)
mem = defaultdict(int)
mem[start] = 1
for spliters_in_line in spliters:
    new_beams = set()
    new_mem = defaultdict(int)
    for beam in list(tachyon_beams):
        if beam in spliters_in_line:
            new_beams.add(beam - 1)
            new_beams.add(beam + 1)
            new_mem[beam - 1] += mem[beam]
            new_mem[beam + 1] += mem[beam]
            new_mem[beam] = 0
        else:
            new_beams.add(beam)
            new_mem[beam] += mem[beam]
    mem = new_mem
    tachyon_beams = new_beams
    
print(sum(mem.values()))
    
            