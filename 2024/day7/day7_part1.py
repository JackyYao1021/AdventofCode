tasks = []
with open("2024/inputs/day7.txt") as file:
    for line in file:
        result, inputs = line.strip().split(":")
        inputs = list(map(int, inputs.strip().split(" ")))
        result = int(result)
        tasks.append((result, inputs))
        print(result, inputs)


def can_make(result, rest):
    if len(rest) == 1:
        return rest[0] == result

    last = rest[-1]

    if result % last == 0:
        possible_mul = can_make(result // last, rest[:-1])
    else:
        possible_mul = False

    possible_add = can_make(result - last, rest[:-1])
    return possible_mul or possible_add
ans = 0

for task in tasks:
    result, inputs = task
    ans += result if can_make(result, inputs) else 0
    
print(ans)
    