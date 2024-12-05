from collections import defaultdict

rules = defaultdict(set)

sum = 0

def check_rule(rule, inputs):
    unvisited = set(inputs)
    for input in inputs:
        required = set(rule[input])
        if len(required.intersection(unvisited)) == 0:
            unvisited.remove(input)
        else:
            return 0
    return inputs[len(inputs)//2]


with open("2024/inputs/day5.txt") as file:
    for line in file:
        if line.strip() == "":
            break
        from_number, to_number = map(int, line.strip().split("|"))
        rules[to_number].add(from_number)
        
    for line in file: 
        inputs = list(map(int, line.strip().split(",")))
        sum += check_rule(rules, inputs)
        
print(sum)
        
        