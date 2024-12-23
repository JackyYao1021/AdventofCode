from itertools import combinations
connections = {}
start_with_t = set()
with open("2024/inputs/day23.txt") as file:
    for line in file:
        computer_A, computer_B = line.strip().split("-")
        if computer_A not in connections:
            connections[computer_A] = []
        if computer_B not in connections:
            connections[computer_B] = []
        connections[computer_A].append(computer_B)
        connections[computer_B].append(computer_A)
        if computer_A.startswith("t"):
            start_with_t.add(computer_A)
        if computer_B.startswith("t"):
            start_with_t.add(computer_B)
            
        
def check(computer_A, computer_B):
    if computer_B in connections[computer_A]:
        return True
    return False
    
ans = 0
seen = set()
for computer in start_with_t:
    connection = connections[computer]
    print(computer, connection)
    for computer_A, computer_B in combinations(connection, 2):
        if computer_A in seen or computer_B in seen:
            continue
        ans += check(computer_A, computer_B)
        # print(computer_A, computer_B, computer)
    seen.add(computer)
print(ans)
    
        