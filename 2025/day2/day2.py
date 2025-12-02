with open('2025/inputs/day2.txt') as file:
    id_ranges = [line.split('-') for line in file.read().strip().split(',')]
    
ans1 = 0

for l, r in id_ranges:
    len_l = len(l)
    len_r = len(r)
    l = int(l)
    r = int(r)
    
    for length in range(2, len_r + 1, 2):
        k = length // 2
        start = 10 ** (k - 1)
        end = 10 ** k

        for half in range(start, end):
            n = int(str(half) + str(half))
            if n > r:
                break
            if n >= l:
                ans1 += n
print(ans1)
            