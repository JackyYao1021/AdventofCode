tasks = []
with open("2024/inputs/day7.txt") as file:
    for line in file:
        result, inputs = line.strip().split(":")
        inputs = list(map(int, inputs.strip().split(" ")))
        result = int(result)
        tasks.append((result, inputs))
    
    
def can_make(result, rest):
    if len(rest) == 1:
        return rest[0] == result

    last = rest[-1]

    if result % last == 0:
        possible_mul = can_make(result // last, rest[:-1])
    else:
        possible_mul = False

    next_power_of_10 = 1
    while next_power_of_10 <= last:
        next_power_of_10 *= 10
    if (result - last) % next_power_of_10 == 0:
        possible_concat = can_make((result - last) // next_power_of_10, rest[:-1])
    else:
        possible_concat = False

    possible_add = can_make(result - last, rest[:-1])
    return possible_mul or possible_add or possible_concat
        
ans = 0
buffer = dict()
for task in tasks:
    buffer = dict()
    result, inputs = task
    ans += result if can_make(result, inputs) else 0
    print(result, inputs)
    
print(ans)
    