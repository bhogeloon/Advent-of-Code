"""
Year 2022, Day 11

Problem description: See https://adventofcode.com/2022/day/11

"""

# Imports
from pprint import pprint
from collections import deque
import re

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


# Classes

class Monkeys(list):
    '''Container class for monkeys'''

    def __init__(self, lines: deque[str], worry = False) -> None:
        self.worry = worry
        self.common_mod = 1
        nr = 0
        while len(lines) > 0:
            self.append(Monkey(lines, nr))
            nr += 1
            self.common_mod = self.common_mod * self[-1].modulus


    def round(self) -> None:
        for monkey in self:
            monkey.turn(self)


    def get_monkey_business(self) -> int:
        insp_items = []

        for monkey in self:
            insp_items.append(monkey.insp_items)

        max1 = max(insp_items)
        insp_items.remove(max1)
        max2 = max(insp_items)

        return max1 * max2


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
        lines.popleft()


    def _init_items(self, line:str):
        m = re.match(r'  Starting items: (.*)$', line)
        self.items = deque(int(item_str) for item_str in m.group(1).split(', '))


    def _init_operation(self, line:str):
        m = re.match(r'  Operation: new = old ([*+]) (.*)$', line)

        if m.group(2) == 'old':
            self.operation = self.sqr
        elif m.group(1) == '+':
            self.oper_arg = int(m.group(2))
            self.operation = self.add
        elif m.group(1) == '*':
            self.oper_arg = int(m.group(2))
            self.operation = self.multiply


    def _init_modulus(self, line:str):
        m = re.match(r'  Test: divisible by (.*)$', line)
        self.modulus = int(m.group(1))


    def _init_action_true(self, line:str):
        m = re.match(r'\s*If true: throw to monkey (.*)$', line)
        self.next_if_true = int(m.group(1))


    def _init_action_false(self, line:str):
        m = re.match(r'\s*If false: throw to monkey (.*)$', line)
        self.next_if_false = int(m.group(1))


    def sqr(self, x:int) -> int:
        return x ** 2


    def add(self, x:int) -> int:
        return x + self.oper_arg


    def multiply(self, x:int) -> int:
        return x * self.oper_arg


    def turn(self, monkeys: Monkeys) -> None:
        while len(self.items) > 0:
            self.process_item(self.items.popleft(), monkeys)


    def process_item(self, item: int, monkeys: Monkeys) -> None:
        item = self.operation(item)

        if not monkeys.worry:
            item = item // 3

        item = item % monkeys.common_mod

        if item % self.modulus == 0:
            monkeys[self.next_if_true].items.append(item)
        else:
            monkeys[self.next_if_false].items.append(item)

        self.insp_items += 1


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    monkeys = Monkeys(deque(lines))

    for i in range(20):
        monkeys.round()

    return monkeys.get_monkey_business()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    # monkeys = Monkeys(deque(lines), worry=False)
    monkeys = Monkeys(deque(lines), worry=True)

    for i in range(10000):
        monkeys.round()
        if i % 100 == 0:
            print(i)

    return monkeys.get_monkey_business()


    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass