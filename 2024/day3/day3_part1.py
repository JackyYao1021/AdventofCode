with open("2024/inputs/day3.txt", 'r') as file:
    lines = file.read() 
    # print(lines)
    
sum = 0

left = 0

while left < len(lines):
    if lines[left:left+4] == "mul(":
        plus_position = -1
        for i in range(4):
            if lines[left+4+1+i] == ",":
                plus_position = left+4+1+i
                break
            
        if plus_position == -1:
            left = left+4+1
            continue
        else:
            right_bracket_position = -1
            for i in range(4):
                if lines[plus_position+1+i] == ")":
                    right_bracket_position = plus_position+1+i
                    break
                
            if right_bracket_position == -1:
                left = plus_position+1
                continue
            
            if lines[left+4:plus_position].isdigit() and lines[plus_position+1:right_bracket_position].isdigit():
                sum += int(lines[left+4:plus_position]) * int(lines[plus_position+1:right_bracket_position])
                left = right_bracket_position+1 
                continue    
    left += 1
    
print(sum)