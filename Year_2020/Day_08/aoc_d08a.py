"""
Year 2020, Day 8, Part 1

Problem description: See https://adventofcode.com/2020/day/8

The following classes are used:
- Instruction: Contains the instruction details (type and value)
- BootCode: List container class of Instruction objects

Part 1: Keep track of the visited indexes in a set and if the index is seen
before, quit the loop and report the value of the acc.
"""

# Imports
from pprint import pprint

# Constants

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

# Functions

def read_instructions(lines: list[str]) -> list[dict]:
    '''Create a list of instructions'''

    instructions = []

    for line in lines:
        (instr_type, instr_value_str) = line.split()
        instr_value_int = int(instr_value_str)

        instruction = {
            'type': instr_type,
            'value': instr_value_int,
        }

        instructions.append(instruction)

    return instructions


# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    instructions = read_instructions(lines)

    steps_visited = set()

    a = 0
    i = 0

    while True:
        if i in steps_visited:
            break

        steps_visited.add(i)

        if instructions[i]['type'] == 'nop':
            i += 1

        elif instructions[i]['type'] == 'acc':
            a += instructions[i]['value']
            i += 1

        elif instructions[i]['type'] == 'jmp':
            i += instructions[i]['value']

        else:
            raise RuntimeError("No valid instruction: {} at {}".format(
                instructions[i]['type'], i))

    return a

    return __name__


if __name__ == '__main__':
    pass