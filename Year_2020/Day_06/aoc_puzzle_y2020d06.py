"""
Year 2020, Day 6

Problem description: See https://adventofcode.com/2020/day/6

The following classes are used:
- PassengerGroup: Represents a group of passengers. They have an attribute 
    answers (set), which contains all catagories answered with "yes".
- PassengerGroups: List container class of PassengerGroup objects.

Part 1: Summarise the length of all answers attribute.

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

class PassengerGroup():
    '''Represents a group of passengers. They have an attribute answers (set),
    which contains all catagories answered with "yes".'''
    def __init__(self, answers: set[str]) -> None:
        self.answers = answers


class PassengerGroups(list[PassengerGroup]):
    '''List container class of PassengerGroup objects'''
    def __init__(self, lines: list[str]) -> None:
        answers = set()

        for (i, line) in enumerate(lines):
            if line == '':
                self.append(PassengerGroup(answers))
                answers = set()
                continue

            answers |= set(line)

            if len(lines) == i+1:
                self.append(PassengerGroup(answers))


    def get_all_answers(self) -> int:
        '''Get the sum of all answers of all groups'''
        sum_of_answers = 0

        for pgroup in self:
            sum_of_answers += len(pgroup.answers)

        return sum_of_answers


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    pgroups = PassengerGroups(lines)

    return pgroups.get_all_answers()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
