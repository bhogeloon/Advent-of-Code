"""
Year 2023, Day 2

Problem description: See https://adventofcode.com/2023/day/2

"""

# Imports
from pprint import pprint

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


# Classes
class Bag(dict):
    '''Bag containing a number of cubes of color red green and blue'''

    def __init__(self, reds: int, greens: int, blues: int) -> None:
        self['red'] = reds
        self['green'] = greens
        self['blue'] = blues


    def increase(self, colour: str, amount: int) -> None:
        '''Increase the amount of balls of the specified colour'''
        self[colour] += amount


    def calculate_power(self) -> int:
        result = 1
        for amount in self.values():
            result *= amount

        return result


class Game(list):
    '''A game containing a number of turns'''
    
    def __init__(self, line: str) -> None:
        # Extract game id string
        (id_string, rest_string) = line.split(':')
        self.id = int(id_string.split()[1])
        # Split the turns
        turn_strings = rest_string.split(';')
        self.turns = []

        for turn_string in turn_strings:
            self.turns.append(Turn(turn_string))


    def is_possible(self, max_bag: Bag) -> bool:
        '''Check if the game is possible'''
        for turn in self.turns:
            if not turn.is_possible(max_bag):
                return False
            
        return True
        

    def calculate_power(self) -> int:
        self.min_bag = Bag(0,0,0)

        for turn in self.turns:
            for (colour, amount) in turn.mini_bag.items():
                if amount > self.min_bag[colour]:
                    self.min_bag[colour] = amount

        return self.min_bag.calculate_power()


class Turn():
    '''A turn reveiling a number of cubes (red, green and blue)'''
    
    def __init__(self, line: str) -> None:
        # Create mini-bag with balls presented in turn
        self.mini_bag = Bag(reds=0, greens=0, blues=0)
        # split the line
        ball_strings = line.split(',')

        # seperate amount and colour
        for ball_string in ball_strings:
            (amount_string, colour) = ball_string.split()
            amount = int(amount_string)
            self.mini_bag.increase(colour, amount)


    def is_possible(self, max_bag) -> bool:
        '''Check if a single turn is possible'''
        for (colour, amount) in self.mini_bag.items():
            if amount > max_bag[colour]:
                return False
            
        return True


class Games(list):
    '''Collection of games'''
    
    def __init__(self, lines: list[str]) -> None:
        self.sum_of_possible_game_ids = 0
        self.sum_of_powers = 0

        for line in lines:
            self.append(Game(line))


    def check_possible(self, max_bag) -> None:
        for game in self:
            if game.is_possible(max_bag):
                self.sum_of_possible_game_ids += game.id


    def calculate_sum_of_powers(self) -> None:
        for game in self:
            self.sum_of_powers += game.calculate_power()


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    # Create bag with maximum amount of cubes
    max_bag = Bag(12,13,14)

    # Create games
    games = Games(lines)
    games.check_possible(max_bag)

    return games.sum_of_possible_game_ids

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    games = Games(lines)
    games.calculate_sum_of_powers()

    return games.sum_of_powers

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass