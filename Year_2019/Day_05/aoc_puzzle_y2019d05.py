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


"""

# Imports
from pprint import pprint


# Constants

INPUT = 1


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Intcode():
    def __init__(self, line:str) -> None:
        self.codes = [ int(nr) for nr in line.split(',') ]
        # Indicates where the program is
        self.ptr = 0

        # Any input is will be value 1:
        self.input = INPUT

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
            elif opcode < 3:
                self.operator(opcode, modes)
            else:
                raise RuntimeError(f'Unkown opcode {opcode}')


    def operator(self, opcode, modes) -> None:
            '''Perform add or multiply operator'''
            # Determine mode per argument
            mode1 = modes % 10
            mode2 = (modes // 10) % 10

            # Get the arguments and the store location
            if mode1 == 0:
                arg1 = self.codes[self.codes[self.ptr+1]]
            else:
                arg1 = self.codes[self.ptr+1]

            if mode2 == 0:
                arg2 = self.codes[self.codes[self.ptr+2]]
            else:
                arg2 = self.codes[self.ptr+2]

            store_loc = self.codes[self.ptr+3]

            # If opcode = 1, add the args
            if opcode == 1:
                self.codes[store_loc] = arg1 + arg2
 
            # If opcode = 2, multiply the args
            elif opcode == 2:
                self.codes[store_loc] = arg1 * arg2

            else:
                raise RuntimeError("Unknown operator {}.".format(self.codes[self.ptr]))

            # Jump ahead 4 positions
            self.ptr += 4


    def get_input(self) -> None:
        '''Get input and store information'''
        store_loc = self.codes[self.ptr+1]
        self.codes[store_loc] = self.input
        self.ptr += 2


    def store_output(self, modes) -> None:
        '''Store output in the output queue'''
        mode = modes % 10

        if mode == 0:
            output = self.codes[self.codes[self.ptr+1]]
        else:
            output = self.codes[self.ptr+1]

        self.output.append(output)
        self.ptr += 2


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

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
