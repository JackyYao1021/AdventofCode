with open('2025/inputs/day1.txt') as file:
    rotations = [int(line.strip()[1:]) if line.strip()[0] == 'R' else -int(line.strip()[1:]) 
                 for line in file.readlines()]

pointer = 50
ans1 = 0
ans2 = 0

for r in rotations:
    pointer = (pointer + r) % 100
    if pointer == 0:
        ans1 += 1
    elif r > 0 and pointer < (r % 100):
        ans2 += 1
    elif r < 0 and pointer > 100 - (abs(r) % 100):
        ans2 += 1    
    ans2 += abs(r) // 100
ans2 += ans1
print(ans1)
print(ans2)