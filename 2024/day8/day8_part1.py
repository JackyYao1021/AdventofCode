from collections import defaultdict
import itertools
from itertools import combinations

antennas = defaultdict(set)


height = 0
width = 0
with open("2024/inputs/day8.txt") as file:
    y = 0
    for line in file:
        line = line.strip()
        # grid.append(line)
        for x, c in enumerate(line):
            if c != '.':
                antennas[c].add((x,y))
        y+=1
        width = len(line)
    height = y
            
ans = 0
antinodes = set()


for antenna_type in antennas.keys():
    for antenna_1, antenna_2 in combinations(antennas[antenna_type], 2):
        print(antenna_1, antenna_2)
        anticode_a = 2*antenna_1[0] - antenna_2[0], 2*antenna_1[1] - antenna_2[1]
        anticode_b = 2*antenna_2[0] - antenna_1[0], 2*antenna_2[1] - antenna_1[1]
        if anticode_a[0] >= 0 and anticode_a[0] < width and anticode_a[1] >= 0 and anticode_a[1] < height:
            antinodes.add(anticode_a)
        if anticode_b[0] >= 0 and anticode_b[0] < width and anticode_b[1] >= 0 and anticode_b[1] < height:
            antinodes.add(anticode_b)

print(len(antinodes))

