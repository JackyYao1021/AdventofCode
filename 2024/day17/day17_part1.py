import re

register_A = 0
register_B = 0
register_C = 0

program_inputs = []
REGISTER_PARTTERN = re.compile(r"Register (\w+): (\d+)")

with open("2024/inputs/day17.txt") as file:
    for line in file:
        if "Register A" in line:
            register_A = int(REGISTER_PARTTERN.match(line).group(2))
        elif "Register B" in line:
            register_B = int(REGISTER_PARTTERN.match(line).group(2))
        elif "Register C" in line:
            register_C = int(REGISTER_PARTTERN.match(line).group(2))
        elif "Program" in line:
            program_inputs = list(map(int,line.split(":")[1].split(",")))
    
        
pointer = 0            
outputs = []

while pointer < len(program_inputs):
    opcode = program_inputs[pointer]
    operand = program_inputs[pointer+1]
    match opcode:
        case 0:
            # a division
            numerator = register_A
            match operand:
                case 4:
                    denominator = pow(2, register_A)
                case 5:
                    denominator = pow(2, register_B)
                case 6:
                    denominator = pow(2, register_C)
                case _:
                    denominator = pow(2, operand)
            register_A = numerator // denominator
            
        case 1:
            # bxl
            x = register_B
            y = operand
            register_B = x ^ y
        
        case 2:
            #bst
            match operand:
                case 4:
                    register_B = register_A % 8
                case 5:
                    register_B = register_B % 8
                case 6:
                    register_B = register_C % 8
                case _:
                    register_B = operand % 8
          
        case 3:
            # jnz
            if register_A != 0:
                if pointer == operand:
                    pointer += 2
                else:
                    pointer = operand
                continue
            
        case 4:
            #bxc
            register_B = register_B ^ register_C
            
        case 5:
            #out
            match operand:
                case 4:
                    print(register_A % 8)
                    outputs.append(register_A % 8)
                case 5:
                    print(register_B % 8)
                    outputs.append(register_B % 8)
                case 6:
                    print(register_C % 8)
                    outputs.append(register_C % 8)
                case _:
                    print(operand % 8)
                    outputs.append(operand % 8)
            
        case 6:
            #bdv
            numerator = register_A
            match operand:
                case 4:
                    denominator = pow(2, register_A)
                case 5:
                    denominator = pow(2, register_B)
                case 6:
                    denominator = pow(2, register_C)
                case _:
                    denominator = pow(2, operand)
            register_B = numerator // denominator
            
        case 7:
            #cdv
            numerator = register_A
            match operand:
                case 4:
                    denominator = pow(2, register_A)
                case 5:
                    denominator = pow(2, register_B)
                case 6:
                    denominator = pow(2, register_C)
                case _:
                    denominator = pow(2, operand)
            register_C = numerator // denominator
                
    pointer += 2
            
            
print(outputs)
            
                        