"""
Year 2016, Day 3

Problem description: See https://adventofcode.com/2016/day/3

The following classes are used:
- Triangle: A triangle with three sides and a sum of sides
- Triangles: List container class of Triangle objects

Part 1: Check for each side if it is smaller than half of the sum of sides.

"""

# Imports
from pprint import pprint


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Triangle():
    '''Triangle with three sides'''

    def __init__(self, line: str) -> None:
        self.sides = [int(s) for s in line.split()]
        self.side_sum = sum(self.sides)


    def is_valid(self) -> bool:
        '''Check if triangle is valid.
        The triangle is valid if sides[i] < sides[i] - side_sum
        So invalid if sides[i] >= sides[i] - side_sum
        Or: 2*sides[i] > = side_sum'''
        for side in self.sides:
            if 2*side >= self.side_sum:
                return False
            
        return True


class Triangles(list[Triangle]):
    '''List container class of Triangle objects'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Triangle(line))


    def get_valid(self) -> int:
        '''Count all valid triangles'''
        result = 0

        for triangle in self:
            if triangle.is_valid():
                result += 1

        return result


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    triangles = Triangles(lines)

    return triangles.get_valid()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
