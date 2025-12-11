import re
pattern = r"(\w+):\s*([\w\s]+)"

connections = {}

with open("2025/inputs/day11.txt") as file:
    for line in file:
        match = re.match(pattern, line)
        key = match.group(1)
        values = match.group(2).split()
        connections[key] = values


def helper(start, end, memo, fft, dac):
    if start == end:
        if fft and dac:
            return 1
        else:
            return 0
        return 1
        
    if (start, fft, dac) in memo:
        return memo[(start, fft, dac)]
    
    count = 0
    for neighbor in connections[start]:
        new_fft = fft
        new_dac = dac
        if neighbor == "fft":
            new_fft = True
        if neighbor == "dac":
            new_dac = True
        
        count += helper(neighbor, end, memo, new_fft, new_dac)
            
    memo[(start, fft, dac)] = count
    return count

memo = {}
print(helper("svr", "out", memo, False, False))
    
