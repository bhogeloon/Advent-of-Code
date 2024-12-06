"""
Year 2020, Day 11

Problem description: See https://adventofcode.com/2020/day/11

The following class is used:
- WaitingRoom: Grid class containing the seat states.

Part 1: Each time make a copy of the seats as you need look at the current
value of the surrounding seats for each seat in turn.
Then for each seat look at the surrounding seats and count the seats occupied:
- If no other seats are occupied, make the seat occupied.
- If more than 3 seats are occupied, make the seat empty.
If a change is made, notify this.
Repeat this process, until no changes are notified for a particular round.
Then count the number of occupied seats.

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
        self.y_size = len(lines)
        self.x_size = len(lines[0])
        super().__init__(
            sizes=(self.x_size,self.y_size),
            input_lines=lines,
        )
        # Include grid allocation
        self.seats = self.grid


    def change_seats(self) -> bool:
        '''Change seats for one round'''
        # This will hold the new result
        new_seats = self.seats.copy()
        # Detect if there is a change
        something_changed = False

        for y in range(self.y_size):
            for x in range(self.x_size):
                # If this is a floor point, ignore
                if self.seats[x,y] == '.':
                    continue

                # Determine the boundaries (baring in mind the borders)
                min_x = max(0, x-1)
                max_x = min(self.x_size-1, x+1)
                min_y = max(0, y-1)
                max_y = min(self.y_size-1, y+1)

                # the amount of seats occupied
                occ = 0
                for y2 in range(min_y, max_y + 1):
                    for x2 in range(min_x, max_x + 1):
                        if self.seats[x2,y2] == '#':
                            # Ignore if own seat
                            if y == y2 and x == x2:
                                pass
                            else:
                                occ += 1

                # If this is an empty seat
                if self.seats[x,y] == 'L':
                    # If no surrounding seats are occupied
                    if occ == 0:
                        # Occupy new seat
                        new_seats[x,y] = '#'
                        something_changed = True

                # If this is an occupied seat
                elif self.seats[x,y] == '#':
                    # If more than 3 surrounding seats occupied
                    if occ > 3:
                        # Empty seat
                        new_seats[x,y] = 'L'
                        something_changed = True

        # Point seats to the new grid
        self.seats = new_seats
        self.grid = self.seats

        return something_changed


    def count_occ_seats(self) -> int:
        '''Count the seats occupied'''
        occ = 0
        for seat in self.seats.flat:
            if seat == '#':
                occ += 1

        return occ


    def calculate_stable(self) -> int:
        '''Repeat changing seats until no changes are detected'''
        while self.change_seats():
            Gv.log.debug(self)

        return self.count_occ_seats()
    

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    wr = WaitingRoom(lines)

    return wr.calculate_stable()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
