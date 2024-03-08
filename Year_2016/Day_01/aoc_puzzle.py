"""
Year 2016, Day 1

Problem description: See https://adventofcode.com/2016/day/1

I created the following classes:
- Instruction: contains a turn (L or R) and a nr (amount of steps)
- Instructions: container class
- Position: keeps track of the position coordinates (x and y) and
of the direction we are walking (dir)

Part 1: Follow the path keeping track of the position. The starting
position is (0,0) so in the end the length of the path is the absolute
value of x and y added up together.

For part 2 we have to follow the path one step at the time and
then keep track in a tuple which locations we have already
visited. As soon as we find a duplicate, we can stop.
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
    
class Instruction():
    '''An Instruction contains a turn (L or R) and a nr (amount of steps)'''
    def __init__(self, word: str) -> None:
        # First part is the turn
        self.turn = word[0]
        # The remainder is the amount
        self.nr = int(word[1:])


class Instructions(list[Instruction]):
    '''Container class (list) of Instruction objects'''
    def __init__(self, line:str) -> None:
        # Extract all the instructions
        instr_words = line.split(', ')

        for word in instr_words:
            self.append(Instruction(word))


class Position():
    '''Position contains dir (direction, NESW) and x and y coordinates'''
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.dir = 'N'


    def follow_path(self, intrs: Instructions) -> None:
        '''Change the position following the Instructions'''
        for instr in intrs:
            self.change_pos(instr)


    def change_pos(self, instr: Instruction) -> None:
        '''Change the position based on the instruction'''
        self.change_dir(instr.turn)
        self.move(instr.nr)


    def change_dir(self, turn: str) -> None:
        '''Change the direction based on the instruction turn'''
        if turn == 'L':
            if self.dir == 'N':
                self.dir = 'W'
            elif self.dir == 'W':
                self.dir = 'S'
            elif self.dir == 'S':
                self.dir = 'E'
            elif self.dir == 'E':
                self.dir = 'N'
        elif turn == 'R':
            if self.dir == 'N':
                self.dir = 'E'
            elif self.dir == 'W':
                self.dir = 'N'
            elif self.dir == 'S':
                self.dir = 'W'
            elif self.dir == 'E':
                self.dir = 'S'


    def move(self, nr: int) -> None:
        '''Move in the direction dir nr of steps'''
        if self.dir == 'N':
            self.y += nr
        elif self.dir == 'E':
            self.x += nr
        elif self.dir == 'S':
            self.y -= nr
        elif self.dir == 'W':
            self.x -= nr


    def find_duplicate(self, intrs) -> int:
        '''This function finds the answer on part 2, so the
        first postion visited twice'''
        found_positions = []

        for instr in intrs:
            # First change direction
            self.change_dir(instr.turn)

            # Now go forward one by one
            for step in range(instr.nr):
                self.move(1)

                # Now check if you have been there before
                if (self.x, self.y) in found_positions:
                    return self.get_distance()
                else:
                    # Add to positions visited
                    found_positions.append((self.x, self.y))


    def get_distance(self) -> int:
        '''Get the distance to the starting point'''
        # The distance is the abolute values of x and y added up
        # as the starting point is (0,0)
        return abs(self.x) + abs(self.y)


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    instrs = Instructions(lines[0])
    pos = Position()
    pos.follow_path(instrs)

    return pos.get_distance()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    instrs = Instructions(lines[0])
    pos = Position()

    return pos.find_duplicate(instrs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
