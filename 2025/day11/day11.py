import re
pattern = r"(\w+):\s*([\w\s]+)"

connections = {}

with open("2025/inputs/day11.txt") as file:
    for line in file:
        match = re.match(pattern, line)
        key = match.group(1)
        values = match.group(2).split()
        connections[key] = values


def helper(start, end, visited):
    if start == end:
        return 1
    count = 0
    for neighbor in connections[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            count += helper(neighbor, end, visited)
            visited.remove(neighbor)
    return count

visited = set()
visited.add("you")
print(helper("you", "out", visited))
    
