"""
Year 2021, Day 2

Problem description: See https://adventofcode.com/2021/day/2

The following classes were used:
- Instruction: Instruction to go forward down or up by a certain amount
- Instructions: List container class of Instruction objects.
- Submarine: The submarine which has a horizontal position, a depth and an aim (part 2)

For part 1: Just increase hor_pos and depth according to instructions. Then calculate
product.

For part 2: The aim is introduced and replaces depth in up and down instructions. When
going forward, use amount * aim.
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

class Instruction():
    '''Instruction to go up, down or forward by a certain amount'''
    
    def __init__(self, line: str) -> None:
        (self.dir, amount_str) = line.split()
        self.amount = int(amount_str)


class Instructions(list[Instruction]):
    '''List container class of Instruction objects'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Instruction(line))


class Submarine():
    '''Submarine with a horizontal and depth position'''

    def __init__(self, lines: list[str]) -> None:
        self.hor_pos = 0
        self.depth = 0
        self.aim = 0
        self.instrs = Instructions(lines)


    def move1(self) -> None:
        '''Move according to part 1'''
        for instr in self.instrs:

            if instr.dir == 'forward':
                self.hor_pos += instr.amount
            elif instr.dir == 'up':
                self.depth -= instr.amount
            elif instr.dir == 'down':
                self.depth += instr.amount
            else:
                raise RuntimeError("no valid direction {}".format(instr.dir))


    def move2(self) -> None:
        '''Move according to part 2'''
        for instr in self.instrs:

            if instr.dir == 'forward':
                # Move forward
                self.hor_pos += instr.amount
                # Change depth according to amount and current aim
                self.depth += instr.amount * self.aim
            elif instr.dir == 'up':
                # Change aim
                self.aim -= instr.amount
            elif instr.dir == 'down':
                # Change aim
                self.aim += instr.amount
            else:
                raise RuntimeError("no valid direction {}".format(instr.dir))


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    sub = Submarine(lines)
    sub.move1()

    return sub.hor_pos * sub.depth

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    sub = Submarine(lines)
    sub.move2()

    return sub.hor_pos * sub.depth

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
