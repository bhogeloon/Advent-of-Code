"""
Year 2016, Day 3

Problem description: See https://adventofcode.com/2016/day/3

The following classes are used:
- Triangle: A triangle with three sides and a sum of sides
- Triangles: List container class of Triangle objects

Part 1: Check for each side if it is smaller than half of the sum of sides.

For part 2 I just had to change the way to read the input. All lines are read in blocks
of 3 and then the vertical values are passed on the Triangle initiator.
The calculation remains the same.

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

    def __init__(self, a: int, b: int, c: int) -> None:
        self.sides = [a, b, c]
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

    def __init__(self, lines: list[str], method='hor') -> None:
        if method == 'hor':
            self._init_hor(lines)
        elif method == 'ver':
            self._init_ver(lines)
        else:
            raise RuntimeError("Unkown method: {}".format(method))


    def _init_hor(self, lines:list[str]) -> None:
        '''Create Triangle object read horizontally (part 1)'''
        for line in lines:
            self.append(Triangle(*exctract_ints(line)))


    def _init_ver(self, lines: list[str]):
        '''Create Triangle object read vertically (part 2)'''
        for i in range(0,len(lines),3):
            size_block = []
            for j in range(3):
                size_block.append(exctract_ints(lines[i+j]))

            # Create Triangle objects using the vertical values
            for x in range(3):
                self.append(Triangle(
                    size_block[0][x],
                    size_block[1][x],
                    size_block[2][x],
                ))


    def get_valid(self) -> int:
        '''Count all valid triangles'''
        result = 0

        for triangle in self:
            if triangle.is_valid():
                result += 1

        return result


# Functions

def exctract_ints(line: str) -> list[int]:
    '''Function that reads a line and returns the integers (seperated by blanks)'''
    return [int(s) for s in line.split()]


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

    triangles = Triangles(lines, method='ver')

    return triangles.get_valid()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
