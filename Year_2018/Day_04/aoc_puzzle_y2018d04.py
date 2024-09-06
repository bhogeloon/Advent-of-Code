"""
Year 2018, Day 4

Problem description: See https://adventofcode.com/2018/day/4

<Include solution description>

"""

# Imports
from pprint import pprint
import re
from datetime import datetime, timedelta


# Constants

ONE_HOUR = timedelta(hours=1)

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Event():
    '''An event can be:
    - Guard starts shift
    - Guard falls asleep
    - Guard wakes up'''
    def __init__(self, line: str) -> None:
        m = re.fullmatch(r'\[(.*)\] (.*)', line)
        date_time_str = m.group(1)
        action = m.group(2)

        date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
        print(date_time.isoformat(), (date_time + ONE_HOUR).isoformat())


class Events(list[Event]):
    '''List container class of Event objects'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Event(line))


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    events = Events(lines)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
