"""
Year 2020, Day 15, Part 1

Problem description: See https://adventofcode.com/2020/day/15

"""

# Imports
from pprint import pprint
from collections import deque

# Constants

MAX_TURNS = 2020


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Game(deque[int]):
    def __init__(self, line:str) -> None:
        elements = line.split(',')
        self.extendleft(int(nr) for nr in elements)


    @property
    def last_turn(self) -> int:
        return len(self)


    @property
    def age(self) -> int:
        last_element = self[0]

        try:
            age = self.index(last_element, 1)
        except ValueError:
            age = 0

        return age


    def play_turn(self) -> None:
        self.appendleft(self.age)


# Functions


# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    game = Game(lines[0])

    while game.last_turn < MAX_TURNS:
        game.play_turn()

    # pprint(game)

    return game[0]

    return __name__


if __name__ == '__main__':
    pass