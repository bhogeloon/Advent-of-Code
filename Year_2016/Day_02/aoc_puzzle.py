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

For part 2 I made the keypad more generic (varying in size) and I also checked that if the
next key was value 'x' (an non-existing key) the current key value will not change.
At the start, I make a class variable for part 1 and part 2 to make all the functions
work for both parts, without having to create new ones.
"""

# Imports
from pprint import pprint
from collections import deque
from math import sqrt
# Use function in aoc_lib
from grid import Grid2D


# Constants
# The keypad lay out for both parts
KP ={}

KP[1] = '123'
KP[1] += '456'
KP[1] += '789'

KP[2] = 'xx1xx'
KP[2] += 'x234x'
KP[2] += '56789'
KP[2] += 'xABCx'
KP[2] += 'xxDxx'

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Keypad(Grid2D):
    '''This is the keypad containing the numbers 1 to 9 in a matrix form.
    It has addtional attributes cur_x and cur_y to indicate the current position'''
    def __init__(self, part=1) -> None:
        '''Create the initial keypad, based on the solution part'''
        digits = deque(KP[part])

        self.size = int(sqrt(len(digits)))

        super().__init__(
            sizes=(self.size,self.size),
        )

        self.keys = self.grid
        # Fill the keypad with numbers 1 to 9
        fill_nr = 1

        for y in range(self.size):
            for x in range(self.size):
                digit = digits.popleft()
                self.keys[x,y] = digit
                
                # if digit has value 5, set as current
                if digit == '5':
                    self.cur_x = x
                    self.cur_y = y


    def get_current(self) -> str:
        '''Return the current key in str format'''
        return self.keys[self.cur_x, self.cur_y]


class Instruction():
    '''Contains a single instruction (UDLR)'''

    def __init__(self, char: str, part = 1) -> None:
        self.part = part
        self.dir = char


    def process(self) -> None:
        '''Change the current keypad according to direction'''

        keypad = InstructionSets.keypad[self.part]

        # Determine new (candidate) x,y value
        # If up change y if not already 0
        if self.dir == 'U' and keypad.cur_y > 0:
            new_x = keypad.cur_x
            new_y = keypad.cur_y - 1
        # If down change y if not already 2
        elif self.dir == 'D' and keypad.cur_y < keypad.size - 1:
            new_x = keypad.cur_x
            new_y = keypad.cur_y + 1
        # If left change x if not already 0
        elif self.dir == 'L' and keypad.cur_x > 0:
            new_x = keypad.cur_x - 1
            new_y = keypad.cur_y
        # If right change x if not already 2
        elif self.dir == 'R' and keypad.cur_x < keypad.size - 1:
            new_x = keypad.cur_x + 1
            new_y = keypad.cur_y
        # If no match, just continue and don't chane anything
        else:
            return

        # If the new keypad value equals 'x', don't change anything
        # Otherwise change the keypad values
        if keypad.keys[new_x, new_y] != 'x':
            keypad.cur_x = new_x
            keypad.cur_y = new_y


class InstructionSet(list[Instruction]):
    '''Contains a list of Instruction objects which will result in 
    a single digit.'''

    def __init__(self, line: str, part=1) -> None:
        self.part = part

        for char in line:
            self.append(Instruction(char, self.part))


    def get_digit(self) -> str:
        '''Get the digit for this line of instructions'''
        for instr in self:
            instr.process()

        # Return the current keypad value
        return InstructionSets.keypad[self.part].get_current()


class InstructionSets(list[InstructionSet]):
    '''List container class of InstructionSet objects. This will result in
    the bathroom code'''

    # Class variable that contains the keypads for both parts
    keypad = {
        1: Keypad(1),
        2: Keypad(2),
    }

    def __init__(self, lines: list[str], part = 1) -> None:
        self.part = part

        for line in lines:
            self.append(InstructionSet(line, self.part))


    def get_bathroom_code(self) -> str:
        '''Get the solution'''
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

    instrs = InstructionSets(lines, part=2)

    return instrs.get_bathroom_code()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
