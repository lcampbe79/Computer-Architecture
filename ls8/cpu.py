"""CPU functionality."""

import sys

program_filename = sys.argv[1]
# print(program_filename)
# sys.exit()
# print(sys.argv)
# sys.exit()

'''
LDI ==  Load immediately,
        Store a value in the register <int>,
        OR set this register to this value

PRN ==  pseudo-instruction that prints the numeric value store in a register

HLT ==  stops the CPU and exits the emulator

Internal Registers are:
PC: Program Counter, address of the currently executing instruction

IR: Instruction Register, contains a copy of the currently executing instruction

MAR: Memory Address Register, holds the memory address we're reading or writing

MDR: Memory Data Register, holds the value to write or the value just read

FL: holds the current flags status. These flags can change based on the operands given to the CMP   opcode.

The register is made up of 8 bits. If a particular bit is set, that flag is "true".

FL bits: 00000LGE

L Less-than: during a CMP, set to 1 if registerA is less than registerB, zero otherwise.
G Greater-than: during a CMP, set to 1 if registerA is greater than registerB, zero otherwise.
E Equal: during a CMP, set to 1 if registerA is equal to registerB, zero otherwise.
'''

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        '''
        Add list properties to the CPU class to hold 256 bytes of memory and 8 general-purpose registers. (register = [0] * 8)

        Add properties for any internal registers you need, e.g. PC (is this the same as "address"?)
        '''
        # Create memory
        self.ram =  [0] * 256 # length and the index will stop at 255
        # I think add lines 27 (register), 28 (pc) and 29 (running) from comp.py
        self.reg = [0] * 8  # returns 8 zeros and stores values (0-7)
        self.pc = 0 # Program counter, the index (address) of the current instruction
        self.running = True
        self.LDI = 0b10000010
        self.PRN = 0b01000111
        self.HLT = 0b00000001

    def load(self):
        """Load a program into memory."""
        address = 0
        with open(program_filename) as f:  # opens file
            for line in f: # reads file line by line
                # try:
                # print(line, end='')  # prints line by line and gets rid of extra lines (end='' prints %)
                line = line.split('#', 2) #line = int(line) # turns the line into int instead of string, line = int(line, 2) 2 means is added for binary
                line = line[0].strip() #list
                # except ValueError:
                if line == '':
                    continue
                self.ram[address] = int(line, 2) #turns the line into int instead of string store the address in memory

                address +=1 #add one and goes to the next
        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000, # R0 operand
        #     0b00001000, # 8 (will be += 3)

        #     0b01000111, # PRN R0
        #     0b00000000, # R0 (will be += 2)

        #     0b00000001, # HLT (running = False)
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     # print(self.ram)
        #     address += 1

    

    def alu(self, op, reg_a, reg_b):
        """ALU operations. does math"""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
    '''
    There are two internal registers used for memory operations: 
    Memory Address Register (MAR) and the Memory Data Register (MDR). 
    
    MAR contains the address that is being read or written to. 
    ram_read() should accept the address (MAR) to read and return the value stored there. (Maybe something like: 
        register_num= memory[pc + 1]
        value= register[register_num] 
    from comp.py in the while loop    
    )
    

    MDR contains the data that was read or the data to write. 
    ram_write() should accept a value(MDR) to write, and the address (MAR) to write it to.

    You don't need to add the MAR or MDR to your CPU class, but they would make handy parameter names for ram_read() and ram_write()
    '''
    # MAR contains the address that is being read or written to. 
    #ram_read() should accept the address (MAR) to read and return the value stored #there.
    def ram_read(self, MAR):
        return self.ram[MAR]
    
    # MDR contains the data that was read or the data to write. 
    # ram_write() should accept a value(MDR) to write, and the address (MAR) to write it to.

    def ram_write(self, MDR, MAR):
        self.ram[MAR] = MDR

    def run(self):
        """Run the CPU."""
        '''
        Reads the memory address that's stored in register PC, and store that result in IR, the Instruction Register. This can just be a local variable in run()

        Some instructions requires up to the next two bytes of data after the PC in memory to perform operations on. Sometimes the byte value is a register number, other times it's a constant value (in the case of LDI)(declare value = program[pc + ?]). 
        
        Using ram_read(), read the bytes at PC+1 and PC+2 from RAM into variables operand_a and operand_b in case the instruction needs them

        Then, depending on the value of the opcode, perform the actions needed for the instruction per the LS-8 spec. Maybe an if-elif cascade...? There are other options, too.

        After running code for any particular instruction, the PC needs to be updated to point to the next instruction for the next iteration of the loop in run(). The number of bytes an instruction uses can be determined from the two high bits (bits 6-7) of the instruction opcode. See the LS-8 spec for details.

        In run() in your switch, exit the loop if a HLT instruction is encountered, regardless of whether or not there are more lines of code in the LS-8 program you loaded.
        '''
        # Program counter, the index (address) of the current instruction
        # Reads the memory address that's stored in register
        PC = self.pc 
        # Figures out the instruction length to make the while loop more readable
        #instruction_length = ???
        while self.running:
            
            # Stores the result in "Instruction Register" from the memory (RAM) address in PC
            IR = self.ram[PC]

            # `LDI` instruction (EX: SAVE_REG in comp.py)
            if IR == self.LDI:
                register_num = self.ram_read(PC + 1)
                value = self.ram_read(PC + 2)
                self.reg[register_num] = value
                PC += 3
            
            #`PRN` instruction (EX: PRINT_REG in comp.py)
            elif IR == self.PRN:
                register_num = self.ram_read(PC + 1)
                value = self.reg[register_num]
                print(value)
                PC += 2
              
            
            #`HLT` instruction (EX: HALT in comp.py)
            elif IR == self.HLT:
                self.running = False
            
            #ELSE STATEMENT from comp.py
            else:
                print('Unknown instruction')
                self.running = False
            #PC = 
        # self.trace()
