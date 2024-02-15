"""
Year 2020, Day 15, Part 2

Problem description: See https://adventofcode.com/2020/day/15

"""

# Imports
from pprint import pprint
from time import process_time

# Constants

# MAX_TURNS = 2020
MAX_TURNS = 30000000
# MAX_TURNS = 7


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Game(dict):
    def __init__(self, line:str) -> None:
        elements = line.split(',')
        self.last_turn = len(elements)

        for i in range(len(elements)-1):
            self[int(elements[i])] = i + 1

        self.last_spoken = int(elements[-1])


    @property
    def age(self) -> int:
        if self.last_spoken in self.keys():
            age = self.last_turn - self[self.last_spoken]
        else:
            age = 0

        # pprint(self)
        # print(self.last_spoken, self.last_turn, age)

        return age


    def play_turn(self) -> None:
        age = self.age

        self[self.last_spoken] = self.last_turn
        self.last_turn += 1
        self.last_spoken = age



# Functions


# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    game = Game(lines[0])

    while game.last_turn < MAX_TURNS:
        game.play_turn()

        if game.last_turn % 100000 == 0:
            print(game.last_turn * 100 // MAX_TURNS, '%', int(process_time()))

    # pprint(game)

    return game.last_spoken

    return __name__


if __name__ == '__main__':
    pass