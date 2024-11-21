"""
Year 2015, Day 8

Problem description: See https://adventofcode.com/2015/day/8

The following classes are used:
- SantaLine: a line in Santa's list
- SantaList: List container class of SantaLine objects

Part 1: Use the python eval() function to evaluate the string in each line.
Then get the difference in length between the line (SantaLine.code) and the
evaluated line (SantaLine.mem). Add those together for all lines.
"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger

# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False

    # Variable that will be used for holding the logger object
    log = None

    def __init__(self, test: bool, logger: Logger, **kwargs) -> None:
        '''Initialize the global variables'''
        Gv.test = test
        Gv.log = logger


# Classes

class SantaLine:
    '''Line from Santa's list'''
    def __init__(self, line: str) -> None:
        self.code = line
        self.mem = eval(self.code)

        Gv.log.debug(f'{self.code} --- {self.mem}')


class SantaList(list[SantaLine]):
    '''List container class of SantaLine objects'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(SantaLine(line))


    def get_code_minus_mem(self) -> int:
        '''Get the total amount of code characters minus the total amount
        of memory characters'''
        total = 0

        for santaline in self:
            total += len(santaline.code) - len(santaline.mem)

        return total


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    Gv.log.debug(lines)
    santalist = SantaList(lines)

    return santalist.get_code_minus_mem()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
