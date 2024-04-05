"""
Year 2016, Day 2

Problem description: See https://adventofcode.com/2016/day/2

The following classes are used:
- Keypad: contains a matrix of the keypad numbers.
- Instruction: contains the direction of the instruction.
- InstructionSet: Contains all the instructions leading to one digit code.
- InstructionSets: Contains all instructionsets to retrieve the total code.
    This class also maintains a class variable keypad which is a Keypad
    object.

For part 1: follow all the instructions and change the InstructionSets.keypad variable
accordingly. At the end of each IntructionSet object: retrieve the current keypad
position.

"""

# Imports
from pprint import pprint
import numpy as np


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Keypad():
    '''This is the keypad containing the numbers 1 to 9 in a matrix form.
    It has addtional attributes cur_x and cur_y to indicate the current position'''
    def __init__(self) -> None:
        self.keys = np.full((3,3), None)
        # Fill the keypad with numbers 1 to 9
        fill_nr = 1
        for y in range(3):
            for x in range(3):
                self.keys[x,y] = fill_nr
                fill_nr += 1

        # Set current key to 5 (middle one)
        self.cur_x = 1
        self.cur_y = 1


    def get_current(self) -> str:
        '''Return the current key in str format'''
        return str(self.keys[self.cur_x, self.cur_y])


class Instruction():
    '''Contains a single instruction (UDLR)'''

    def __init__(self, char: str) -> None:
        self.dir = char


    def process(self) -> None:
        '''Change the current keypad according to direction'''

        keypad = InstructionSets.keypad

        # If up change y if not already 0
        if self.dir == 'U' and keypad.cur_y > 0:
            keypad.cur_y -= 1
        # If down change y if not already 2
        elif self.dir == 'D' and keypad.cur_y < 2:
            keypad.cur_y += 1
        # If left change x if not already 0
        elif self.dir == 'L' and keypad.cur_x > 0:
            keypad.cur_x -= 1
        # If right change x if not already 2
        elif self.dir == 'R' and keypad.cur_x < 2:
            keypad.cur_x += 1


class InstructionSet(list[Instruction]):
    '''Contains a list of Instruction objects which will result in 
    a single digit.'''

    def __init__(self, line: str) -> None:
        for char in line:
            self.append(Instruction(char))


    def get_digit(self) -> str:
        '''Get the digit for this line of instructions'''
        for instr in self:
            instr.process()

        return InstructionSets.keypad.get_current()


class InstructionSets(list[InstructionSet]):
    '''List container class of InstructionSet objects. This will result in
    the bathroom code'''

    keypad = Keypad()

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(InstructionSet(line))


    def get_bathroom_code(self) -> str:
        '''Get the solution to part 1'''
        result = ''

        for instrs in self:
            result += instrs.get_digit()

        return result


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    instrs = InstructionSets(lines)

    return instrs.get_bathroom_code()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
