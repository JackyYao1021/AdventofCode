data = []
with open("2025/inputs/day6.txt") as file:
    for line in file:
        data.append(line.rstrip("\n"))

print(data)
operators = list(data[-1].split())
op_idx = len(operators) - 1
data = data[:-1]
N = len(data)
d = len(data[0])

tmp = []
ans2 = 0
for i in range(d-1, -1, -1):
    number = [data[j][i] for j in range(N)]
    number = "".join(number).strip()
    
    if number == "":
        op = operators[op_idx]
        
        if op == "*":
            tmp_number = 1
            for num in tmp:
                tmp_number *= int(num)
        else:
            tmp_number = 0
            for num in tmp:
                tmp_number += int(num)
                
        ans2 += tmp_number
        tmp = []
        op_idx -= 1
    else:
        tmp.append(int(number))

#final operation
op = operators[op_idx]
if op == "*":
    tmp_number = 1
    for num in tmp:
        tmp_number *= int(num)
else:
    tmp_number = 0
    for num in tmp:
        tmp_number += int(num)

ans2 += tmp_number

print(ans2)
    