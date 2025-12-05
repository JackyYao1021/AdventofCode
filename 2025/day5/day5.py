import re
ingredient_pattern = re.compile(r"(\d+)-(\d+)")
input_ingredients = True
ingradients = []
queries = []
ans1 = 0
with open("2025/inputs/day5.txt") as file:
    for line in file:
        if line == "\n":
            input_ingredients = False
            ingradients.sort(key=lambda x: (x[0], x[1]))
            continue
        if input_ingredients:
            left, right = re.findall(ingredient_pattern, line.strip())[0]
            ingradients.append((int(left), int(right)))
        else:
            queries.append(int(line.strip()))
        

for query in queries:
    for left, right in ingradients:
        if right < query:
            continue
        elif left <= query <= right:
            ans1 += 1
            break
        else:
            break
        
print(ans1)
    