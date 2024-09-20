"""
Year 2020, Day 6

Problem description: See https://adventofcode.com/2020/day/6

The following classes are used:
- PassengerGroup: Represents a group of passengers. They have an attribute 
    answers (set), which contains all catagories answered with "yes".
- PassengerGroups: List container class of PassengerGroup objects.

Part 1: Use logical or to merge answer sets. Summarise the length of all answers 
attribute.

Part 2: For the first person, fill the set and for all next person, use logical 
and to merge the answer sets. Summarise in the end.

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
    def __init__(self) -> None:
        # Contains the set of cats that anyone has answered
        self.anyone_yes = set()
        # Contains the set of cats that everyone has answered
        # Starts with None to indicate that the first time it needs
        # to be set with the full contents of the persons answers
        self.all_yes = None


    def add_person(self, line: str) -> None:
        '''Add the answers from one person in the group'''
        self.anyone_yes |= set(line)

        if self.all_yes == None:
            self.all_yes = set(line)
        else:
            self.all_yes &= set(line)


class PassengerGroups(list[PassengerGroup]):
    '''List container class of PassengerGroup objects'''
    def __init__(self, lines: list[str]) -> None:
        new_pgroup = PassengerGroup()
        self.append(new_pgroup)

        for (i, line) in enumerate(lines):
            if line == '':
                new_pgroup = PassengerGroup()
                self.append(new_pgroup)
            else:
                new_pgroup.add_person(line)


    def get_all_answers_any_yes(self) -> int:
        '''Get the sum of all categories of all groups where anyone has
        answered yes'''
        sum_of_answers = 0

        for pgroup in self:
            sum_of_answers += len(pgroup.anyone_yes)

        return sum_of_answers


    def get_all_answers_all_yes(self) -> int:
        '''Get the sum of all categories of all groups where everyone has
        answered yes'''
        sum_of_answers = 0

        for pgroup in self:
            sum_of_answers += len(pgroup.all_yes)

        return sum_of_answers


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    pgroups = PassengerGroups(lines)

    return pgroups.get_all_answers_any_yes()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    pgroups = PassengerGroups(lines)

    return pgroups.get_all_answers_all_yes()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
