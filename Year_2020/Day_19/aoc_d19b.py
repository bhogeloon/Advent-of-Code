"""
Year 2020, Day 19, Part 2

Problem description: See https://adventofcode.com/2020/day/19

"""

# Imports
from pprint import pprint

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Rule():
    def __init__(self, line:str) -> None:
        index_str, rmdr = line.split(": ")

        self.index = int(index_str)

        if rmdr[0] == '"':
            self.ref = False
            self.value = rmdr[1]
        else:
            self.ref = True
            ref_options_str = rmdr.split(' | ')

            self.ref_options = []
            for ref_option_str in ref_options_str:
                refs = [int(a) for a in ref_option_str.split()]
                self.ref_options.append(refs)


    def explore(self, rules, loop_detect = None):
        if not self.ref:
            return [self.value]

        matched_msgs = Messages()

        if loop_detect == None:
            loop_detect = []

        if self.index in loop_detect:
            return matched_msgs

        loop_detect.append(self.index)

        for ref_option in self.ref_options:
            msgs1 = rules[ref_option[0]].explore(rules, loop_detect[:])

            if len(msgs1) == 0:
                continue

            if len(ref_option) == 1:
                matched_msgs.extend(msgs1)
                continue

            msgs2 = rules[ref_option[1]].explore(rules, loop_detect[:])

            if len(msgs2) == 0:
                continue

            for msg1 in msgs1:
                for msg2 in msgs2:
                    matched_msgs.append(msg1 + msg2)

        return matched_msgs


class Rules(dict):
    def fix(self):
        self[8] = Rule('8: 42 | 42 8')
        self[11] = Rule('11: 42 31 | 42 11 31')


class Message(str):
    pass


class Messages(list[Message]):
    pass


# Functions

def read_input(lines: list[str]) -> tuple:
    i = 0
    # Create empty rules
    rules = Rules()

    while lines[i] != '':
        # Add rule
        rule = Rule(lines[i])
        rules[rule.index] = rule
        if not rule.ref:
            rules[rule.value] = rule

        i += 1

    i += 2

    # Create empty Messages
    messages = Messages()

    for line in lines[i:]:
        pass
        # nb_tickets.append(Ticket(line))
        # Add message
        messages.append(Message(line))

    return rules, messages


# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    rules, messages = read_input(lines)

    rules.fix()

    valid_msgs = rules[0].explore(rules)
    print(len(valid_msgs))
    print()

    total_valid = 0

    for msg in messages:
        if msg in valid_msgs:
            total_valid += 1

    return total_valid

    return __name__


if __name__ == '__main__':
    pass