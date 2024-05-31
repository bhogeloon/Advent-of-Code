"""
Year 2018, Day 3

Problem description: See https://adventofcode.com/2018/day/3

The following classes are used:
- Fabric: This contains the Numpy grid with fabric positions
- ElveIds: Each Fabric grid position holds an ElveIds object. This is a list
    that contains all ElveIds that claim this position.

Part 1: For each input line, the grid positions are determined and for each grid position, the
claim ID is added. As soon as the number of ids reaches 2, the double_booked counter is increased.

Part 2: An additional function is used to find the single isolated claim. We introduce an
attribute, which collects all candidate claim ids (in a set). It goes through all the grid position
and if a single id has been found (which wasn't seen before), it is added as candidate. If
multiple ids are found they are removed from the set. In the end only one should be left.

"""

# Imports
from pprint import pprint
import numpy as np
import re


# Constants

# Grid size
GRID_SIZE = 1000


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Fabric():
    '''Class for the fabric for Santa's outfit.
    Contains a numpy grid object'''

    def __init__(self) -> None:
        self.grid = np.full((GRID_SIZE,GRID_SIZE), None)

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                self.grid[x,y] = ElveIds()

        # Counter that keeps track of all positions that are occupied by
        # multiple ElveIds
        self.double_booked = 0
        self.isolated_claims = set()


    def gather_claims(self, lines: list[str]) -> None:
        '''Process all Elve claims'''
        for line in lines:
            self.process_claim(line)


    def process_claim(self, line: str) -> None:
        '''Process Elve claim'''
        m = re.fullmatch(r'#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)', line)

        id = int(m.group(1))
        x_start = int(m.group(2))
        y_start = int(m.group(3))
        x_len = int(m.group(4))
        y_len = int(m.group(5))

        for y in range(y_start, y_start+y_len):
            for x in range(x_start, x_start+x_len):
                # If double booked, increment counter
                if self.grid[x,y].add_id(id) == 2:
                    self.double_booked += 1


    def find_isolated_claim(self) -> None:
        '''Find the isloated claim and store in the isolated_claims set attribute'''
        # Set to track which ids have already been considered
        ids_considered = set()

        for elve_ids in self.grid.flat:
            # If one id found, add it to the cancidate set
            if len(elve_ids) == 1 and elve_ids[0] not in ids_considered:
                self.isolated_claims |= set(elve_ids)
                ids_considered |= set(elve_ids)
            # If multiple ids found, remove them from the candidate set
            elif len(elve_ids) > 1:
                self.isolated_claims -= set(elve_ids)
                ids_considered |= set(elve_ids)


class ElveIds(list[int]):
    '''Elve Ids that occupy the Fabric grid position'''

    def __init__(self) -> None:
        pass


    def add_id(self, id: int) -> int:
        self.append(id)
        return len(self)


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    fabric = Fabric()
    fabric.gather_claims(lines)

    return fabric.double_booked

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    fabric = Fabric()
    fabric.gather_claims(lines)
    fabric.find_isolated_claim()

    if len(fabric.isolated_claims) > 1:
        raise RuntimeError("More than 1 entry found in the set")

    return fabric.isolated_claims.pop()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
