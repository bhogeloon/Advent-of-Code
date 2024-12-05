"""
Year 2024, Day 2

Problem description: See https://adventofcode.com/2024/day/2

The following classes are being used:
- Report: A single report, containing a list of levels
- UnusualData: List container class of Report objects

Part 1: Go through each report and look at two succeeding levels. Check the
size of the difference. If the order is not yet known record it. If it is known
check if it stays that way.
Count the number of safe reports.

Part 2: Check whether the report is safe (as in part 1), but if not: copy the
report, remove one level and check again. Do this for each level. If one is
safe, the whole report is safe.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from copy import deepcopy

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

class Report(list[int]):
    '''List class containing several levels'''
    def __init__(self, line: str) -> None:
        self.extend([int(lvl) for lvl in line.split()])


    def is_safe(self) -> bool:
        '''Check if this report is safe'''
        # Order can be 'asc', 'dec' or 'unk'(own)
        self.order = 'unk'

        for i in range(len(self)-1):
            # First calculate the difference
            diff = self[i+1] - self[i]

            # If diff is too little or too much, bale out
            if abs(diff) < 1 or abs(diff) > 3:
                return False
            
            # If order is unknown yet, set it:
            if self.order == 'unk':

                if diff > 0:
                    self.order = 'asc'
                else:
                    self.order = 'dec'
                
                continue

            # Check id order is consistent:
            if (
                (diff > 0 and self.order == 'dec') or
                (diff < 0 and self.order == 'asc')
            ):
                return False

        # If not bailed out, report is safe
        return True
    

    def is_dampened_safe(self) -> bool:
        '''Check if the report is safe, considering the Problem Dampener'''
        # First, if the whole report is safe, we are good
        if self.is_safe():
            return True
        
        # Now remove a level one by one and check again
        for i in range(len(self)):
            dampened_report = deepcopy(self)
            del dampened_report[i]
            # Gv.log.debug(dampened_report)

            if dampened_report.is_safe():
                return True
            
        # If none are safe
        # Gv.log.debug(self)
        return False


class UnusualData(list[Report]):
    '''List container class of Report objects'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Report(line))


    def nr_of_safe_reports(self) -> int:
        '''Return the number of safe reports'''
        nr = 0

        for report in self:
            if report.is_safe():
                nr += 1

        return nr
    

    def nr_of_dampened_safe_reports(self) -> int:
        '''Return the number of safer reports, considering the Problem
        Dampener'''
        nr = 0

        for report in self:
            if report.is_dampened_safe():
                nr += 1

        return nr


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    data = UnusualData(lines)

    return data.nr_of_safe_reports()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    data = UnusualData(lines)

    return data.nr_of_dampened_safe_reports()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
