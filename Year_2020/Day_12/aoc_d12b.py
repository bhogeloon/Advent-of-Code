"""
Year 2020, Day 12, Part 2

Problem description: See https://adventofcode.com/2020/day/12

"""

# Imports
from pprint import pprint
from collections import deque

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes
class Ship():
    def __init__(self, lines: list[str]) -> None:
        self.pos = (0,0)
        self.dir = (10,1)
        self.instructions = deque()

        for line in lines:
            instruction = {}
            instruction['cmd'] = line[0]
            instruction['amount'] = int(line[1:])
            self.instructions.append(instruction)


    def move(self):
        instruction = self.instructions.popleft()

        if instruction['cmd'] == 'R' or instruction['cmd'] == 'L':
            nr_turns = instruction['amount'] // 90
            if instruction['cmd'] == 'R':
                for i in range(nr_turns):
                    self.dir = (self.dir[1], -self.dir[0])
            elif instruction['cmd'] == 'L':
                for i in range(nr_turns):
                    self.dir = (-self.dir[1], self.dir[0])

            return

        if instruction['cmd'] == 'F':
            self.pos = (
                self.pos[0] + instruction['amount'] * self.dir[0],
                self.pos[1] + instruction['amount'] * self.dir[1],
            )
            return

        if instruction['cmd'] == 'E':
            chdir = (1,0)
        elif instruction['cmd'] == 'S':
            chdir = (0,-1)
        elif instruction['cmd'] == 'W':
            chdir = (-1,0)
        elif instruction['cmd'] == 'N':
            chdir = (0,1)
        elif instruction['cmd'] == 'F':
            chdir = self.dir
        else:
            raise RuntimeError('Invalid command {}'.format(instruction['cmd']))

        self.dir = (
            self.dir[0] + instruction['amount'] * chdir[0],
            self.dir[1] + instruction['amount'] * chdir[1],
        )


    def move_all(self):
        while len(self.instructions) > 0:
            self.move()


    def get_manhattan_dist(self) -> int:
        return abs(self.pos[0]) + abs(self.pos[1])


# Functions



# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    ship = Ship(lines)

    ship.move_all()

    return ship.get_manhattan_dist()

    return __name__


if __name__ == '__main__':
    pass