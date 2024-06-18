"""
Year 2023, Day 3

Problem description: See https://adventofcode.com/2023/day/3

The following classes are used:
- Engine: Represents the total engine. It contains the following aatributes:
    - chars: Numpy object that contains the matrix with all the characters
    - part_numbers: List of part number integers

- Part: A part within the engine containing a part number.
    It also gets an attribute gear_pos, to which all gear positions (* symbols)
    are stored where the part connects to.

For part 1: Go through the matrix in search for digits. Is a digit is found, try
to find more digits to get the potential (candidate) part number. Then search for symbols
in the surrounding area to see if it's a real part number.
In the end add all the part numbers together.

For part 2, we start by doing the same as in part 1 (finding all the parts). In this process,
we also notify all gear positions connected to each part.
After this process, we go again through the matrix. If we found a gear, we go through all 
the parts to see if this gear position is connected to the part. If 2 parts are found,
we multiply the part numbers and list the result. At the end, the summary is returned.
"""

# Imports
from pprint import pprint
import string
from grid import Grid2D


# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


# Classes
class Engine(Grid2D):
    '''Matrix containing all the engine information'''
    def __init__(self, lines: list[str]) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        super().__init__(
            sizes=(self.x_size,self.y_size),
        )
        self.chars = self.grid

        for y in range(self.y_size):
            for x in range(self.x_size):
                self.chars[x,y] = lines[y][x]

        self.part_numbers = []
        self.parts = []
        self.gear_ratios = []


    def investigate(self) -> None:
        '''Walks through the matrix in search for numbers.
        It then will call a function to see if it is an actual
        part number'''

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
        '''Read all the digits of a candidate'''

        # Keep track of the grid position of the candidate string
        self._cand_start = self._cur_x
        candidate_str = ''

        while True:
            # If end of line
            if self._cur_x >= self.x_size:
                break

            # If current character is no longer a digit
            if self.chars[self._cur_x,self._cur_y] not in string.digits:
                break

            # Add digit to the candidate string
            candidate_str += self.chars[self._cur_x, self._cur_y]
            # Keep track of the grid position of the candidate string
            self._cand_stop = self._cur_x

            self._cur_x += 1

        # Store candidate as integer
        self.candidate = int(candidate_str)


    def check_part_number(self) -> None:
        '''Check if the candidate is actually a part number'''

        # create candidate part object
        cand_part = Part(self.candidate)

        # Set the search boundaries
        min_x = self._cand_start - 1
        max_x = self._cand_stop + 1
        min_y = self._cur_y - 1
        max_y = self._cur_y + 1

        real_part_nr = False

        # Search for symbol within the search boundaries
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

                # If we did not find anything that is not a symbol
                real_part_nr = True
 
        # If it is a real part number
        if real_part_nr:
            # Add to part numbers and part objects
            self.part_numbers.append(self.candidate)
            self.parts.append(cand_part)


    def find_gears(self) -> None:
        '''Find all gears and calculate Gear Ratios'''

        for y in range(self.y_size):
            for x in range(self.x_size):
                # If a gear is found
                if self.chars[x,y] != '*':
                    continue

                gear_part_nrs = []

                # Find the connecting part numbers
                for part in self.parts:
                    if (x,y) in part.gear_pos:
                        # Add the part numbers for this gear
                        gear_part_nrs.append(part.number)

                # If more than 2 parts have been found connecting to this gear,
                # raise an exception as this should not occur
                if len(gear_part_nrs) > 2:
                    raise RuntimeError("More than 2 parts {},{}".format(x,y))

                # If we found 2 parts connected                
                if len(gear_part_nrs) == 2:
                    # Multiply the part numbers and add to the gear_ratios list
                    self.gear_ratios.append(gear_part_nrs[0] * gear_part_nrs[1])


class Part():
    '''Part containing part number and all positions in the grid'''

    def __init__(self, part_nr: int) -> None:
        self.number = part_nr
        self.gear_pos = []


    def add_gear_pos(self, x, y) -> None:
        '''Add the coordinates of a gear position (*) to the gear_pos list'''
        self.gear_pos.append((x,y))


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    engine = Engine(lines)
    engine.investigate()

    return sum(engine.part_numbers)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    engine = Engine(lines)
    engine.investigate()
    engine.find_gears()

    return sum(engine.gear_ratios)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass