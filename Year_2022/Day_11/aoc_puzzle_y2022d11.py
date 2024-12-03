"""
Year 2022, Day 11

Problem description: See https://adventofcode.com/2022/day/11

The following classes are used:
- Monkey: A monkey containing several items with worry levels
- Monkeys: List container class of Monkey objects.

Part 1: First read in all the data for each Monkey:
- Worry level for each item they are holding
- The operation they need to perform on the worry level
- The test they need to do after they divide the level by 3
- The action they need to perform depening on the test (True and False)
Then play 20 rounds according to these rules. Assign an item to the end of the
items list of the next Monkey. In the mean time keep track of all the items that
have been inspected for each Monkey.
After 20 rounds, get the two most active monkeys by looking at the amount of
inspected items. Multiply these together.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from collections import deque
import re


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

class Monkey():
    '''Monkey'''

    def __init__(self, lines:deque[str], nr: int) -> None:
        self.insp_items = 0
        self.nr = nr
        lines.popleft()
        self._init_items(lines.popleft())
        self._init_operation(lines.popleft())
        self._init_modulus(lines.popleft())
        self._init_action_true(lines.popleft())
        self._init_action_false(lines.popleft())
        # If not end of file
        if len(lines) > 0:
            lines.popleft()


    def _init_items(self, line:str):
        # Get the initial items
        m = re.match(r'  Starting items: (.*)$', line)
        self.items = deque(int(item_str) for item_str in m.group(1).split(', '))


    def _init_operation(self, line:str):
        '''Get the monkey operation attributes'''
        m = re.match(r'  Operation: new = old ([*+]) (.*)$', line)

        # Assign operation to the right function
        if m.group(2) == 'old':
            self.operation = self.sqr
        elif m.group(1) == '+':
            self.oper_arg = int(m.group(2))
            self.operation = self.add
        elif m.group(1) == '*':
            self.oper_arg = int(m.group(2))
            self.operation = self.multiply


    def _init_modulus(self, line:str):
        '''Get the 'divisible by' test'''
        m = re.match(r'  Test: divisible by (.*)$', line)
        self.modulus = int(m.group(1))


    def _init_action_true(self, line:str):
        '''Store the action to be done when test is True'''
        m = re.match(r'\s*If true: throw to monkey (.*)$', line)
        self.next_if_true = int(m.group(1))


    def _init_action_false(self, line:str):
        '''Store the action to be done when test is True'''
        m = re.match(r'\s*If false: throw to monkey (.*)$', line)
        self.next_if_false = int(m.group(1))


    def sqr(self, x:int) -> int:
        '''operation sqr'''
        return x ** 2


    def add(self, x:int) -> int:
        '''operation add'''
        return x + self.oper_arg


    def multiply(self, x:int) -> int:
        '''operation multiply'''
        return x * self.oper_arg


    def turn(self, monkeys: Monkeys) -> None:
        '''Play one turn for this Monkey'''
        while len(self.items) > 0:
            self.process_item(self.items.popleft(), monkeys)


    def process_item(self, item: int, monkeys: Monkeys) -> None:
        '''Play the turn for one item'''
        # Apply operation
        item = self.operation(item)

        if not monkeys.worry:
            # Divide worry level by 3
            item = item // 3

        item = item % monkeys.common_mod

        # If division is possible perform True action, otherwise False
        if item % self.modulus == 0:
            monkeys[self.next_if_true].items.append(item)
        else:
            monkeys[self.next_if_false].items.append(item)

        # Increase the inspected items by this Monkey
        self.insp_items += 1


class Monkeys(list[Monkey]):
    '''Container class for monkeys'''

    def __init__(self, lines: deque[str], worry = False) -> None:
        self.worry = worry
        self.common_mod = 1
        # Index number of Monkey
        nr = 0

        while len(lines) > 0:
            self.append(Monkey(lines, nr))
            nr += 1
            self.common_mod = self.common_mod * self[-1].modulus


    def round(self) -> None:
        '''Play one round for each Monkey'''
        for monkey in self:
            monkey.turn(self)


    def get_monkey_business(self) -> int:
        '''Get the two most active Monkeys and multiply the amount of
        inspected items for those Monkeys'''
        insp_items = []

        for monkey in self:
            insp_items.append(monkey.insp_items)

        max1 = max(insp_items)
        insp_items.remove(max1)
        max2 = max(insp_items)

        return max1 * max2


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    monkeys = Monkeys(deque(lines))

    # Play 20 rounds
    for i in range(20):
        monkeys.round()

    return monkeys.get_monkey_business()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
