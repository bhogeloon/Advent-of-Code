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

Part 2:
Simply run the cycle 40 times? Well that takes too long.
Instead an additional attribute is added to the rule object, in which the
insertion string of each entry is calculated after 20 cycles. 
This string is then inserted in 2 cycles each. In the second we only count the 
occurences.
This way, the task is completed in a little under 3 mu=inutes.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from input_handling import split_input
from collections import Counter


# Constants

# Nr of pre-cycles in part 2
PRE_CYCLE = 40

# Nr of main cycles in part 2
MAIN_CYCLE = 1


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
        # Manual counter object, initially None
        self.cnt20 = None


    def get_high_low_diff(self) -> int:
        '''Return the difference between the highest amount of elements
        present and the lowes amount'''
        if self.cnt20 is None:
            occ = Counter(self.pol)
        else:
            occ = self.cnt20

        return max(occ.values()) - min(occ.values())
    

    def insert(self,
               rules: PairInsertionRules,
               use_extend=False,
               only_count=False,
               ) -> None:
        '''Execute the Pair Insertion rules.
        With the use_extend flag set the insertion will be done using
        the extended insertion string.
        With the only_count flag set, only the Counter object is updated'''
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
                    if only_count:
                       for element, el_amount in rules[combi].cnt.items():
                            if element in self.cnt20.keys():
                                self.cnt20[element] += el_amount
                            else:
                                self.cnt20[element] = el_amount
                    elif use_extend:
                        new_pol += rules[combi].extended_ins
                    else:
                        new_pol += rules[combi].insertion

        self.pol = new_pol


class PairInsertionRule():
    '''Represents a single rule, containing the the two elements to match
    and the insertion element'''
    def __init__(self, match_pair: str, insertion: str):
        self.match_pair = match_pair
        self.insertion = insertion


    def extend_ins_str(self, rules: PairInsertionRules) -> None:
        '''Create a new extended_ins attribute containing the insertion string 
        calculated after 20 cycles.
        Also create a cnt attribute, containing the counter object of the
        extended_ins string'''
        # Create polymer from match_pair
        pol = Polymer(self.match_pair)

        # Calculate new polymer after PRE_CYCLE cycles
        for i in range(20):
            pol.insert(rules)

        # Extract original match pair from start and end
        self.extended_ins = pol.pol[1:-1]
        self.cnt = Counter(self.extended_ins)


class PairInsertionRules(dict[str, PairInsertionRule]):
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

    (pol_list, rules_list) = split_input(lines)

    pol = Polymer(pol_list[0])

    rules = PairInsertionRules(rules_list)

    # Prepare rules with extended string
    for n, rule in enumerate(rules.values()):
        Gv.log.debug(f"starting extending rule {n} of {len(rules.values())}")
        rule.extend_ins_str(rules)

    Gv.log.debug("Rules prepared")

    # Execute the insert cycle 20 times using the extended string
    Gv.log.debug("Starting initial 20 cycles in one go")
    pol.insert(rules, use_extend=True)

    # Set counter object.
    pol.cnt20 = Counter(pol.pol)

    # Do the final extended insertion
    Gv.log.debug("Starting final cycle (only count)")
    pol.insert(rules, only_count=True)

    return pol.get_high_low_diff()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
