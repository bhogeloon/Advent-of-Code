"""
Year 2019, Day 5

Problem description: See https://adventofcode.com/2019/day/5

The same class for day 2 was used as a basis, but with the necessarry 
extenstions.

So, we have again a single class called Intcode, representing the Integer
Code of the computer.
The ptr attribute keeps track of code position.

Part 1:
As input, we have a static value of 1.
The output queue is stored as a list. When the terminating code 99 is read, 
the last value of the output queue is returned.
When processing the current postion, it is first split in the opcode and modes.
Depending on the opcode, we either treat it as an operator (add an multiply),
input or output function. The arguments are gathered either positional or as an
immediate value depending on the mode.

Part 2:
Add the new jump functions as a separate function and the less_than and equal
functions are added as operators.
Then change the input value to 5.

"""

# Imports
from pprint import pprint


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Intcode():
    def __init__(self, line:str, input=1) -> None:
        self.codes = [ int(nr) for nr in line.split(',') ]
        # Indicates where the program is
        self.ptr = 0

        # Any input is will be value 1:
        self.input = input

        # Create output list
        self.output = []


    def fix(self, val1 = 12, val2 = 2) -> None:
        '''Fix the initial values'''
        self.codes[1] = val1
        self.codes[2] = val2


    def run_program(self) -> int:
        '''Run through the program and return diagnostic code'''
        while True:
            # If we detect value 99, end program
            if self.codes[self.ptr] == 99:
                # Return last code on the output queue
                return self.output[-1]

            # Determine opcode and modes
            opcode = self.codes[self.ptr] % 100
            modes = self.codes[self.ptr] // 100

            if opcode == 3:
                self.get_input()
            elif opcode == 4:
                self.store_output(modes)
            elif opcode in (1,2,7,8):
                self.operator(opcode, modes)
            elif opcode in (5,6):
                self.jump(opcode, modes)
            else:
                raise RuntimeError(f'Unkown opcode {opcode}')


    def operator(self, opcode: int, modes: int) -> None:
            '''Perform add or multiply operator'''
            # Determine mode per argument
            mode1 = modes % 10
            mode2 = (modes // 10) % 10

            # Get the arguments and the store location
            arg1 = self.get_value_by_mode(mode1, self.ptr+1)
            arg2 = self.get_value_by_mode(mode2, self.ptr+2)
            store_loc = self.codes[self.ptr+3]

            # If opcode = 1, add the args
            if opcode == 1:
                self.codes[store_loc] = arg1 + arg2
 
            # If opcode = 2, multiply the args
            elif opcode == 2:
                self.codes[store_loc] = arg1 * arg2

            # If opcode = 7
            elif opcode == 7:
                if arg1 < arg2:
                    self.codes[store_loc] = 1
                else:
                    self.codes[store_loc] = 0

            # If opcode = 8
            elif opcode == 8:
                if arg1 == arg2:
                    self.codes[store_loc] = 1
                else:
                    self.codes[store_loc] = 0

            else:
                raise RuntimeError(f"Unknown operator {opcode}.")

            # Jump ahead 4 positions
            self.ptr += 4


    def less_than(self, modes: int) -> None:
        '''Store 1 if less than, otherwise 0'''


    def equal_to(self, modes: int) -> None:
        '''Store 1 if equal, otherwise 0'''


    def get_input(self) -> None:
        '''Get input and store information'''
        store_loc = self.codes[self.ptr+1]
        self.codes[store_loc] = self.input
        self.ptr += 2


    def store_output(self, modes: int) -> None:
        '''Store output in the output queue'''
        mode = modes % 10
        output = self.get_value_by_mode(mode, self.ptr+1)
        self.output.append(output)
        self.ptr += 2


    def jump(self, opcode: int, modes: int) -> None:
        '''Change the ptr'''
        # First check if you need to do something at all by checking first
        # parameter
        mode1 = modes % 10
        action = self.get_value_by_mode(mode1, self.ptr+1)

        # If no action required
        if (
                (opcode == 5 and action == 0) or
                (opcode == 6 and action != 0)
            ):
            self.ptr += 3
            return
        
        # Now determine the new ptr position
        mode2 = (modes // 10) % 10
        self.ptr = self.get_value_by_mode(mode2, self.ptr+2)


    def get_value_by_mode(self, mode: int, index: int) -> int:
        '''Return the positional or immediate value, depending on the mode'''
        if mode == 0:
            return self.codes[self.codes[index]]
        else:
            return self.codes[index]


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    intcode = Intcode(lines[0])

    return intcode.run_program()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    intcode = Intcode(lines[0], input=5)

    return intcode.run_program()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
