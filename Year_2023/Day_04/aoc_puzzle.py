"""
Year 2023, Day 4

Problem description: See https://adventofcode.com/2023/day/4

"""

# Imports
from pprint import pprint

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


# Classes
class Card():
    '''Card containing a list of numbers and winning nummbers'''

    def __init__(self, line: str) -> None:
        self.score = 0
        card_info, rest = line.split(':')
        card_str, card_nr_str = card_info.split()
        self.nr = int(card_nr_str)
        (win_str, nrs_str) = rest.split('|')
        self.wins = [int(n) for n in win_str.split()]
        self.nrs = [int(n) for n in nrs_str.split()]
        self.copies = 1


    def calculate_score(self) -> None:
        for nr in self.nrs:
            if nr in self.wins:
                if self.score == 0:
                    self.score = 1
                else:
                    self.score *=2


    def count_winning_nrs(self) -> int:
        result = 0
        for nr in self.nrs:
            if nr in self.wins:
                result += 1

        return result
    

    def expand(self, cards) -> None:
        wins = self.count_winning_nrs()

        for i in range(self.nr+1, self.nr+1+wins):
            cards[i].copies += self.copies


class Cards(dict):
    '''Container class of Card objects. Key is the card nr'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            new_card = Card(line)
            self[new_card.nr] = new_card


    def calculate_score(self) -> None:
        for card in self.values():
            card.calculate_score()


    def expand(self):
        for card in self.values():
            card.expand(self)


# Main functions
def get_solution_part1(lines: list[str]) -> int:
    '''Main function'''

    cards = Cards(lines)
    cards.calculate_score()

    return sum([ c.score for c in cards.values()])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str]) -> int:
    '''Main function'''

    cards = Cards(lines)
    cards.expand()

    return sum([ c.copies for c in cards.values()])

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass