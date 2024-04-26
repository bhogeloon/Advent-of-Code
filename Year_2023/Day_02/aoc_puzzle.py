"""
Year 2023, Day 2

Problem description: See https://adventofcode.com/2023/day/2

The following classes are used:
- Bag: A dict class containing red, green and blue cubes
- Turn: A game turn revealing a number of cubes of different colors. The revealed
    cubes are put in a 'mini-bag', which is a Bag object.
- Game: A list of Turn objects. It also has an id number.
- Games: List container class of Game objects.

For part 1:
First we create a max-bag which is the bag which contains exactly the amount of cubes
to compare with in each game, so we can determine which games are possible with this
bag.
Then we create the Games from the input, keeping track of the sum of the possible
game-ids.
Then we check for each game, for each turn if the total amount of balls for each colour
is bigger than the amount in max_bag. If so, we return False. 

For part 2:
For each game, start with an empty test bag. Then go through each turn and if the amount
of cubes for a colour is bigger than the one in the in test bag, raise the amount in the
test bag. That will result in the minimum amount for each colour. Then return the product
of this.
"""

# Imports
from pprint import pprint
from math import prod

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
        '''Return the product of the amount of cubes for each colour'''
        return prod(self.values())


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
        '''Determine the minimum set of cubes and return the product
        of those numbers'''

        # Create an empty bag
        self.min_bag = Bag(0,0,0)

        for turn in self.turns:
            for (colour, amount) in turn.mini_bag.items():
                # If the amount of cubes is larger than in the min_bag,
                # Update the min_bag amount
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


class Games(list[Game]):
    '''Collection of games'''
    
    def __init__(self, lines: list[str]) -> None:
        self.sum_of_possible_game_ids = 0
        self.sum_of_powers = 0

        for line in lines:
            self.append(Game(line))


    def check_possible(self, max_bag) -> None:
        '''Check for every game if it is possible and if so add the id
        to the sum_of_possible_game_ids'''

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