"""
Year 2021, Day 14

Problem description: See https://adventofcode.com/2021/day/14

The following classes are used:
- Polymer: Contains the polymer character string
- PairInsertionRule: a rule to insert the insertion char in between the 
    matching characters.
- PairInsertionRules: Dict container class of PairInsertionRule objects with
    the matching characters as key.

Part 1: Go through the polymer string and for every pair see if there is an 
existing rule. If so, insert the character. Repeat this 10 times.
Then find the highest and lowest occurences and calulate the difference.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from input_handling import split_input
from collections import Counter


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

class Polymer():
    '''Character string representing the Polymer'''
    def __init__(self, pol: str):
        self.pol = pol


    def get_high_low_diff(self) -> int:
        '''Return the difference between the highest amount of elements
        present and the lowes amount'''
        occ = Counter(self.pol)

        return max(occ.values()) - min(occ.values())
    

    def insert(self, rules: PairInsertionRules) -> None:
        '''Execute the Pair Insertion rules'''
        new_pol = ''

        for nr in range(len(self.pol)):
            # Write current char
            new_pol += self.pol[nr]
            # Don't look ahead if last char
            if nr < len(self.pol) - 1:
                char_left = self.pol[nr]
                char_right = self.pol[nr + 1]
                combi = char_left + char_right
                # Check if a key exist
                if combi in rules.keys():
                    # Write extra element
                    new_pol += rules[combi].insertion

        self.pol = new_pol


class PairInsertionRule():
    '''Represents a single rule, containing the the two elements to match
    and the insertion element'''
    def __init__(self, match_pair: str, insertion: str):
        self.match_pair = match_pair
        self.insertion = insertion


class PairInsertionRules(dict):
    '''Dict container class containing all the rules, with the matching 
    elements as key.'''
    def __init__(self, lines: list[str]):
        for line in lines:
            match_pair, insertion = line.split(' -> ')
            self[match_pair] = PairInsertionRule(match_pair, insertion)
        
# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)


    (pol_list, rules_list) = split_input(lines)

    pol = Polymer(pol_list[0])

    rules = PairInsertionRules(rules_list)

    for i in range(10):
        pol.insert(rules)

    return pol.get_high_low_diff()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
