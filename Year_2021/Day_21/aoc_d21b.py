"""
Day 21, Part 1

Problem description: See https://adventofcode.com/2021/day/21

My solution:
Part 1:

"""

# Imports
import copy

# Constants

START_POS = {
    1: 8,
    2: 7,
}

WINNING_SCORE = 21

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

    progress = []


# Classes

class Player():
    '''Player class'''

    total_wins = {
        1: 0,
        2: 0,
    }

    def __init__(self, start_pos: int) -> None:
        '''Player object.
        start_pos: Starting position'''

        self.pos = start_pos
        self.score = 0


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def report_progress():
    '''print a string to report progress'''
    if sum(Player.total_wins.values()) % 100000 == 0:
        print(''.join(Gv.progress[:80]))

def play_turn(player_nr: int, turn: int, players: dict, throw):
    for nr in range(1,3):
        if players[nr].score >= WINNING_SCORE:
            Player.total_wins[nr] += 1
            report_progress()
            return

    players[player_nr].pos = (((players[player_nr].pos - 1) + throw) % 10) + 1

    for die in range(1,4):

        if turn < 3:
            new_players = copy.deepcopy(players)
            Gv.progress.append(str(die))
            play_turn(player_nr, turn + 1, new_players, die)
            Gv.progress.pop()
        else:
            players[player_nr].score += players[player_nr].pos
            new_players = copy.deepcopy(players)
            Gv.progress.append(str(die))
            play_turn(3 - player_nr, 1, new_players, die)
            Gv.progress.pop()

    return


def get_solution() -> int:
    '''Main function'''
    players = {
        1: Player(START_POS[1]),
        2: Player(START_POS[2]),
    }

    for die in range(1,4):
        Gv.progress.append(str(die))
        play_turn(1, 1, players, die)
        Gv.progress.pop()

    return max(Player.total_wins.values())


if __name__ == '__main__':
    # lines = read_input('input.txt')
    # lines = read_input('example1.txt')
    print("Solution:", get_solution())
