"""
Year 2023, Day 4

Problem description: See https://adventofcode.com/2023/day/4

The following classes are used:
- Card: This has the followint attributes:
    - score: The score that is calculated at the end.
    - nr: The card sequence number
    - wins: A list of winning numbers
    - nrs: The numbers on the card
    - copies: The number of times the card is copied (part 2)
- Cards: A dict container class of cards, using card.nr as key.

Part 1: For each card, check for each number if it is in the winning list and then double
the score (or set to 1 if is still 0)

For part 2, the copies attribute was introduced. For each card, we first calculate the number
of wins and then increase the copies attribute for all cards below that. We increase it by the
amount of copies that was already calculate for the card in hand.

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
        # Will contain the score in the end
        self.score = 0
        card_info, rest = line.split(':')
        card_str, card_nr_str = card_info.split()
        self.nr = int(card_nr_str)
        (win_str, nrs_str) = rest.split('|')
        self.wins = [int(n) for n in win_str.split()]
        self.nrs = [int(n) for n in nrs_str.split()]
        # Number of copies of the card (part 2)
        self.copies = 1


    def calculate_score(self) -> None:
        '''Calculate and populate the score for a card'''

        # For each number on the card
        for nr in self.nrs:
            # Check if nr is in the winning numbers list
            if nr in self.wins:
                # If no score yet, set to 1
                if self.score == 0:
                    self.score = 1
                # Otherwise double it
                else:
                    self.score *=2


    def count_winning_nrs(self) -> int:
        '''Return the number of winning cards'''
        result = 0

        # Check for each number is it is in the winning list
        for nr in self.nrs:
            if nr in self.wins:
                result += 1

        return result
    

    def expand(self, cards) -> None:
        '''Expand the cards object, based on the winning numbers on this card'''
        wins = self.count_winning_nrs()

        # Increase the copies of the cards below this one with the amount of copies that
        # this cards has itself.
        for i in range(self.nr+1, self.nr+1+wins):
            cards[i].copies += self.copies


class Cards(dict):
    '''Container class of Card objects. Key is the card nr'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            new_card = Card(line)
            self[new_card.nr] = new_card


    def calculate_score(self) -> None:
        '''Fill the Card.score for each card'''
        for card in self.values():
            card.calculate_score()


    def expand(self):
        '''Expand all the cards, based on the winning numbers (part 2 solution)'''
        for card in self.values():
            card.expand(self)


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    cards = Cards(lines)
    cards.calculate_score()

    # Return the sum of all the scores
    return sum([ c.score for c in cards.values()])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    cards = Cards(lines)
    cards.expand()

    # Add up all the copies of all cards
    return sum([ c.copies for c in cards.values()])

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass