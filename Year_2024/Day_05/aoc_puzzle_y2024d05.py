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

Part 2: Now in addition to check if the update complies to each rule, I 
immediately correct the update by moving the 'before' value just before the
'after' value. I also proceed with checking the result and repeat going over
all the rules until no issues have been found anymore.
Then finally consider only the Updates that were corrected and get the middle
value and add them up.

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


    def comply(self, update: Update, correct=False) -> bool:
        '''Check if the update complies to the Rule. If it does not comply and 
        the correct flag is set, correct the update, but still return False.'''
        # If the before or after is not part of the update, the rule does not
        # apply
        if self.before not in update or self.after not in update:
            return True
        
        before_index = update.index(self.before)
        after_index = update.index(self.after)

        if before_index < after_index:
            return True

        if correct:
            # Move the before value just before the after value
            del update[before_index]
            update.insert(after_index, self.before)

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


    def is_correct(self, rules: Rules, correct=False) -> bool:
        '''Check if the update is according to the rules. If it is not
        correct and the correct flag is set, correct it, but still return 
        False.'''
        result = True

        found_incorrect = True

        # Repeat the process until no issues found
        while found_incorrect:
            found_incorrect = False

            for rule in rules:
                if not rule.comply(self, correct=correct):
                    if correct:
                        result = False
                        found_incorrect = True
                    else:
                        return False

        return result
    

    def get_middle_page(self) -> int:
        '''Return the middle page'''
        return self[len(self)//2]
    

class Updates(list[Update]):
    '''List container class of Update objects'''
    def __init__(self, lines:list[str]):
        for line in lines:
            self.append(Update(line))


    def get_middle_pages(self, rules: Rules, part=1) -> int:
        '''Get the sum of all middle pages of each update, if correct'''
        result = 0

        if part == 1:
            correct = False
        else:
            correct = True

        for update in self:
            update_is_correct = update.is_correct(rules, correct=correct)

            if part == 1 and update_is_correct:
                result += update.get_middle_page()
            elif part == 2 and not update_is_correct:
                Gv.log.debug(f'Getting middle page for {update}')
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

    rules, updates = process_input(deque(lines))

    return updates.get_middle_pages(rules,part=2)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
