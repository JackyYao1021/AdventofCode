keys = []
locks = []
with open("2024/inputs/day25.txt") as file:
    blocks = file.read().strip().split("\n\n")
    for block in blocks:    
        columns = list(zip(*block.split("\n")))
            
        values = [column.count("#") - 1 for column in columns]

        if block[0] == "#":
            locks.append(values)
        else:
            keys.append(values)

def fits(key, lock):
    return all(a+b<=5 for a,b in zip(key, lock))

ans = 0
for key in keys:
    for lock in locks:
        ans += fits(key, lock)
print(ans)
        
    