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

Part 2: For each seat, start searching in every direction (including diagonal)
by indicating the dir_x and dir_y as -1, 0 or 1. As soon as you find a seat (so
no floor), note whether it is occupied or not. If on a border, the seat is not
occupied.
In this way, count the occupied seats and use the same process as in part 1
(only the max amount of occupied seats is now 4 instead of 3).
It takes quite some time before it stabilises (~3.5 seconds).

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


    def change_seats(self, part=1) -> bool:
        '''Change seats for one round'''
        # The max amount of occupied seats for each part
        if part == 1:
            max_occ_seats = 3
        else:
            max_occ_seats = 4

        # This will hold the new result
        self.old_seats = self.seats.copy()
        # Detect if there is a change
        something_changed = False

        for y in range(self.y_size):
            for x in range(self.x_size):
                # If this is a floor point, ignore
                if self.old_seats[x,y] == '.':
                    continue

                if part == 1:
                    occ = self.get_occ_seats_p1(x,y)
                else:
                    occ = self.get_occ_seats_p2(x,y)

                # If this is an empty seat
                if self.old_seats[x,y] == 'L':
                    # If no surrounding seats are occupied
                    if occ == 0:
                        # Occupy new seat
                        self.seats[x,y] = '#'
                        something_changed = True

                # If this is an occupied seat
                elif self.old_seats[x,y] == '#':
                    # If more than 3 surrounding seats occupied
                    if occ > max_occ_seats:
                        # Empty seat
                        self.seats[x,y] = 'L'
                        something_changed = True

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


    def find_occ_seat(self, cur_x, cur_y, dir_x, dir_y) -> bool:
        '''See if you can find an occupied seat in a specific direction'''
        occ_found = False
        x = cur_x
        y = cur_y

        while True:
            # break if a border has been found
            if x <= 0 and dir_x < 0:
                break
            if x >= self.x_size-1 and dir_x > 0:
                break
            if y <= 0 and dir_y < 0:
                break
            if y >= self.y_size-1 and dir_y > 0:
                break

            # Update x and y depending on the direction
            x += dir_x
            y += dir_y

            # If an occupied seat is found, set occ_found and break
            if self.old_seats[x,y] == '#':
                occ_found = True
                break
            # if an empty seat is found, leave occ_found False and break
            elif self.old_seats[x,y] == 'L':
                break

        return occ_found


    def get_occ_seats_p1(self, x:int, y:int) -> int:
        '''Count the number of occupied seats according the the rules of 
        part 1'''
        # Determine the boundaries (baring in mind the borders)
        min_x = max(0, x-1)
        max_x = min(self.x_size-1, x+1)
        min_y = max(0, y-1)
        max_y = min(self.y_size-1, y+1)

        # the amount of seats occupied
        occ = 0
        for y2 in range(min_y, max_y + 1):
            for x2 in range(min_x, max_x + 1):
                if self.old_seats[x2,y2] == '#':
                    # Ignore if own seat
                    if y == y2 and x == x2:
                        pass
                    else:
                        occ += 1

        return occ


    def get_occ_seats_p2(self, x:int, y:int) -> int:
        '''Count the number of occupied seats according the the rules of 
        part 2'''
        # the amount of seats occupied
        occ = 0
        # Try in all directions
        for dir_y in range(-1,2):
            for dir_x in range(-1,2):
                # If both directions are 0, skip
                if dir_x == 0 and dir_y == 0:
                    pass
                else:
                    # If you can find a seat, increase occ
                    if self.find_occ_seat(x, y, dir_x, dir_y):
                        occ += 1

        return occ


    def calculate_stable_p2(self) -> int:
        '''Repeat changing seats until no changes are detected (using the 
        part 2) logic'''
        while self.change_seats(part=2):
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

    wr = WaitingRoom(lines)

    return wr.calculate_stable_p2()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
