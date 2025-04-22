"""
Year 2024, Day 7

Problem description: See https://adventofcode.com/2024/day/7

The following classes are used:
- CalibrationEquotation: containing a result and a list of arguments.
- CalibrationEquotations: List container class of CalibrationEquotation objects.

Part 1: A recursive function is being used to check if the result is equal to 
calculated result. Each time, the function is called with adding the next
argument as well as multiplying it.

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

class CalibrationEquotation():
    '''A calibration equotation containing a result and several arguments'''
    def __init__(self, line:str):
        (result_str, remainder) = line.split(': ')
        self.result = int(result_str)
        self.arguments = [int(a) for a in remainder.split()]


    def get_calibration(self, offset=0, result_so_far = None) -> bool:
        '''Return True if there is a way to get the result using + and *.
        This will be a recursive function. The offset value will determine
        at which argument the calculation will start'''
        if result_so_far is None:
            result_so_far = self.arguments[offset]

        # If at the end of all arguments
        if offset == len(self.arguments)-1:
            return result_so_far == self.result

        if self.get_calibration(
            offset=offset+1,
            result_so_far=result_so_far+self.arguments[offset+1]
        ):
            return True

        if self.get_calibration(
            offset=offset+1,
            result_so_far=result_so_far*self.arguments[offset+1]
        ):
            return True

        return False
    

class CalibrationEquotations(list[CalibrationEquotation]):
    '''List container class of CalibrationEquotation objects'''
    def __init__(self, lines: list[str]):
        for line in lines:
            self.append(CalibrationEquotation(line))


    def get_total_calibration(self) -> int:
        '''Return the total calibration result'''
        result = 0

        for caleq in self:
            if caleq.get_calibration():
                result += caleq.result

        return result


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    caleqs = CalibrationEquotations(lines)

    return caleqs.get_total_calibration()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
