from functools import cache

NUMERIC_KEYPAD = [["7", "8", "9"],
                  ["4", "5", "6"],
                  ["1", "2", "3"],
                  ["_", "0", "A"]]

DIRECTIONAL_KEYPAD = [["_", "^", "A"],
                      ["<", "v", ">"]]


def get_position(key, keypad):
    for m, row in enumerate(keypad):
        for n, k in enumerate(row):
            if k == key:
                return m, n
            
def generate_paths(key1, key2, keypad):
    # generate the path from key1 to key2
    # we want less moves in following steps,
    # so we would better keep in one direction as long as possible
    m1, n1 = get_position(key1, keypad)
    m2, n2 = get_position(key2, keypad)
    m_gap, n_gap = get_position("_", keypad)
    
    m_diff = m2 - m1
    n_diff = n2 - n1
    
    col_moves = (">" if n_diff > 0 else "<") * abs(n_diff)
    row_moves = ("v" if m_diff > 0 else "^") * abs(m_diff)
    
    if m_diff == 0 and n_diff == 0:
        return [""]
    elif m1 == m_gap and n2 == n_gap:
        return [row_moves + col_moves]
    elif m2 == m_gap and n1 == n_gap:
        return [col_moves + row_moves]
    elif m_diff == 0:
        return [col_moves]
    elif n_diff == 0:
        return [row_moves]
    else:
        return [row_moves+col_moves, col_moves+row_moves]
    return [row_moves + col_moves, col_moves + row_moves]

def generate_sequence(codes, keypad):
    # generate the possible sequences from codes
    sequences = []
    # print(codes)
    new = "A" + codes
    for key1, key2 in zip(new, codes):
        # print(key1, key2)
        paths = generate_paths(key1, key2, keypad)
        # print(paths)
        sequences += [[path + "A" for path in paths]]
        # print(sequences)
    return sequences

@cache
def find_shortest_path_length(codes, depth):
    # recursively find the shortest path length
    if depth == 1:
        return len(codes)
    
    if any(code in codes for code in ["<", ">", "^", "v"]):
        keypad = DIRECTIONAL_KEYPAD
    else:
        keypad = NUMERIC_KEYPAD  
    
    ans = 0
    for sequence in generate_sequence(codes, keypad):
        ans += min([find_shortest_path_length(seq, depth-1) for seq in sequence])
            
    return ans

ans = 0
with open("2024/inputs/day21.txt") as file:
    for line in file:
        line = line.strip()
        ans += find_shortest_path_length(line, 27) * int(line.lstrip("0").rstrip("A"))

print(ans)