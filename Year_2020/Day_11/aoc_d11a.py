"""
Year 2020, Day 11, Part 1

Problem description: See https://adventofcode.com/2020/day/11

"""

# Imports
from pprint import pprint

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes
class WaitingRoom():
    def __init__(self, lines: list[str]) -> None:
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



# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    wr = WaitingRoom(lines)

    return wr.calculate_stable()

    return __name__


if __name__ == '__main__':
    pass