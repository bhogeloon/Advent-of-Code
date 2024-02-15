"""
Year 2020, Day 11, Part 2

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
                for dir_y in range(-1,2):
                    for dir_x in range(-1,2):
                        if dir_x == 0 and dir_y == 0:
                            pass
                        else:
                            if self.find_occ_seat(x, y, dir_x, dir_y):
                                occ += 1

                if self.seats[y][x] == 'L':
                    if occ == 0:
                        new_row += '#'
                        something_changed = True
                    else:
                        new_row += 'L'

                elif self.seats[y][x] == '#':
                    if occ >= 5:
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


    def find_occ_seat(self, cur_x, cur_y, dir_x, dir_y) -> bool:
        occ_found = False
        x = cur_x
        y = cur_y

        while True:
            if x <= 0 and dir_x < 0:
                break
            if x >= len(self.seats[y])-1 and dir_x > 0:
                break
            if y <= 0 and dir_y < 0:
                break
            if y >= len(self.seats)-1 and dir_y > 0:
                break

            x += dir_x
            y += dir_y

            if self.seats[y][x] == '#':
                occ_found = True
                break
            elif self.seats[y][x] == 'L':
                break

        return occ_found


# Functions



# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    wr = WaitingRoom(lines)

    return wr.calculate_stable()

    return __name__


if __name__ == '__main__':
    pass