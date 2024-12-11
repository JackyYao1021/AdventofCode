stones = []

round = 75

with open("2024/inputs/day11.txt") as file:
    for line in file:
        stones = list(map(int, line.strip().split()))
        
for i in range(round):
    idx = 0
    n_stones = len(stones)
    while idx < n_stones:
        stone = stones[idx]
        if stone == 0:
            stones[idx] = 1
        elif len(str(stones[idx]).strip()) %2 == 0:
            strstone = str(stone)
            new_stone_1 = int(strstone[:len(strstone) // 2])
            new_stone_2 = strstone[len(strstone) // 2:].lstrip("0")
            if new_stone_2 == "":
                new_stone_2 = 0
            else:
                new_stone_2 = int(new_stone_2)
            
            stones = stones[:idx] + [new_stone_1, new_stone_2] + stones[idx+1:]
            n_stones += 1
            idx += 1
        else:
            stones[idx] = stone*2024

        idx += 1
        
print(len(stones))
        