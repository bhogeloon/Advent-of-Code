"""
Year 2022, Day 2, Part 1

Problem description: See https://adventofcode.com/2022/day/2

"""

# Imports
from pprint import pprint

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Rps():
    '''Rock Paper Scissors round'''

    def __init__(self, line: str) -> None:
        opp_char = line[0]
        own_char = line[2]

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

        return

    def get_score(self) -> int:
        '''Calculate total score'''

        score = self.own_val
        result = self.opp_val - self.own_val

        if result < 0:
            result += 3

        if result == 0:
            score += 3
        elif result == 1:
            pass
        elif result == 2:
            score += 6
        else:
            raise RuntimeError('Unexpected result: {}'.format(result))

        return score


# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    total_score = 0

    for line in lines:
        rps = Rps(line)
        total_score += rps.get_score()
    
    return total_score

    # return __name__


if __name__ == '__main__':
    pass