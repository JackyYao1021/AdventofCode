import re

WIRE_PARTERN = re.compile(r'(\w+): (\d+)')
CONNECTION_PARTERN = re.compile(r'(\w+) (\w+) (\w+) -> (\w+)')

wires = {}
connections = []

with open("2024/inputs/day24.txt") as file:
    blocks = file.read().split('\n\n')
    
    for wire in blocks[0].split('\n'):
        
        match = WIRE_PARTERN.match(wire)
        wires[match.group(1)] = int(match.group(2))
        
    for connection in blocks[1].split('\n'):
        match = CONNECTION_PARTERN.match(connection)
        if match.group(1) in wires and match.group(3) in wires:
            if match.group(2) == 'AND':
                wires[match.group(4)] = wires[match.group(1)] & wires[match.group(3)]
            elif match.group(2) == 'OR':
                wires[match.group(4)] = wires[match.group(1)] | wires[match.group(3)]
            elif match.group(2) == 'XOR':
                wires[match.group(4)] = wires[match.group(1)] ^ wires[match.group(3)]
        else:
            connections.append((match.group(1), match.group(2), match.group(3), match.group(4)))
    
while connections:
    for connection in connections:
        if connection[0] in wires and connection[2] in wires:
            if connection[1] == 'AND':
                wires[connection[3]] = wires[connection[0]] & wires[connection[2]]
            elif connection[1] == 'OR':
                wires[connection[3]] = wires[connection[0]] | wires[connection[2]]
            elif connection[1] == 'XOR':
                wires[connection[3]] = wires[connection[0]] ^ wires[connection[2]]
            connections.remove(connection)
            
ans = 0

Z_PARTERN = re.compile(r'z(\d+)')

for name, value in wires.items():
    match = Z_PARTERN.match(name)
    # print(name, value)
    if match:
        print(name, value)
        ans += value * pow(2, int(match.group(1)))

print(ans)
    