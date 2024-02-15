"""
Day 21, Part 1

Problem description: See https://adventofcode.com/2021/day/21

My solution:
Part 1:

"""

# Imports

# Constants

START_POS = {
    1: 8,
    2: 7,
}

WINNING_SCORE = 1000
DIE_SIZE = 100

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Die():
    '''Class for a die'''

    def __init__(self) -> None:
        '''Die object'''
        self.last_result = 0
        self.times_rolled = 0


    def roll(self) -> int:
        '''Roll a die. Return the result'''

        self.last_result += 1
        if self.last_result > DIE_SIZE:
            self.last_result = 1

        self.times_rolled += 1

        return self.last_result


class Player():
    '''Player class'''

    def __init__(self, start_pos: int) -> None:
        '''Player object.
        start_pos: Starting position'''

        self.pos = start_pos
        self.score = 0


    def play_turn(self, die: Die) -> bool:
        '''Play a turn. Return True if player wins'''
        die_result = 0

        for i in range(3):
            die_result += die.roll()

        self.pos = (((self.pos - 1) + die_result) % 10) + 1
        self.score += self.pos

        return self.score >= WINNING_SCORE


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def get_solution() -> int:
    '''Main function'''
    die = Die()
    players = {
        1: Player(START_POS[1]),
        2: Player(START_POS[2]),
    }

    winning_player = 0
    losing_player = 0

    while winning_player == 0:
        for player_nr, player in players.items():
            if player.play_turn(die):
                winning_player = player_nr
                losing_player = 3 - player_nr
                break

    return die.times_rolled * players[losing_player].score


if __name__ == '__main__':
    # lines = read_input('input.txt')
    # lines = read_input('example1.txt')
    print("Solution:", get_solution())
