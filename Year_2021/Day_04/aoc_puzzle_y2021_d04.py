"""
Year 2021, Day 4

Problem description: See https://adventofcode.com/2021/day/4

We use the following classes:
- Balls: A list of numbers that represent the Bingo Balls being drawn.
- Card: A 5x5 Bingo card
- CardEntry: A single entry on a Bingo card, containing a nr and a boolean to indicate
    if it's marked or not.
- Cards: List container of Card objects

Part 1: For each ball, we mark each card and while doing that, check if it's a winner. If it is,
collect the sum of all unmarked entries and multiply that by the ball nr.

Part 2: Keep track of all the cards that have already won and if only one is left, calculate result.

"""

# Imports
from pprint import pprint
from aoc_lib.grid import Grid2D
from collections import deque

# Constants
CARD_SIZE = 5

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Balls(deque[int]):
    '''List of winning numbers'''

    def __init__(self, line: str) -> None:
        self.extend([int(nr) for nr in line.split(',')])


class CardEntry():
    '''Represents an entry on a Bingo card. It holds a number and a boolean hit.
    This is True when the entry has been called.'''

    def __init__(self, nr: int) -> None:
        self.nr = nr
        self.hit = False


class Card(Grid2D):
    '''Represents a 5x5 Bingo card'''

    def __init__(self, lines: list[str], id: int) -> None:
        self.id = id
        # Create a matrix based on lists
        matrix = []

        for line in lines:
            row = [int(nr) for nr in line.split()]
            matrix.append(row)

        # Using the matrix, fill the grid with CardEntry objects
        super().__init__(
            sizes=(CARD_SIZE,CARD_SIZE),
            func=lambda x=None,y=None,lines=lines: CardEntry(matrix[y][x]),
        )

        self.nrs = self.grid
        self.won = False


    def mark_ball(self, ball: int) -> bool:
        '''Marks a CardEntry with the matching ball number (if any).
        Returns True if anything found. Otherwise False'''

        nr_found = False

        # Mark all matching nrs
        for card in self.nrs.flat:
            if card.nr == ball:
                card.hit = True
                nr_found = True

        return nr_found
    

    def is_winner(self) -> bool:
        '''Checks if the card has a horizontal or vertical completed row and 
        returns True if so.'''

        return self.is_winner_hor() or self.is_winner_ver()


    def is_winner_hor(self) -> bool:
        '''Checks for horizontal completed rows'''

        is_winner = False

        # Look for each row
        for y in range(CARD_SIZE):
            row_complete = True

            # Within the row, check if any nr is not marked
            for x in range(CARD_SIZE):
                if not self.nrs[x,y].hit:
                    row_complete = False
                    break

            # If not, then all nrs are marked
            if row_complete:
                is_winner = True
                break

        return is_winner


    def is_winner_ver(self) -> bool:
        '''Checks for vertical completed columns'''

        is_winner = False

        # Look for each col
        for x in range(CARD_SIZE):
            col_complete = True

            # Within the col, check if any nr is not marked
            for y in range(CARD_SIZE):
                if not self.nrs[x,y].hit:
                    col_complete = False
                    break

            # If not, then all nrs are marked
            if col_complete:
                is_winner = True
                break

        return is_winner
    

    def unmarked_sum(self) -> int:
        '''Return the sum of all unmarked numbers'''

        result = 0

        # Add all nrs that are not marked
        for card_entry in self.nrs.flat:
            if not card_entry.hit:
                result += card_entry.nr

        return result


    def print(self) -> None:
        for y in range(CARD_SIZE):
            pline = ''
            for x in range(CARD_SIZE):
                if self.nrs[x,y].hit:
                    pline += ' x '
                else:
                    pline += f'{self.nrs[x,y].nr:2} '
            print(pline)


class Cards(list[Card]):
    '''List container class of Card objects'''

    def __init__(self, lines:deque[str]) -> None:
        # Ignore first line
        lines.popleft()

        # Keep reading until all cards processed
        end_reached = False
        while len(lines) > 0:
            # Ignore all empty lines
            while lines[0] == '':
                lines.popleft()
                if len(lines) == 0:
                    end_reached = True
                    break
            
            if end_reached:
                break

            # Now take 5 lines and create a card:
            card_lines =[]
            for i in range(5):
                card_lines.append(lines.popleft())

            id = len(self)
            self.append(Card(card_lines, id))


    def find_first_win(self, balls: Balls) -> int:
        '''This function will draw all balls until there is a winner.
        If there is a winner, the function will return the product of the last
        ball and the sum of all unmarked numbers'''

        # For all balls
        for ball in balls:
            # For each card
            for card in self:
                # Mark the nrs on the card and if one found
                if card.mark_ball(ball):
                    # Check if it's a winner and if so
                    if card.is_winner():
                        # Calculate the result and return it
                        return ball * card.unmarked_sum()


    def find_last_win(self, balls: Balls) -> int:
        '''This function will draw all balls until all cards are a winner.
        For the last winner, the function will return the product of the last
        ball and the sum of all unmarked numbers'''

        nr_of_cards_left = len(self)

        # For all balls
        for ball in balls:
            # For each card
            for card in self:
                # If already won, ignore
                if card.won:
                    continue

                # Mark the nrs on the card and if one found
                elif card.mark_ball(ball):
                    # Check if it's a winner and if so
                    if card.is_winner():
                        # Check if this is the only one left:
                        if nr_of_cards_left == 1:
                            # Calculate the result and return it
                            return ball * card.unmarked_sum()
                        else:
                            card.won = True
                            nr_of_cards_left -= 1


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    # Use first line to create the balls
    balls = Balls(lines[0])
    # Use the complete set to create the cards
    cards = Cards(deque(lines))

    return cards.find_first_win(balls)

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    # Use first line to create the balls
    balls = Balls(lines[0])
    # Use the complete set to create the cards
    cards = Cards(deque(lines))

    return cards.find_last_win(balls)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
