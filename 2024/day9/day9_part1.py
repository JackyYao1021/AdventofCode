with open('2024/inputs/day9.txt') as file:
    line = file.readline().strip()
    
file_left = 0
file_right = len(line) + len(line)%2
space_left = 1
backword_buffer = 0
backword_buffer_value = 0

ans = 0
count = 0
for i in range(0, len(line)): 
    if file_left == file_right:
        for n in range(backword_buffer):
            ans += count*backword_buffer_value
            count += 1
        break
    if i % 2 == 0:
        for n in range(int(line[file_left])):
            ans += count*(file_left//2)
            count += 1
        file_left += 2
    else:
        space_buffer = int(line[space_left])
        while space_buffer > 0:    
            if backword_buffer == 0:
                file_right -= 2
                backword_buffer = int(line[file_right])
                backword_buffer_value = file_right//2
            ans += count*backword_buffer_value
            count += 1
            space_buffer -= 1
            backword_buffer -= 1
        space_left += 2
print(ans)
            
        
        
            
            
    