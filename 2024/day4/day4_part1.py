def check(n, m, table):
    count = 0
    # check down
    if n <= len(table) - 4:
       if table[n+1][m] == 'M'and table[n+2][m] == 'A' and table[n+3][m] == 'S':
           count += 1
    # check up
    if n >= 3:
        if table[n-1][m] == 'M' and table[n-2][m] == 'A' and table[n-3][m] == 'S':
            count += 1
    # check right
    if m <= len(table[n]) - 4:
        if table[n][m+1] == 'M' and table[n][m+2] == 'A' and table[n][m+3] == 'S':
            count += 1
    # check left
    if m >= 3:
        if table[n][m-1] == 'M' and table[n][m-2] == 'A' and table[n][m-3] == 'S':
            count += 1
    # check down right
    if n <= len(table) - 4 and m <= len(table[n]) - 4:
        if table[n+1][m+1] == 'M' and table[n+2][m+2] == 'A' and table[n+3][m+3] == 'S':
            count += 1
    # check down left
    if n <= len(table) - 4 and m >= 3:
        if table[n+1][m-1] == 'M' and table[n+2][m-2] == 'A' and table[n+3][m-3] == 'S':
            count += 1
    # check up right    
    if n >= 3 and m <= len(table[n]) - 4:        
        if table[n-1][m+1] == 'M' and table[n-2][m+2] == 'A' and table[n-3][m+3] == 'S':
            count += 1
    # check up left
    if n >= 3 and m >= 3:
        if table[n-1][m-1] == 'M' and table[n-2][m-2] == 'A' and table[n-3][m-3] == 'S':
            count += 1
        
    return count


table = []
sum=0
with open("2024/inputs/day4.txt", 'r') as file:
    for line in file:
        table += list(line.strip().split())
    
for n in range(len(table)):
    for m in range(len(table[n])):
        if table[n][m] == 'X':
            sum += check(n, m, table)
            
print(sum)