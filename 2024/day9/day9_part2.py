with open('2024/inputs/day9.txt') as file:
    line = file.readline().strip()
    
spaces = []
files = {}

pos = 0
fid = 0
for i, char in enumerate(line):
    x = int(char)
    if i % 2 == 0:
        files[fid] = (x, pos)
        fid += 1
    else:
        if x > 0:
            spaces.append((x, pos))
    pos += x
        
ans = 0

while fid > 0:
    fid -= 1
    file_size, file_pos = files[fid]
    for i, (space_size, space_pos) in enumerate(spaces):
        if space_pos > file_pos:
            spaces = spaces[:i]
            break
        if space_size > file_size:
            files[fid] = (file_size, space_pos)
            spaces[i] = (space_size - file_size, space_pos + file_size)
            break
        if space_size == file_size:
            files[fid] = (file_size, space_pos)
            spaces = spaces[:i] + spaces[i+1:]
            break


for fid, (file_size, file_pos) in files.items():
    for i in range(file_size):
        ans += fid * (file_pos + i)
            

print(ans)
    

