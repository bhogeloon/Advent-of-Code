"""
Year 2020, Day 8

Problem description: See https://adventofcode.com/2020/day/8

<Include solution description>

"""

# Imports
from __future__ import annotations
from pprint import pprint


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Instruction:
    '''A boot code instruction'''

    def __init__(self, line: str) -> None:
        (instr_type, instr_value_str) = line.split()
        instr_value_int = int(instr_value_str)

        self.type = instr_type
        self.value = instr_value_int


class BootCode(list[Instruction]):
    '''A list container class of Instruction objects'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Instruction(line))

        # Keep track of the visited instruction indexes
        self.visited = set()
        # Current instruction pointer
        self.ptr = 0
        # Value of accumulator
        self.acc = 0

    def detect_loop(self) -> None:
        '''Run the code until a loop is detected'''
        # Repeat until instruction is already seen
        while self.ptr not in self.visited:
            # Register current pointer
            self.visited.add(self.ptr)

            # If no oprtation, proceed with next one
            if self[self.ptr].type == 'nop':
                self.ptr += 1
            # If acc then update acc
            elif self[self.ptr].type == 'acc':
                self.acc += self[self.ptr].value
                self.ptr += 1
            # If jmp update pointer
            elif self[self.ptr].type == 'jmp':
                self.ptr += self[self.ptr].value
            else:
                raise RuntimeError(
                    "No valid instruction: "
                    f"{self[self.ptr].type} at {self.ptr}"
                )


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    bootcode = BootCode(lines)
    bootcode.detect_loop()

    return bootcode.acc

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
