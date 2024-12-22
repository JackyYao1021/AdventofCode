
def secure_number(number):
    for i in range(2000):
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
    

ans = 0

with open("2024/inputs/day22.txt") as file:
    for line in file:
        number = int(line)
        ans += secure_number(number)
        
print(ans)