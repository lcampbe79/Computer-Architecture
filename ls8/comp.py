# Write a program in python that runs programs

# OP CODES ARE LIKE INSTRUCTIONS

PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3 # Store a value in a register (in LS8 called LDI)
PRINT_REG = 4 # Corresponds with PRN in the LS8
#^^^
#Global Variables - change only in one place

#Memory uses a list
memory = [
    PRINT_BEEJ,

    SAVE_REG,   # Save R0, 37   store 37 in R0  the op code
    0,  #R0     operand("argument")
    37, #37     operand

    PRINT_BEEJ,

    PRINT_REG,  #PRINT_REG R0
    0, #R0

    HALT
]
register = [0] * 8 # like variables but named the same R0-R7 ([0] * 8 means it returns 8 zeros)(stores values)
pc = 0 # Program counter, the index (address) of the current instruction
running = True

# NOT FLEXIBLE
# for v in memory:
#     if v == PRINT_BEEJ:
#         print('Beej')
#     elif v == HALT:
#         break

while running:
    instruction = memory[pc]

    if instruction == PRINT_BEEJ:
        print('Beej') #add not print (1:45)
        pc += 1

    elif instruction == SAVE_REG: #take the value 37 
        register_num = memory[pc + 1]
        value = memory[pc + 2]
        register[register_num] = value
        pc += 3 # uses three 
        
    elif instruction == PRINT_REG:
        register_num= memory[pc + 1]
        value= register[register_num]
        print(value)
        pc += 2 # uses two

    elif instruction == HALT:
        running = False
    
    else:
        print('Unknown instruction')
        running = False