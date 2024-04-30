"""
Year 2022, Day 2

Problem description: See https://adventofcode.com/2022/day/2

For this we have the following classes:
- RpsRound: One round of Rock Paper Scissors
- RpsGame: The complete game, which is a list container class of RpsRound objects

For round 1: Determine the integer value of your own choice and the opponent one
according to the given scoring table:
Rock = 1
Paper = 2
Scissors = 3
By substracting the values you can then determine the winner, e.g.
Rock - Paper = -1 (add 3 and you get 2): Paper wins
Scissors - Rock = 2: Rock wins
Paper - Rock = 1 Paper wins
Rock - Scissors = -2 (add 3 and you get 1): Rock wins
So after adding 3 to each negative value: 2 means the second wins and 1 means the first
wins. 0 means a tie.
Then calculate the total score by adding the choice value to 0, 3 or 6, depending on loose,
tie or win

For part 2: Go the other way around. Depending on whether you need to win, tie or loose which
value is required (using the same calculation). Then calculate the score. 
"""

# Imports
from pprint import pprint


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class RpsRound():
    '''Rock Paper Scissors round'''

    def __init__(self, line: str) -> None:
        # Get opponent and own character
        self.opp_char = line[0]
        self.own_char = line[2]


    def play_game1(self) -> None:
        '''Play the game according to part 1'''
        opp_char = self.opp_char
        own_char = self.own_char

        # Determine the value for the opponent. Will be used to
        # calculate the winner.
        if opp_char == 'A':
            self.opp_str = 'rock'
            self.opp_val = 1
        elif opp_char == 'B':
            self.opp_str = 'paper'
            self.opp_val = 2
        elif opp_char == 'C':
            self.opp_str = 'scissors'
            self.opp_val = 3
        else:
            raise RuntimeError('Unknown code for opponent: {}'.format(opp_char))

        # Determine the value belonging to the choice
        # That also matches the first part of the score
        if own_char == 'X':
            self.own_str = 'rock'
            self.own_val = 1
        elif own_char == 'Y':
            self.own_str = 'paper'
            self.own_val = 2
        elif own_char == 'Z':
            self.own_str = 'scissors'
            self.own_val = 3
        else:
            raise RuntimeError('Unknown code for your self: {}'.format(own_char))


    def play_game2(self):
        '''Play the game according to part 2 (second column is the outcome)'''
        opp_char = self.opp_char
        own_char = self.own_char

        # Set the value of the opponents choice
        if opp_char == 'A':
            self.opp_val = 1
        elif opp_char == 'B':
            self.opp_val = 2
        elif opp_char == 'C':
            self.opp_val = 3
        else:
            raise RuntimeError('Unknown code for opponent: {}'.format(opp_char))

        # Determine what you will choose as your own choice, based on the
        # desired outcome

        # If we need to win this one
        if own_char == 'X':
            # Set your own value one lower (so you will loose)
            self.own_val = self.opp_val - 1

            # If 0, reset to 3
            if self.own_val == 0:
                self.own_val = 3

            # Set the score to the choice value (winning score is 0)
            self.score = self.own_val

        # If we need to tie
        elif own_char == 'Y':
            # Set your own value equal to the opponents
            self.own_val = self.opp_val

            # Score is choice value + 3 (for tie)
            self.score = self.own_val + 3

        # If we need to win
        elif own_char == 'Z':
            # Set your own choice 1 higher, so you can win
            self.own_val = self.opp_val + 1

            # If 4, reset to 1
            if self.own_val == 4:
                self.own_val = 1

            # The score is the choice value + 6 (for a win)
            self.score = self.own_val + 6
        else:
            raise RuntimeError('Unknown code for your self: {}'.format(own_char))


    def get_score1(self) -> int:
        '''Calculate total score'''

        # Initial score is determined by your own choice
        score = self.own_val

        # Start to calculate winner by looking at difference between values
        result = self.opp_val - self.own_val

        # If result is negative, then add 3, as it is a rotating win
        if result < 0:
            result += 3

        # Determine winner based 3 beats 2 beats 1 beats 3
        # If result = 0, it is a draw
        if result == 0:
            score += 3
        # If result is 1, I have lost
        elif result == 1:
            pass
        # If result os 2, I have won
        elif result == 2:
            score += 6
        else:
            raise RuntimeError('Unexpected result: {}'.format(result))

        return score


class RpsGame(list[RpsRound]):
    '''Complete Rock Paper Scissors game. This is a list container class of
    RpsRound objects'''
    
    def __init__(self, lines: list[str]) -> None:
        self.total_score = 0

        for line in lines:
            self.append(RpsRound(line))


    def play_game1(self) -> None:
        '''Play the game according to part 1'''
        for rps in self:
            rps.play_game1()


    def play_game2(self) -> None:
        '''Play the game according to part 2'''
        score = 0

        for rps in self:
            rps.play_game2()
            score += rps.score

        return score


    def get_score1(self) -> int:
        '''Calculate the score after playing game 1'''
        total_score = 0

        for rps in self:
            total_score += rps.get_score1()

        return total_score


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    rpsgame = RpsGame(lines)
    rpsgame.play_game1()
    
    return rpsgame.get_score1()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    rpsgame = RpsGame(lines)
    return rpsgame.play_game2()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
