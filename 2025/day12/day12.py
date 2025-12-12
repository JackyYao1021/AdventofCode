with open('2025/inputs/day12.txt') as file:
    in_shapes = True
    shapes = {}
    cur_shape_index = None
    trees = []
    for line in file:
        line = line.strip()
        if in_shapes:
            if cur_shape_index is None:
                if line == '':
                    continue
                cur_shape_index = int(line[:line.index(':')])
                shapes[cur_shape_index] = []
            else:
                shapes[cur_shape_index].append(tuple(line))
                if len(shapes[cur_shape_index]) == 3:
                    cur_shape_index = None
                    if len(shapes) == 6:
                        in_shapes = False
        else:
            if line == '':
                continue
            sp = line.split(':')
            size = tuple(map(int, sp[0].split('x')))
            counts = tuple(map(int, sp[1].strip().split()))
            trees.append((size, counts))




areas = [None] * len(shapes)
for k,v in shapes.items():
    total = 0
    for r in v:
        total += r.count('#')
    areas[k] = total


ans = 0
for size, counts in trees:
    total_size = size[0] * size[1]
    if (total_size // 9) >= sum(counts):
        ans += 1

print(ans)