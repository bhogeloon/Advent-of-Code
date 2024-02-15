"""
Year 2020, Day 8, Part 2

Problem description: See https://adventofcode.com/2020/day/8

"""

# Imports
from pprint import pprint

# Constants

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class InstructionSet():

    def __init__(self, lines: list[str]) -> None:
        self.instructions = []
        self.jmps = []
        self.nops = []
        self.a = None

        for (i, line) in enumerate(lines):
            (instr_type, instr_value_str) = line.split()
            instr_value_int = int(instr_value_str)

            if instr_type == 'jmp':
                self.jmps.append(i)
            elif instr_type == 'nop':
                self.nops.append(i)

            instruction = {
                'type': instr_type,
                'value': instr_value_int,
            }

            self.instructions.append(instruction)


    def validate(self) -> bool:
        '''Check if this is valid code'''

        steps_visited = set()

        self.a = 0
        i = 0

        while True:
            if i == len(self.instructions):
                return True

            if i < 0 or i > len(self.instructions):
                return False

            if i in steps_visited:
                return False

            steps_visited.add(i)

            if self.instructions[i]['type'] == 'nop':
                i += 1

            elif self.instructions[i]['type'] == 'acc':
                self.a += self.instructions[i]['value']
                i += 1

            elif self.instructions[i]['type'] == 'jmp':
                i += self.instructions[i]['value']

            else:
                raise RuntimeError("No valid instruction: {} at {}".format(
                    self.instructions[i]['type'], i))



# Functions


# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    instr_set = InstructionSet(lines)

    print(instr_set.validate())

    for jmp_i in instr_set.jmps:
        instr_set.instructions[jmp_i]['type'] = 'nop'

        if instr_set.validate():
            return instr_set.a

        instr_set.instructions[jmp_i]['type'] = 'jmp'

    for nop_i in instr_set.nops:
        instr_set.instructions[nop_i]['type'] = 'jmp'

        if instr_set.validate():
            return instr_set.a

        instr_set.instructions[nop_i]['type'] = 'nop'

    return "No valid set found"

    return __name__


if __name__ == '__main__':
    pass