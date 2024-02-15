"""
Year 2020, Day 19, Part 1

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


    def explore(self, rules):
        if not self.ref:
            return [self.value]

        matched_msgs = Messages()

        for ref_option in self.ref_options:
            msgs1 = rules[ref_option[0]].explore(rules)

            if len(ref_option) == 1:
                matched_msgs.extend(msgs1)
                continue

            msgs2 = rules[ref_option[1]].explore(rules)

            for msg1 in msgs1:
                for msg2 in msgs2:
                    matched_msgs.append(msg1 + msg2)

        return matched_msgs


class Rules(dict):
    pass

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