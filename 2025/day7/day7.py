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
        
ans1 = 0
tachyon_beams = set()
tachyon_beams.add(start)
for spliters_in_line in spliters:
    new_beams = set()
    for beam in list(tachyon_beams):
        if beam in spliters_in_line:
            ans1 += 1
            new_beams.add(beam - 1)
            new_beams.add(beam + 1)
        else:
            new_beams.add(beam)
            
    tachyon_beams = new_beams
    
print(ans1)
    
            