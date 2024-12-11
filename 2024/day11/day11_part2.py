stones = []

round = 75

with open("2024/inputs/day11.txt") as file:
    for line in file:
        stones = list(map(int, line.strip().split()))
        
        
mem = {}

def count_result(number, round):
    if (number, round) in mem:
        return mem[(number, round)]
    if round == 0:
        mem[(number, round)] = 1
        return 1
    else:
        if number == 0:
            mem[(number, round)] = count_result(1, round-1)
            return mem[(number, round)]
        elif len(str(number)) % 2 == 0:
            strstone = str(number)
            new_stone_1 = int(strstone[:len(strstone) // 2])
            new_stone_2 = strstone[len(strstone) // 2:].lstrip("0")
            if new_stone_2 == "":
                new_stone_2 = 0
            else:
                new_stone_2 = int(new_stone_2)
            
            mem[(number, round)] = count_result(new_stone_1, round-1) + count_result(new_stone_2, round-1)
            return mem[(number, round)]
        else:
            mem[(number, round)] = count_result(number*2024, round-1)
            return mem[(number, round)]

ans = 0
for stone in stones:
    ans += count_result(stone, round)
    
print(ans)
        