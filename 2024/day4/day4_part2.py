def check(n, m, table): 
    count = 0
    diagonal = False
    anti_diagonal = False
    
    if table[n+1][m+1] == 'M' and table[n-1][m-1] == 'S' or table[n+1][m+1] == 'S' and table[n-1][m-1] == 'M':
        diagonal = True    
    if table[n-1][m+1] == 'M' and table[n+1][m-1] == 'S' or table[n-1][m+1] == 'S' and table[n+1][m-1] == 'M':
        anti_diagonal = True
    return 1 if diagonal and anti_diagonal else 0

table = []
sum=0

with open("2024/inputs/day4.txt", 'r') as file:
    for line in file:
        table += list(line.strip().split())
        
for n in range(1,len(table)-1):
    for m in range(1,len(table[n])-1):
        if table[n][m] == 'A':
            sum += check(n, m, table)
            
print(sum)