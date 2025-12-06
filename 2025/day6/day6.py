
data = []
with open("2025/inputs/day6.txt") as file:
    for line in file:
        data.append(list(line.strip().split()))
    
ans1 = 0
N = len(data[0])
d = len(data)
for i in range(N):
    if data[-1][i] == "*":
        tmp = 1
        for j in range(d-1):
            tmp *= int(data[j][i])
    else:
        tmp = 0
        for j in range(d-1):
            tmp += int(data[j][i])
    ans1 += tmp
print(ans1)