"""
Year 2020, Day 8

Problem description: See https://adventofcode.com/2020/day/8

The following classes are used:
- Instruction: Contains the instruction details (type and value)
- BootCode: List container class of Instruction objects

Part 1: Keep track of the visited indexes in a set and if the index is seen
before, quit the loop and report the value of the acc.

Part 2: Go through all the instruction and swap jmp for nop. If a swap has
been done, run the detec_loop function again. If no loop is detected, report
the acc.
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
        '''Run the code until a loop is detected or until the end of the
        program is detected. If a loop is detected or the code runs out its
        index range, the function will return True. If the end is properly
        reached, the function will return False'''
        # Repeat until instruction is already seen
        while True:
            if (
                self.ptr in self.visited or
                self.ptr < 0 or
                self.ptr > len(self)
            ):
                return True
            
            # Return False if the ptr is just past the end
            if self.ptr == len(self):
                return False
            
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
            

    def repair(self) -> None:
        '''Keep swapping nop and jmp instructions until the code does no
        longer contain a loop'''
        for swap_instr in self:
            if swap_instr.type == 'nop':
                # Temporarily change instruction
                swap_instr.type = 'jmp'

                if Gv.test:
                    pprint([ins.type for ins in self])

                # Terminate if no loop
                if not self.detect_loop():
                    return

                # Restore instruction
                swap_instr.type = 'nop'
                # Re_initialise
                self.reset()

            elif swap_instr.type == 'jmp':
                # Temporarily change instruction
                swap_instr.type = 'nop'

                if Gv.test:
                    pprint([ins.type for ins in self])

                # Terminate if no loop
                if not self.detect_loop():
                    return

                # Restore instruction
                swap_instr.type = 'jmp'
                # Re_initialise
                self.reset()

        raise RuntimeError('No valid code found')


    def reset(self) -> None:
        '''Reset to initial values'''
        self.ptr = 0
        self.acc = 0
        self.visited = set()


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

    bootcode = BootCode(lines)
    bootcode.repair()

    return bootcode.acc

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
