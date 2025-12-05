import re
ingredient_pattern = re.compile(r"(\d+)-(\d+)")
input_ingredients = True
ingradients = []
queries = []
ans2 = 0
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

previous_right = -1
for left, right in ingradients:
    if left > previous_right:
        previous_right = right
        ans2 += right - left + 1
    else:
        if right > previous_right:
            ans2 += right - previous_right
            previous_right = right
            
print(ans2)
    