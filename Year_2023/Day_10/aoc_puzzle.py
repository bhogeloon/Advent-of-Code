"""
Year 2023, Day 10

Problem description: See https://adventofcode.com/2023/day/10

"""

# Imports
from pprint import pprint
import numpy as np

# Constants

UUCODE_TABLE = {
    '|': '\u2502',
    '-': '\u2501',
    'L': '\u2515',
    'J': '\u2519',
    '7': '\u2511',
    'F': '\u250d',
}

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


# Classes
class Pipe():
    '''A Pipe object is an element in the grid connecting to two directions
    (or empty list, in case of .)'''

    def __init__(self, char: str, x: int, y: int, test=False) -> None:
        self.x = x
        self.y = y

        if char == 'S':
            if test:
                self.char = '7'
            else:
                self.char = '|'
            self.start = True
            self.distance = 0 
        else:
            self.char = char
            self.start = False
            self.distance = -1


    def set_relations(self, grid) -> None:
        self.neighbors = []

        if self.char == '.':
            return
        elif self.char == '|':
            nb_x = (self.x, self.x)
            nb_y = (self.y-1, self.y+1)
        elif self.char == '-':
            nb_x = (self.x-1, self.x+1)
            nb_y = (self.y, self.y)
        elif self.char == 'L':
            nb_x = (self.x, self.x+1)
            nb_y = (self.y-1, self.y)
        elif self.char == 'J':
            nb_x = (self.x, self.x-1)
            nb_y = (self.y-1, self.y)
        elif self.char == '7':
            nb_x = (self.x-1, self.x)
            nb_y = (self.y, self.y+1)
        elif self.char == 'F':
            nb_x = (self.x, self.x+1)
            nb_y = (self.y+1, self.y)
        else:
            raise RuntimeError("Unknown char: {}".format(self.char))
        
        for i in range(2):
            if nb_x[i] < 0 or nb_x[i] >= grid.x_size or \
                nb_y[i] < 0 or nb_y[i] >= grid.y_size:
                self.neighbors.append(None)
            else:
                self.neighbors.append(grid.pipes[nb_x[i],nb_y[i]])



    def get_next_pipe(self, prev_pipe):
        for nb in self.neighbors:
            # if (nb.x, nb.y) != (prev_pipe.x, prev_pipe.y):
            if nb != prev_pipe:
                return nb



class Grid():
    '''The grid containing all the pipes'''

    def __init__(self, lines: list[str], test=False) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        self.pipes = np.full((self.x_size, self.y_size), None)

        for y in range(self.y_size):
            for x in range(self.x_size):
                self.pipes[x,y] = Pipe(lines[y][x],x,y,test=test)
                if self.pipes[x,y].start:
                    self.start = self.pipes[x,y]


    def set_relations(self) -> None:
        for y in range(self.y_size):
            for x in range(self.x_size):
                self.pipes[x,y].set_relations(self)


    def get_max_distance(self) -> None:
        for i in range(2):
            self.discover_path(i)


    def discover_path(self, i: int) -> None:
        steps = 1
        prev_pipe = self.start
        cur_pipe = prev_pipe.neighbors[i]

        while True:
            if cur_pipe.distance < 0 or cur_pipe.distance > steps:
                cur_pipe.distance = steps
    
            next_pipe = cur_pipe.get_next_pipe(prev_pipe)

            if next_pipe.start:
                break

            steps += 1
            prev_pipe = cur_pipe
            cur_pipe = next_pipe


    def print_distances(self) -> None:
        for y in range(self.y_size):
            line = ''
            for x in range(self.x_size):
                distance = self.pipes[x,y].distance
                if distance < 0:
                    line += '.'
                else:
                    line += str(distance)
            print(line)


    def print_map(self) -> None:
        for y in range(self.y_size):
            line = ''
            for x in range(self.x_size):
                distance = self.pipes[x,y].distance
                if distance < 0:
                    line += '.'
                else:
                    line += UUCODE_TABLE[self.pipes[x,y].char]
            print(line)


# Main functions
def get_solution_part1(lines: list[str], test=False) -> int:
    '''Main function'''

    grid = Grid(lines,test=test)
    grid.set_relations()
    grid.get_max_distance()

    # grid.print_distances()
    grid.print_map()

    return max([p.distance for p in grid.pipes.flat ])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], test=False) -> int:
    '''Main function'''

    map = []

    for line in lines:
        for char in line:
            map.append(char)

    pprint(map)

    return map.count('I')

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass