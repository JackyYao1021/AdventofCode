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

# 2,4, 1,6, 7,5, 4,4, 1,7, 0,3, 5,5, 3,0
# bst ^ 7, bxl ^ 6, cdv // 2 << b, bxc b ^ c, bxl ^ 7 , adv 3 , out B, repeat 


# b <- a & 7
# b <- b ^ 6
# c <- a >> b
# b <- b ^ c
# b <- b ^ 7
# a <- a >> 3
# out b
# repeat

def executor(register_A, register_B, register_C, program_inputs):
    pointer = 0
    output_pointer = 0
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
                        shift = register_A
                    case 5:
                        shift = register_B
                    case 6:
                        shift = register_C
                    case _:
                        shift = operand
                register_A = numerator >> shift
                
            case 1:
                # bxl
                x = register_B
                y = operand
                register_B = x ^ y
            
            case 2:
                #bst
                match operand:
                    case 4:
                        register_B = register_A & 7
                    case 5:
                        register_B = register_B & 7
                    case 6:
                        register_B = register_C & 7
                    case _:
                        register_B = operand & 7
            
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
                        output = register_A & 7
                    case 5:
                        output = register_B & 7
                    case 6:
                        output = register_C & 7
                    case _:
                        output = operand & 7
                outputs.append(output)
                # if output != program_inputs[output_pointer]:
                #     return False
                # output_pointer += 1
                
            case 6:
                #bdv
                numerator = register_A
                match operand:
                    case 4:
                        shift = register_A
                    case 5:
                        shift = register_B
                    case 6:
                        shift = register_C
                    case _:
                        shift = operand
                register_B = numerator >> shift
                
            case 7:
                #cdv
                numerator = register_A
                match operand:
                    case 4:
                        shift = register_A
                    case 5:
                        shift = register_B
                    case 6:
                        shift = register_C
                    case _:
                        shift = operand
                register_C = numerator >> shift
                    
        pointer += 2
      
    return outputs
    
register_A = pow(2, 45) 

# Brust force (bad example)


while True:
    outputs = executor(register_A, register_B, register_C, program_inputs)
    if outputs == program_inputs:
        print(register_A)
        break
 
    if register_A > 2**48:
        print("Not found")
        break
            
