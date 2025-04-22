"""
Year 2021, Day 13

Problem description: See https://adventofcode.com/2021/day/13

The following classes were used:
- TransparentPaper: Grid class representing the dots on the tranparent
    paper.
- Instruction: Representing a fold instruction, specifying the direction and
    the x or y axis value.
- Instructions: List container class of Instruction objects.

A fold instruction consists of copying the values of the part below the fold
or right of the fold to the upper or left part. It then also changes the 
actual size of the paper.

For part 1, only a single fold is executed and then the number of dots are
counted.

For part 2, all the fold instructions are executed and the paper is then
represented in string format.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from grid import Grid2D
from input_handling import split_input

# Constants

GRID_SIZE = 1500
GRID_SIZE_TEST = 15


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

class TransparentPaper(Grid2D):
    '''Grid class representing the transparant paper'''
    def __init__(self, dot_lines: list[str]):
        if Gv.test:
            size = GRID_SIZE_TEST
        else:
            size= GRID_SIZE

        super().__init__(
            sizes=(size,size),
            default_value = False,
        )

        # The real_size value indicates the size that needs to be looked at.
        # This will change when folding the paper.
        self.real_size_x = 0
        self.real_size_y = 0
        self.fill_dots(dot_lines)


    def fill_dots(self, dot_lines: list[str]) -> None:
        '''This will fill the grid using the input lines'''
        for dot_line in dot_lines:
            self.fill_dot(dot_line)
        
        return


    def fill_dot(self, dot_line:str) -> None:
        '''This will populate a single dot in the grid'''
        (x,y) = [ int(n) for n in dot_line.split(',')]
        self.grid[x,y] = True

        # Set the real size if necessarry
        if self.real_size_x < x+1:
            self.real_size_x = x+1
        if self.real_size_y < y+1:
            self.real_size_y = y+1


    def __str__(self) -> str:
        '''String representation'''
        result = '\n'

        for y in range(self.real_size_y):
            for x in range(self.real_size_x):
                if self.grid[x,y]:
                    result += '#'
                else:
                    result += '.'
            result += '\n'

        return result
    

    def fold(self, instr: Instruction) -> None:
        '''Fold the paper according to the instruction'''
        if instr.xy == 'x':
            self.x_fold(instr.value)
        else:
            self.y_fold(instr.value)


    def x_fold(self, x_axis: int) -> None:
        '''Fold the paper on the x-axis'''
        pass


    def y_fold(self, y_axis: int) -> None:
        '''Fold the paper on the y-axis'''
        # Go through the new sheet
        for y in range(y_axis):
            for x in range(self.real_size_x):
                # Determine if mirrored y is off the sheet
                mirror_y = (2 * y_axis) - y
                if mirror_y < self.real_size_y:
                    self.grid[x,y] = self.grid[x,y] or self.grid[x,mirror_y]

        # Adjust real size to new size
        self.real_size_y = y_axis


    def x_fold(self, x_axis: int) -> None:
        '''Fold the paper on the y-axis'''
        # Go through the new sheet
        for y in range(self.real_size_y):
            for x in range(x_axis):
                # Determine if mirrored x is off the sheet
                mirror_x = (2 * x_axis) - x
                if mirror_x < self.real_size_x:
                    self.grid[x,y] = self.grid[x,y] or self.grid[mirror_x,y]

        # Adjust real size to new size
        self.real_size_x = x_axis


    def count_dots(self) -> None:
        '''Return the number of dots on the paper'''
        result = 0

        for y in range(self.real_size_y):
            for x in range(self.real_size_x):
                if self.grid[x,y]:
                    result += 1

        return result
    

    def all_folds(self, instrs: Instructions) -> None:
        '''Perform all folds for all instructions'''
        for instr in instrs:
            self.fold(instr)


class Instruction():
    '''Represents a folding instruction'''
    def __init__(self, line:str):
        last_part = line.split()[2]
        (self.xy, value_str) = last_part.split('=')
        self.value = int(value_str)


class Instructions(list[Instruction]):
    '''List container class of Instruction objects'''
    def __init__(self, lines: list[str]):
        for line in lines:
            self.append(Instruction(line))
        
    

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    (dot_lines, instr_lines) = split_input(lines)
    paper = TransparentPaper(dot_lines)
    instrs = Instructions(instr_lines)
    paper.fold(instrs[0])

    return paper.count_dots()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    (dot_lines, instr_lines) = split_input(lines)
    paper = TransparentPaper(dot_lines)
    instrs = Instructions(instr_lines)
    paper.all_folds(instrs)

    return str(paper)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
