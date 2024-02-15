"""
Year 2023, Day 7

Problem description: See https://adventofcode.com/2023/day/7

"""

# Imports
from pprint import pprint

# Constants
CARD_TRANS = {
    'A': 'z',
    'K': 'y',
    'Q': 'x',
    'J': 'w',
    'T': 'v',
}

CARD_TRANS_JKR = {
    'A': 'z',
    'K': 'y',
    'Q': 'x',
    'J': '1',
    'T': 'v',
}


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''



# Classes
class Hand():
    '''Camel card hand plus bid'''

    def __init__(self, line: str) -> None:
        self.cards, bid_str = line.split()
        self.bid = int(bid_str)
        self.rank = 0


    def translate(self) -> None:
        self.trans_cards = self.cards

        for orig_c, new_c in CARD_TRANS.items():
            self.trans_cards = self.trans_cards.replace(orig_c, new_c)


    def translate_jkr(self) -> None:
        self.trans_cards = self.cards

        for orig_c, new_c in CARD_TRANS_JKR.items():
            self.trans_cards = self.trans_cards.replace(orig_c, new_c)


    def set_type(self) -> None:
        '''Determine type of hand'''
        card_set = set(self.cards)

        if len(card_set) == 1:
            # This must be 'Five of a kind'
            self.type = '7'
        elif len(card_set) == 2:
            # Can be 'Four of a kind' or 'Full House'
            cnt = self.cards.count(self.cards[0])
            if cnt == 2 or cnt == 3:
                # 'Full House'
                self.type = '5'
            else:
                # 'Four of a kind'
                self.type = '6'
        elif len(card_set) == 3:
            # 'Three of a kind' or 'Two pair'
            for card in self.cards:
                cnt = self.cards.count(card)
                if cnt == 3:
                    # Three of a kind
                    self.type = '4'
                    break
                elif cnt == 2:
                    # Two pairs
                    self.type = '3'
                    break
        elif len(card_set) == 4:
            # 'One pair'
            self.type = '2'
        else:
            # 'High card'
            self.type = '1'

        self.sort_string = self.type + self.trans_cards


    def set_type_jkr(self) -> None:
        # First determine the number of Jokers:
        nr_of_jkrs = self.cards.count('J')
        card_set = set(self.cards)

        # If no Jokers, just process as normal
        if nr_of_jkrs == 0:
            return self.set_type()
        
        # If 5 or 4 Jokers, make it 'Five of a kind'
        elif nr_of_jkrs >= 4:
            self.type = '7'

        # Also, if there are only two card types, it is
        # still 'Five of a kind'
        elif len(card_set) == 2:
            self.type = '7'

        # If 3 Jokers, it must now be 'Four of a kind'
        elif nr_of_jkrs == 3:
            self.type = '6'

        # When there 2 Jokers and only 3 types, we
        # can also make it 'Four of a kind'
        elif nr_of_jkrs == 2:
            if len(card_set) == 3:
                self.type = '6'
            # And otherwise it is 'Three of a kind'
            else:
                self.type = '4'

        # What is now left is on Joker
        # If 5 different types, it can only be One pair
        elif len(card_set) == 5:
            self.type = '2'

        # If 4 different types, it can only be 'Three of a kind'
        elif len(card_set) == 4:
            self.type = '4'

        # What is left is 1 Joker and 2 types
        else:
            for card in self.cards:
                if card == 'J':
                    continue
                elif self.cards.count(card) == 2:
                    # This must be 'Full House'
                    self.type = '5'
                    break
                else:
                    # Otherwise 'Four of a kind'
                    self.type = '6'
                    break

        # print(self.cards)
        self.sort_string = self.type + self.trans_cards


class Hands(list):
    '''Container class for Hand objects'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Hand(line))


    def translate(self) -> None:
        for hand in self:
            hand.translate()


    def translate_jkr(self) -> None:
        for hand in self:
            hand.translate_jkr()


    def set_type(self) -> None:
        for hand in self:
            hand.set_type()


    def set_type_jkr(self) -> None:
        for hand in self:
            hand.set_type_jkr()


    def rank(self) -> None:
        for i, hand in enumerate(self):
            hand.rank = i + 1


# Main functions
def get_solution_part1(lines: list[str]) -> int:
    '''Main function'''

    hands = Hands(lines)
    hands.translate()
    hands.set_type()
    hands.sort(key=lambda hand: hand.sort_string)
    # pprint([h.cards for h in hands])
    hands.rank()

    return sum([h.rank * h.bid for h in hands])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str]) -> int:
    '''Main function'''

    hands = Hands(lines)
    hands.translate_jkr()
    hands.set_type_jkr()
    hands.sort(key=lambda hand: hand.sort_string)
    # pprint([h.cards for h in hands])
    hands.rank()

    return sum([h.rank * h.bid for h in hands])

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass