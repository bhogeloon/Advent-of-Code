"""
Year 2015, Day 2

Problem description: See https://adventofcode.com/2015/day/2

<Include solution description>

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

class Present():
    '''A Present has three dimension sizes ('w', 'l' and 'h'). They are reprented in a dict'''
    
    def __init__(self, line: str) -> None:
        self.sizes = {}

        self.sizes['l'], self.sizes['w'],self.sizes['h']=[int(s) for s in line.split('x')]


    def get_paper(self) -> int:
        result = 2 * self.sizes['l'] * self.sizes['w']
        result += 2 * self.sizes['w'] * self.sizes['h']
        result += 2 * self.sizes['h'] * self.sizes['l']
        # This is wrong
        result += min(self.sizes.values())

        return result


class Presents(list[Present]):
    '''List container class of Present objects'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Present(line))


    def get_total_paper(self) -> int:
        result = 0
        for present in self:
            result += present.get_paper()

        return result
    

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    presents = Presents(lines)

    return presents.get_total_paper()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
