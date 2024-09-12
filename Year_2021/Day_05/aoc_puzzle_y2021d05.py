"""
Year 2021, Day 5

Problem description: See https://adventofcode.com/2021/day/5

The following classes are used:
- OceanFloor: A numpy grid containing a single integer that represents the 
    amount of lines passing through
- VentLine: A line of hydrothermal
- VentLines: List container class of VentLine objects

Part 1: In processing the VentLines, we only consider VentLines it the
x coordinates or the y coordinates are equal. Then we walk through the
other coordinate to increase the number in the grid.

"""

# Imports
from pprint import pprint
from grid import Grid2D


# Constants

GRID_SIZE = 1000

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class VentLine():
    '''A line of hydrothermal vents'''
    def __init__(self, line: str) -> None:
        xy_str = line.split(' -> ')
        (x1_str, y1_str) = xy_str[0].split(',')
        self.x1 = int(x1_str)
        self.y1 = int(y1_str)
        (x2_str, y2_str) = xy_str[1].split(',')
        self.x2 = int(x2_str)
        self.y2 = int(y2_str)


class VentLines(list[VentLine]):
    '''List container class of Line objects'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(VentLine(line))


class OceanFloor(Grid2D):
    '''Represents the ocean floor, containg a numpy grid.
    The cells contain an int wich represents the amount of lines passing'''
    def __init__(self) -> None:
        super().__init__(
            sizes=(GRID_SIZE,GRID_SIZE),
            default_value=0,
        )


    def process_vent_lines_straight(self, vent_lines: VentLines) -> None:
        '''Processs all the ventlines and update the grid, using only straight
        lines'''
        for vent_line in vent_lines:
            # if x coordinates are the same:
            if vent_line.x1 == vent_line.x2:
                # Put them in the right order
                (y_small, y_big) = sorted([vent_line.y1, vent_line.y2])
                for y in range(y_small, y_big + 1):
                    self.grid[vent_line.x1, y] += 1

            # if y coordinates are the same:
            elif vent_line.y1 == vent_line.y2:
                # Put them in the right order
                (x_small, x_big) = sorted([vent_line.x1, vent_line.x2])
                for x in range(x_small, x_big + 1):
                    self.grid[x, vent_line.y1] += 1

            # Otherwise it is not a straight line, so no further action needed


    def get_nr_of_crossings(self) -> int:
        '''Return the number of crossings in the grid'''
        result = 0

        for pos in self.grid.flat:
            if pos > 1:
                result += 1

        return result


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    floor = OceanFloor()
    vent_lines = VentLines(lines)
    floor.process_vent_lines_straight(vent_lines)

    return floor.get_nr_of_crossings()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
