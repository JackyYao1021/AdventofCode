from collections import defaultdict

rules = defaultdict(set)
sum = 0

def check_ordered(rule, inputs):
    unvisited = set(inputs)
    for input in inputs:
        required = set(rule[input])
        if len(required.intersection(unvisited)) == 0:
            unvisited.remove(input)
        else:
            return False
    return True


def check_new_rule(rule, inputs):
    visited = list()
    unvisited = set(inputs)
    if check_ordered(rule, inputs) == False:
        while len(unvisited) > 0:
            for input in unvisited:
                required = rule[input]
                if len(required.intersection(unvisited)) == 0:
                    unvisited.remove(input)
                    visited.append(input)
                    break
        return visited[len(visited)//2]
    return 0


with open("2024/inputs/day5.txt") as file:
    for line in file:
        if line.strip() == "":
            break
        from_number, to_number = map(int, line.strip().split("|"))
        
        rules[to_number].add(from_number)
        # print(from_number, to_number)
    for line in file: 
        inputs = list(map(int, line.strip().split(",")))
        sum += check_new_rule(rules, inputs)
        
print(sum)
        
        