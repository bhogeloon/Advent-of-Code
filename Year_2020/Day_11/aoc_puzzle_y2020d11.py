"""
Year 2020, Day 11

Problem description: See https://adventofcode.com/2020/day/11

<Include solution description>

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from grid import Grid2D

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

class WaitingRoom(Grid2D):
    def __init__(self, lines: list[str]) -> None:
        # Include grid allocation
        self.seats = lines


    def change_seats(self) -> bool:
        new_seats = []
        something_changed = False

        for y in range(len(self.seats)):
            new_row = ''

            for x in range(len(self.seats[y])):
                if self.seats[y][x] == '.':
                    new_row += '.'
                    continue

                min_x = max(0, x-1)
                max_x = min(len(self.seats[y])-1, x+1)
                min_y = max(0, y-1)
                max_y = min(len(self.seats)-1, y+1)

                occ = 0
                for y2 in range(min_y, max_y + 1):
                    for x2 in range(min_x, max_x + 1):
                        if self.seats[y2][x2] == '#':
                            if y == y2 and x == x2:
                                pass
                            else:
                                occ += 1

                if self.seats[y][x] == 'L':
                    if occ == 0:
                        new_row += '#'
                        something_changed = True
                    else:
                        new_row += 'L'

                elif self.seats[y][x] == '#':
                    if occ > 3:
                        new_row += 'L'
                        something_changed = True
                    else:
                        new_row += '#'

            new_seats.append(new_row)

        self.seats = new_seats

        return something_changed


    def count_occ_seats(self) -> int:
        occ = 0
        for row in self.seats:
            for seat in row:
                if seat == '#':
                    occ += 1

        return occ


    def calculate_stable(self) -> int:
        while self.change_seats():
            pass

        return self.count_occ_seats()


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
