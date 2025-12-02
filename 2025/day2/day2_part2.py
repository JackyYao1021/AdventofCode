with open('2025/inputs/day2.txt') as file:
    id_ranges = [line.split('-') for line in file.read().strip().split(',')]
    
ans2 = 0
visited = set()
for l, r in id_ranges:
    len_l = len(l)
    len_r = len(r)
    l = int(l)
    r = int(r)
    
    for length in range(len_l, len_r + 1):
        for i in range(1, length // 2 + 1):
            if length % i == 0:
                k = length // i
                start = 10 ** (i - 1)
                end = 10 ** i
                
                for fst in range(start, end):
                    pattern = str(fst) * k
                    n = int(pattern)
                    if n > r:
                        break
                    if n >= l and n not in visited:
                        visited.add(n)
                        ans2 += n

print(ans2)
# print(visited)
            