"""
Year 2023, Day 10

Problem description: See https://adventofcode.com/2023/day/10

"""

# Imports
from pprint import pprint
import numpy as np

# Constants

MAX_ROUNDS = 25

UUCODE_TABLE = {
    '|': '\u2502',
    '-': '\u2501',
    'L': '\u2515',
    'J': '\u2519',
    '7': '\u2511',
    'F': '\u250d',
}

START_CHAR = '|'
START_CHAR_TST = '7'

START_ORI = {
    'out_x': 1,
    'out_y': 0,
    'in_x': -1,
    'in_y': 0,
}

START_ORI_TST = {
    'out_x': 1,
    'out_y': -1,
    'in_x': -1,
    'in_y': 1,
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
                self.char = START_CHAR_TST
            else:
                self.char = START_CHAR
            self.start = True
            self.distance = 0
            self.status = 'L'
        else:
            self.char = char
            self.start = False
            self.distance = -1
            self.status = 'U'


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


    def set_neighbor_status(self, grid) -> None:
        '''Set neighbors status as either Inside or Outside'''
        if self.char == '|' or self.char == '-':
            self._set_neighbor_status_straight(grid)
        elif self.char == 'L':
            self._set_neighbor_status_ne(grid)
        elif self.char == 'J':
            self._set_neighbor_status_nw(grid)
        elif self.char == '7':
            self._set_neighbor_status_sw(grid)
        elif self.char == 'F':
            self._set_neighbor_status_se(grid)


    def _set_neighbor_status_straight(self, grid) -> None:
        '''In case of "|" or "-"'''
        # First Inside
        nb_x = self.x + self.ori['in_x']
        nb_y = self.y + self.ori['in_y']
        self._set_nb_io(nb_x, nb_y, 'I', grid)

        # Then Outside
        nb_x = self.x + self.ori['out_x']
        nb_y = self.y + self.ori['out_y']
        self._set_nb_io(nb_x, nb_y, 'O', grid)


    def _set_neighbor_status_ne(self, grid) -> None:
        '''in case of "L"'''
        if self.ori['in_x'] == -1:
            io = 'I'
        else:
            io = 'O'

        nb_x = self.x - 1
        nb_y = self.y
        self._set_nb_io(nb_x, nb_y, io, grid)

        nb_x = self.x
        nb_y = self.y + 1
        self._set_nb_io(nb_x, nb_y, io, grid)

        nb_x = self.x - 1
        nb_y = self.y + 1
        self._set_nb_io(nb_x, nb_y, io, grid)


    def _set_neighbor_status_nw(self, grid) -> None:
        '''in case of "J"'''
        if self.ori['in_x'] == 1:
            io = 'I'
        else:
            io = 'O'

        nb_x = self.x + 1
        nb_y = self.y
        self._set_nb_io(nb_x, nb_y, io, grid)

        nb_x = self.x
        nb_y = self.y + 1
        self._set_nb_io(nb_x, nb_y, io, grid)

        nb_x = self.x + 1
        nb_y = self.y + 1
        self._set_nb_io(nb_x, nb_y, io, grid)


    def _set_neighbor_status_sw(self, grid) -> None:
        '''in case of "7"'''
        if self.ori['in_x'] == 1:
            io = 'I'
        else:
            io = 'O'

        nb_x = self.x + 1
        nb_y = self.y
        self._set_nb_io(nb_x, nb_y, io, grid)

        nb_x = self.x
        nb_y = self.y - 1
        self._set_nb_io(nb_x, nb_y, io, grid)

        nb_x = self.x + 1
        nb_y = self.y - 1
        self._set_nb_io(nb_x, nb_y, io, grid)


    def _set_neighbor_status_se(self, grid) -> None:
        '''in case of "F"'''
        if self.ori['in_x'] == -1:
            io = 'I'
        else:
            io = 'O'

        nb_x = self.x - 1
        nb_y = self.y
        self._set_nb_io(nb_x, nb_y, io, grid)

        nb_x = self.x
        nb_y = self.y - 1
        self._set_nb_io(nb_x, nb_y, io, grid)

        nb_x = self.x - 1
        nb_y = self.y - 1
        self._set_nb_io(nb_x, nb_y, io, grid)


    def _set_nb_io(self, nb_x, nb_y, io, grid) -> None:
        if nb_x >= 0 and nb_x < grid.x_size and \
            nb_y >= 0 and nb_y < grid.y_size:
            if grid.pipes[nb_x,nb_y].status == 'U':
                grid.pipes[nb_x,nb_y].status = io
                # print("setting status to {} for {},{}".format(io, nb_x, nb_y))


    def set_ori(self, prev_pipe) -> None:
        self.status = 'L'
        # print('setting status to L for {},{}'.format(self.x, self.y))

        if self.char == '-':
            self._set_ori_hor(prev_pipe)
        elif self.char == '|':
            self._set_ori_ver(prev_pipe)
        elif self.char == 'L':
            self._set_ori_ne(prev_pipe)
        elif self.char == 'J':
            self._set_ori_nw(prev_pipe)
        elif self.char == '7':
            self._set_ori_sw(prev_pipe)
        elif self.char == 'F':
            self._set_ori_sw(prev_pipe)


    def _set_ori_hor(self, prev_pipe) -> None:
        if prev_pipe.ori['in_y'] == 1:
            self.ori = {
                'in_x': 0,
                'in_y': 1,
                'out_x': 0,
                'out_y': -1,
            }
        else:
            self.ori = {
                'in_x': 0,
                'in_y': -1,
                'out_x': 0,
                'out_y': 1,
            }


    def _set_ori_ver(self, prev_pipe) -> None:
        if prev_pipe.ori['in_x'] == 1:
            self.ori = {
                'in_x': 1,
                'in_y': 0,
                'out_x': -1,
                'out_y': 0,
            }
        else:
            self.ori = {
                'in_x': -1,
                'in_y': 0,
                'out_x': 1,
                'out_y': 0,
            }


    def _set_ori_ne(self, prev_pipe) -> None:
        '''L'''
        if prev_pipe.y == self.y:
            if prev_pipe.ori['in_y'] == 1:
                left_under = 'in'
            else:
                left_under = 'out'
        else:
            if prev_pipe.ori['in_x'] == 1:
                left_under = 'out'
            else:
                left_under = 'in'

        if left_under == 'in':
            self.ori = {
                'in_x': -1,
                'in_y': 1,
                'out_x': 1,
                'out_y': -1,
            }
        else:
            self.ori = {
                'in_x': 1,
                'in_y': -1,
                'out_x': -1,
                'out_y': 1,
            }
            


    def _set_ori_nw(self, prev_pipe) -> None:
        '''J'''
        if prev_pipe.y == self.y:
            if prev_pipe.ori['in_y'] == 1:
                right_under = 'in'
            else:
                right_under = 'out'
        else:
            if prev_pipe.ori['in_x'] == 1:
                right_under = 'in'
            else:
                right_under = 'out'

        if right_under == 'in':
            self.ori = {
                'in_x': 1,
                'in_y': -1,
                'out_x': -1,
                'out_y': 1,
            }
        else:
            self.ori = {
                'in_x': -1,
                'in_y': 1,
                'out_x': 1,
                'out_y': -1,
            }


    def _set_ori_sw(self, prev_pipe) -> None:
        '''7'''
        if prev_pipe.y == self.y:
            if prev_pipe.ori['in_y'] == 1:
                right_above = 'out'
            else:
                right_above = 'in'
        else:
            if prev_pipe.ori['in_x'] == 1:
                right_above = 'in'
            else:
                right_above = 'out'

        if right_above == 'in':
            self.ori = {
                'in_x': 1,
                'in_y': -1,
                'out_x': -1,
                'out_y': 1,
            }
        else:
            self.ori = {
                'in_x': -1,
                'in_y': 1,
                'out_x': 1,
                'out_y': -1,
            }


    def _set_ori_se(self, prev_pipe) -> None:
        '''F'''
        if prev_pipe.y == self.y:
            if prev_pipe.ori['in_y'] == 1:
                left_above = 'out'
            else:
                left_above = 'in'
        else:
            if prev_pipe.ori['in_x'] == 1:
                left_above = 'out'
            else:
                left_above = 'in'

        if left_above == 'in':
            self.ori = {
                'in_x': -1,
                'in_y': -1,
                'out_x': 1,
                'out_y': 1,
            }
        else:
            self.ori = {
                'in_x': 1,
                'in_y': 1,
                'out_x': -1,
                'out_y': -1,
            }



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


    def get_max_distance(self, test=False, dir = 2) -> None:
        for i in range(dir):
            self.discover_path(i)


    def discover_path(self, i: int, test=False) -> None:
        steps = 1
        prev_pipe = self.start

        if test:
            prev_pipe.ori = START_ORI_TST
        else:
            prev_pipe.ori = START_ORI

        prev_pipe.set_neighbor_status(self)

        cur_pipe = prev_pipe.neighbors[i]

        cur_pipe.set_ori(prev_pipe)

        while True:
            self.print_map()

            if cur_pipe.distance < 0 or cur_pipe.distance > steps:
                cur_pipe.distance = steps

            cur_pipe.set_neighbor_status(self)
    
            next_pipe = cur_pipe.get_next_pipe(prev_pipe)

            if next_pipe.start or steps > MAX_ROUNDS:
            # if next_pipe.start:
                break

            steps += 1
            prev_pipe = cur_pipe
            cur_pipe = next_pipe
            cur_pipe.set_ori(prev_pipe)


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
                if self.pipes[x,y].start:
                    line += 'S'
                    continue

                distance = self.pipes[x,y].distance
                status = self.pipes[x,y].status
                if status == 'I':
                    line += '*'
                elif status == 'O':
                    line += '+'
                elif status == 'L':
                    line += UUCODE_TABLE[self.pipes[x,y].char]
                else:
                    line += ' '
            print(line)


# Main functions
def get_solution_part1(lines: list[str], test=False) -> int:
    '''Main function'''

    grid = Grid(lines,test=test)
    grid.set_relations()
    grid.get_max_distance(test=test)

    # grid.print_distances()
    grid.print_map()

    return max([p.distance for p in grid.pipes.flat ])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], test=False) -> int:
    '''Main function'''

    grid = Grid(lines,test=test)
    grid.set_relations()
    grid.get_max_distance(test=test, dir=1)

    grid.print_map()

    return [p.status for p in grid.pipes.flat].count('I')

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass