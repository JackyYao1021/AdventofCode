from functools import cache
from collections import Counter

sequence_counter = Counter()

@cache
def get_secure_number(number):
    mask = number << 6
    number = number ^ mask
    number = number % 16777216
    
    mask = number >> 5
    number = number ^ mask
    number = number % 16777216
    
    mask = number << 11
    number = number ^ mask
    number = number % 16777216
    
    return number
    
        
def solve(number):
    mem = []
    last = number % 10
    seen = set()
    for i in range(2000):
        number = get_secure_number(number)
        diff = number % 10 - last
        last = number % 10
        mem.append(diff)
        if len(mem) >= 4:   
            sequence = tuple(mem[-4:]) 
            if sequence not in seen:
                seen.add(sequence)
                sequence_counter[sequence] += last 
    return 0    


with open("2024/inputs/day22.txt") as file:
    for line in file:
        number = int(line)
        solve(number)
    
print(sequence_counter.most_common(1)[0][1])
        