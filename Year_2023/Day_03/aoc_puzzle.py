"""
Year 2023, Day 3

Problem description: See https://adventofcode.com/2023/day/3

"""

# Imports
from pprint import pprint
import numpy as np
import string

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


# Classes
class Engine():
    '''Matrix containing all the engine information'''
    def __init__(self, lines: list[str]) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        self.chars = np.full((self.x_size, self.y_size), None)

        for y in range(self.y_size):
            for x in range(self.x_size):
                self.chars[x,y] = lines[y][x]

        self.part_numbers = []
        self.parts = []
        self.gear_ratios = []


    def investigate(self) -> None:
        # pointers to keep track on where we are
        self._cur_x = 0
        self._cur_y = 0

        while self._cur_y < self.y_size:

            # If end of line
            if self._cur_x >= self.x_size:
                self._cur_y += 1
                self._cur_x = 0
                continue

            # If a number has been found
            if self.chars[self._cur_x, self._cur_y] in string.digits:
                self.get_candidate()
                self.check_part_number()

            self._cur_x += 1

    def get_candidate(self) -> None:
        self._cand_start = self._cur_x
        candidate_str = ''

        while True:
            if self._cur_x >= self.x_size:
                break

            if self.chars[self._cur_x,self._cur_y] not in string.digits:
                break

            candidate_str += self.chars[self._cur_x, self._cur_y]
            self._cand_stop = self._cur_x

            self._cur_x += 1

        self.candidate = int(candidate_str)


    def check_part_number(self) -> None:
        # create candidat part
        cand_part = Part(self.candidate)

        min_x = self._cand_start - 1
        max_x = self._cand_stop + 1
        min_y = self._cur_y - 1
        max_y = self._cur_y + 1

        real_part_nr = False

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if x < 0 or x >= self.x_size:
                    continue
                if y < 0 or y >= self.y_size:
                    continue
                if self.chars[x,y] == '.':
                    continue
                if self.chars[x,y] in string.digits:
                    continue

                if self.chars[x,y] == '*':
                    cand_part.add_gear_pos(x,y)

                real_part_nr = True
        if real_part_nr:
            self.part_numbers.append(self.candidate)
            self.parts.append(cand_part)


    def find_gears(self) -> None:
        '''Find all gears and calculate Gear Ratios'''
        for y in range(self.y_size):
            for x in range(self.x_size):
                if self.chars[x,y] != '*':
                    continue

                gear_part_nrs = []

                for part in self.parts:
                    if (x,y) in part.gear_pos:
                        gear_part_nrs.append(part.number)

                if len(gear_part_nrs) > 2:
                    raise RuntimeError("More than 2 parts {},{}".format(x,y))
                
                if len(gear_part_nrs) == 2:
                    self.gear_ratios.append(gear_part_nrs[0] * gear_part_nrs[1])


class Part():
    '''Part containing part number and all positions in the grid'''

    def __init__(self, part_nr: int) -> None:
        self.number = part_nr
        self.gear_pos = []


    def add_gear_pos(self, x, y) -> None:
        self.gear_pos.append((x,y))


# Main functions
def get_solution_part1(lines: list[str]) -> int:
    '''Main function'''

    engine = Engine(lines)
    engine.investigate()

    return sum(engine.part_numbers)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str]) -> int:
    '''Main function'''

    engine = Engine(lines)
    engine.investigate()
    engine.find_gears()

    return sum(engine.gear_ratios)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass