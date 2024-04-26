"""
Year 2015, Day 2

Problem description: See https://adventofcode.com/2015/day/2

The following classes are used:
- Present: represents a present with sizes (lwh). At creation time also the three different area's
are calculated.
- Presents: List container class of Present objects.

For part 1, the three area's are summarized and multiplied by 2. Then we add the minimum area.

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
        self.areas = []
        self.areas.append(self.sizes['l'] * self.sizes['w'])
        self.areas.append(self.sizes['w'] * self.sizes['h'])
        self.areas.append(self.sizes['h'] * self.sizes['l'])


    def get_paper(self) -> int:
        return 2 * sum(self.areas) + min(self.areas)


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
