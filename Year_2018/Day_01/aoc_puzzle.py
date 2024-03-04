"""
Year 2018, Day 1

Problem description: See https://adventofcode.com/2018/day/1

I have created the following classes:
Frequency: The actual frequency (the end result of part 1)
FrequencyChange: The change in frequency (each line in the puzzle input)
FrequencyChanges: The list of all changes.

For the first part: go through the list and keep adding the change.



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

class Frequency():
    '''The resulting frequency'''

    def __init__(self) -> None:
        self.freq = 0

    
    def change(self, fc) -> None:
        '''Change the frequency according the the FrequencyChange'''
        self.freq += fc.change


    def change_all(self, fcs) -> None:
        '''Change the frequence following the list of changes'''
        for fc in fcs:
            self.change(fc)


class FrequencyChange():
    '''The change in frequency'''
    def __init__(self, line:str) -> None:
        self.change = int(line)


class FrequencyChanges(list[FrequencyChange]):
    '''Container class (list) of FrequencyChange objects'''
    def __init__(self, lines:list[str]) -> None:
        for line in lines:
            self.append(FrequencyChange(line))


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    fcs = FrequencyChanges(lines)

    freq = Frequency()
    freq.change_all(fcs)

    return freq.freq

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
