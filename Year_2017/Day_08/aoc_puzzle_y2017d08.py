"""
Year 2017, Day 8

Problem description: See https://adventofcode.com/2017/day/8

The following classes are used:
- Instruction: Represents a single instruction
- Instructions: List container class of Instruction objects. This object
    contains an attribute cpu, which is a dict containing all register values
    (with the register id as key)

Part 1: Use the eval function to test the condition and if True update the
register value.

Part 2: Keep track of the highest register value using a class variable in 
Instructions.
"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
import re

# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False

    # Variable that will be used for holding the logger object
    log = None

    def __init__(self, test: bool, logger: Logger, **kwargs) -> None:
        '''Initialize the global variables'''
        Gv.test = test
        Gv.log = logger


# Classes

class Instruction:
    '''An instruction to change the CPU registers'''
    def __init__(self, line: str, cpu: Cpu) -> None:
        self.cpu = cpu
        pattern = r'([a-z]+) ([incde]+) ([\d-]+) if ([a-z]+) ([!=<>]+) ([\d-]+)'
        m = re.fullmatch(pattern, line)

        if not m:
            raise Exception(f"Could not parse line: {line}")
        
        self.target_reg_id = m.group(1)
        
        # Use negative increment if decrement is specified
        if m.group(2) == 'dec':
            self.inc = -int(m.group(3))
        else:
            self.inc = int(m.group(3))

        self.cond_reg_id = m.group(4)
        self.cmp_op = m.group(5)
        self.cmp_val = int(m.group(6))

        Gv.log.debug(
            f'targetreg: {self.target_reg_id}, inc: {self.inc}, '
            f'condreg: {self.cond_reg_id}, op: {self.cmp_op}, '
            f'cmpval: {self.cmp_val}'
        )

        # Create registers (or overwrite if it exists)
        cpu[self.target_reg_id] = 0
        cpu[self.cond_reg_id] = 0


    def process(self) -> None:
        '''Process this instruction on cpu'''
        # construction evaluation string
        eval_str = f'{self.cpu[self.cond_reg_id]} {self.cmp_op} {self.cmp_val}'

        # Increment register if evaluation is True
        if eval(eval_str):
            self.cpu[self.target_reg_id] += self.inc

            # Update highest value if necessarry
            if self.cpu[self.target_reg_id] > Instructions.highest_regval:
                Instructions.highest_regval = self.cpu[self.target_reg_id]


class Instructions(list[Instruction]):
    '''List container class of Intruction objects'''
    # Class variables
    # Keep track of the highest value ever registered
    highest_regval = 0

    def __init__(self, lines: list[str]) -> None:
        # cpu is a dict containing all register values
        self.cpu = {}

        for line in lines:
            self.append(Instruction(line, self.cpu))


    def process(self) -> None:
        '''Process all instructions on cpu'''
        for instr in self:
            instr.process()


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    instrs = Instructions(lines)
    instrs.process()

    return max(instrs.cpu.values())

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    instrs = Instructions(lines)
    instrs.process()

    return Instructions.highest_regval

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
