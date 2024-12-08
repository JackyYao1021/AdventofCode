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
        antinodes_a = antenna_1
        while antinodes_a[0] >= 0 and antinodes_a[0] < width and antinodes_a[1] >= 0 and antinodes_a[1] < height:
            antinodes.add(antinodes_a)
            antinodes_a = antinodes_a[0] - (antenna_2[0] - antenna_1[0]), antinodes_a[1] - (antenna_2[1] - antenna_1[1])
        antinodes_b = antenna_2
        while antinodes_b[0] >= 0 and antinodes_b[0] < width and antinodes_b[1] >= 0 and antinodes_b[1] < height:
            antinodes.add(antinodes_b)
            antinodes_b = antinodes_b[0] + (antenna_2[0] - antenna_1[0]), antinodes_b[1] + (antenna_2[1] - antenna_1[1])

print(len(antinodes))

