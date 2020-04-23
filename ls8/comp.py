import sys

# Write a program in python that runs programs

# Parse the command line
# print(sys.argv)
# sys.exit()
program_filename = sys.argv[1]
# print(program_filename)
# sys.exit()

# OP CODES ARE LIKE INSTRUCTIONS

PRINT_BEEJ = 1
HALT = 2
SAVE_REG = 3 # Store a value in a register (in LS8 called LDI)
PRINT_REG = 4 # Corresponds with PRN in the LS8
PUSH = 5
POP = 6
CALL = 7
RETURN = 8
#^^^
#Global Variables - change only in one place

#Memory uses a list
"""
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
"""

memory = [0] * 256
register = [0] * 8 # like variables but named the same R0-R7 ([0] * 8 means it returns 8 zeros)(stores values)

# R7 is the SP
SP = 7 # change all registers to SP to make it cleaner
register[7] = 0xF4
# Load program into memory
address = 0

with open(program_filename) as f:  # opens file
    for line in f: # reads file line by line
        # try:
        # print(line, end='')  # prints line by line and gets rid of extra lines (end='' prints %)
        line = line.split('#') #line = int(line) # turns the line into int instead of string, line = int(line, 2) 2 means is added for binary
        line = line[0].strip()
        # except ValueError:
        if line[0] == '':
            continue
        memory[address] = int(line[0]) #turns the line into int instead of string store the address in memory

        address +=1 #add one and goes to the next
# sys.exit()

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
    #figure out what the instruction length instead of hardcoding
    #instruction_len = FOR PROJECT
    if instruction == PRINT_BEEJ:
        print('Beej') #add not print (1:45)
        pc += 1

    elif instruction == SAVE_REG: #take the value 37 (read)
        register_num = memory[pc + 1]
        value = memory[pc + 2]
        register[register_num] = value
        pc += 3 # uses three 
        
    elif instruction == PRINT_REG: # ()
        register_num= memory[pc + 1]
        value= register[register_num]
        print(value)
        pc += 2 # uses two
    
    elif instruction == PUSH: # PUSH R2 
        #decrement the stack pointer
        register[7] -= 1 # address_of_top_of_the_stack -= 1

        #copy value from register into memory
        register_num= memory[pc + 1]
        value= register[register_num] # this is what i want to push

        address = register[7] # index into memory
        memory[address]= value # stores the value on the stack
        pc += 2
    
    elif instruction == CALL:
        #compute  return address
        return_address = pc + 2
        #push just the value only

        #push on the stack
        register[SP] -= 1
        memory[register[SP]] = return_address

        # Set the PC to the value in the given register
        register_num = memory[pc + 1]
        destination_address = register[register_num]

        pc = destination_address
    
    elif instruction == RETURN:
        # pop return address from top of the stack
        return_address = memory[register[SP]]
        register[SP] += 1

        #set the pc
        pc = return_address
        #can use auto call increment or not

    elif instruction == HALT:
        running = False
    
    else:
        print('Unknown instruction')
        running = False
    #pc += instruction_len