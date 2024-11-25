"""
Year 2016, Day 8

Problem description: See https://adventofcode.com/2016/day/8

The following classes are used:
- Screen: Grid class representing the screen LEDs. The content of each field is
    a boolean (True=on, False=off).
- Instruction: contains an instruction to manage the screen.
- Instructions: List container class of Instruction objects.

Part 1: Process the instructions one by one. In case of a 'rotate' function:
- Take a copy of the row/column and assign each new LED contents with the 
    offset of the copy.
At the end count the LEDs which are on.

Part 2: Show a graphical representation of the screen.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from grid import Grid2D


# Constants

GRID_SIZES = (50,6)
GRID_SIZES_TEST = (7,3)


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

class Screen(Grid2D):
    '''Grid class containing booleans (True=on and False=off)'''
    def __init__(self, lines: list[str]) -> None:
        if Gv.test:
            self.x_size, self.y_size = GRID_SIZES_TEST
        else:
            self.x_size, self.y_size = GRID_SIZES

        super().__init__(sizes=(self.x_size,self.y_size), default_value=False)
        self.leds = self.grid
        self.instrs = Instructions(lines)


    def get_nr_of_leds(self) -> int:
        '''Return the number of leds turned on'''
        total = 0

        for led in self.leds.flat:
            if led:
                total += 1

        return total
    

    def process_instrs(self) -> None:
        '''Process the instructions'''
        self.instrs.process(self)


    def image(self) -> str:
        '''Create an image for the screen'''
        line = '\n'
        for y in range(self.y_size):
            for x in range(self.x_size):
                if self.leds[x,y]:
                    line += '#'
                else:
                    line += '.'
            line += '\n'

        return line
    

class Instruction:
    '''An instruction to be performed on the screen'''
    def __init__(self, line:str) -> None:
        words = line.split()

        # If rectangle:
        if words[0] == 'rect':
            self.cmd = 'rect'
            self.rect_x,self.rect_y = [int(nr) for nr in words[1].split('x')]
        else:
            # If shift row
            if words[1] == 'row':
                self.cmd = 'rot_row'
                self.row = int(words[2][2:])
            # If shift column
            else:
                self.cmd = 'rot_col'
                self.col = int(words[2][2:])

            self.amount = int(words[4])


    def process(self, screen: Screen) -> None:
        '''Process this instruction on screen'''
        if self.cmd == 'rect':
            self.rect(screen)
        elif self.cmd == 'rot_row':
            self.rot_row(screen)
        else:
            self.rot_col(screen)


    def rect(self, screen: Screen) -> None:
        '''Execute rect command on screen'''
        for y in range(self.rect_y):
            for x in range(self.rect_x):
                screen.leds[x,y] = True


    def rot_row(self, screen: Screen) -> None:
        '''Execute rotate row command on screen'''
        old_row = screen.leds[:,self.row].copy()

        for i, old_led in enumerate(old_row):
            new_pos = (i + self.amount) % screen.x_size
            # Gv.log.debug(f'new_pos = {new_pos}')
            screen.leds[new_pos,self.row] = old_led


    def rot_col(self, screen: Screen) -> None:
        '''Execute rotate column command on screen'''
        old_col = screen.leds[self.col,:].copy()

        for i, old_led in enumerate(old_col):
            new_pos = (i + self.amount) % screen.y_size
            screen.leds[self.col,new_pos] = old_led


class Instructions(list[Instruction]):
    '''List container class of Instruction objects'''
    def __init__(self, lines:list[str]) -> None:
        for line in lines:
            self.append(Instruction(line))


    def process(self, screen: Screen) -> None:
        '''Process the Instructions on screen'''
        for instr in self:
            instr.process(screen)

            if Gv.test:
                print()
                print(screen.image())
                print()


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    screen = Screen(lines)
    screen.process_instrs()

    return screen.get_nr_of_leds()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    screen = Screen(lines)
    screen.process_instrs()

    return screen.image()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
