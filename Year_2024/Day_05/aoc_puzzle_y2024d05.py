"""
Year 2024, Day 5

Problem description: See https://adventofcode.com/2024/day/5

The following classes are used:
- Rule: A rule containing the before page nr and after page nr.
- Rules: List container class of Rule objects
- Update: A list of page numbers.
- Updates: List container class of Update objects

Part 1: For each Update, check for each rule if the index for the before page
is smaller than the index for the after page. If the rule contains a page number
that is not part of the update, ignore the rule. If all rules comply, this
update is correct. Then determine the middle number and add those up.
 
"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from collections import deque

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

class Rule:
    '''A rule consist of a before page and an after page'''
    def __init__(self, line:str):
        elements = line.split('|')
        self.before = int(elements[0])
        self.after = int(elements[1])


    def comply(self, update: Update) -> bool:
        '''Check if the update complies to the Rule'''
        # If the before or after is not part of the update, the rule does not
        # apply
        if self.before not in update or self.after not in update:
            return True
        
        if update.index(self.before) < update.index(self.after):
            return True
        else:
            return False


class Rules(list[Rule]):
    '''List container class of Rule objects'''
    def __init__(self, lines: list[str]):
        for line in lines:
            self.append(Rule(line))


class Update(list[int]):
    '''A list class with with page numbers'''
    def __init__(self, line:str):
        pages = [int(p) for p in line.split(',')]
        self.extend(pages)


    def is_correct(self, rules: Rules) -> bool:
        '''Check if the update is according to the rules'''
        for rule in rules:
            if not rule.comply(self):
                return False

        return True
    

    def get_middle_page(self) -> int:
        '''Return the middle page'''
        return self[len(self)//2]


class Updates(list[Update]):
    '''List container class of Update objects'''
    def __init__(self, lines:list[str]):
        for line in lines:
            self.append(Update(line))


    def get_middle_pages(self, rules: Rules) -> int:
        '''Get the sum of all middle pages of each update, if correct'''
        result = 0

        for update in self:
            if update.is_correct(rules):
                result += update.get_middle_page()

        return result


# Functions

def process_input(lines:deque[str]) -> tuple[Rules, Updates]:
    '''Function to divide the lines between Rules and Updates.
    It returns the Rules and Updates objects'''
    rule_lines = []
    line = lines.popleft()

    while line != '':
        rule_lines.append(line)
        line = lines.popleft()

    rules = Rules(rule_lines)
    line = lines.popleft()
    update_lines = []

    while line != '':
        update_lines.append(line)
        if len(lines) == 0:
            line = ''
        else:
            line = lines.popleft()

    updates = Updates(update_lines)

    return rules, updates


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    rules, updates = process_input(deque(lines))

    return updates.get_middle_pages(rules)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
