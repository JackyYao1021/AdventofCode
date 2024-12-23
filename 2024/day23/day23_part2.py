from itertools import combinations
connections = {}
with open("2024/inputs/day23.txt") as file:
    for line in file:
        computer_A, computer_B = line.strip().split("-")
        if computer_A not in connections:
            connections[computer_A] = []
        if computer_B not in connections:
            connections[computer_B] = []
        connections[computer_A].append(computer_B)
        connections[computer_B].append(computer_A)
        
def check(computers):
    for computer_A, computer_B in combinations(computers, 2):
        if computer_B not in connections[computer_A]:
            return False
    return True

max_nodes = 0
nodes = []
for computer in connections:
    connection = connections[computer]
    for i in range(len(connection), 1, -1):
        if i <= max_nodes-1:
            break
        for computers in combinations(connection, i):
            if check(computers):
                max_nodes = i+1
                nodes = list(computers)+[computer]
                
sorted_nodes = sorted(nodes)
ans = ""
for node in sorted_nodes:
    ans += node + ","
    
print(ans[:-1])
        