"""
Year 2023, Day 10

Problem description: See https://adventofcode.com/2023/day/10

For this puzzle I created a Grid class, which is a matrix containing Pipe objects.
The Pipe object can have two connecting neighbors, depending on the shape.
The idea of part 1 is to go to each connecting neighbor until you find the start
again. To calculate the farthest point, you go back the same way to reset the
distance to the starting point if necessarry.

For part 2, we have to define the inside of the loop and the outside. For this,
I added a orientation field describing which x and which y direction the inside
and outside is. We then go through the loop as in part 1, keeping track of the orientation
and setting the status of the inside and outside.
At the end, I fill the inside pipes which are not directly connected to the loop.

"""

# Imports
from pprint import pprint
import numpy as np
import sys

# Raise recurion limit for the flood function
sys.setrecursionlimit(3000)

# Constants

# Use for debugging
MAX_ROUNDS = 13

# Used to visiolise the pipe, which helps with trouble shooting
UUCODE_TABLE = {
    '|': '\u2502',
    '-': '\u2501',
    'L': '\u2515',
    'J': '\u2519',
    '7': '\u2511',
    'F': '\u250d',
}

# Character of the start position, whixh is different on the test input
START_CHAR = '|'
START_CHAR_TST = '7'

# The orientation of the start position
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
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes
class Pipe():
    '''A Pipe object is an element in the grid connecting to two directions
    (or empty list, in case of .)'''

    def __init__(self, char: str, x: int, y: int) -> None:
        # Grid position
        self.x = x
        self.y = y

        if char == 'S':
            if Gv.test:
                self.char = START_CHAR_TST
            else:
                self.char = START_CHAR
            self.start = True
            self.distance = 0
            self.status = 'L'
        else:
            # The actual character read, wich indicates the shape
            self.char = char
            # Indicates starting position
            self.start = False
            # Will be filled with the distance. -1 means not set yet
            self.distance = -1
            # The status indicats whether it is part of the loop ('L'), Inside ('I') or outside ('O')
            # 'U' means unknown
            self.status = 'U'


    def set_relations(self, grid) -> None:
        '''This function is to discover for each point which connecting neighbors it has'''
        self.neighbors = []

        # Create tuples of coordinates
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
        
        # Fill the actual neighbor relationship
        for i in range(2):
            if nb_x[i] < 0 or nb_x[i] >= grid.x_size or \
                nb_y[i] < 0 or nb_y[i] >= grid.y_size:
                self.neighbors.append(None)
            else:
                self.neighbors.append(grid.pipes[nb_x[i],nb_y[i]])


    def get_next_pipe(self, prev_pipe):
        '''Returns the next pipe in line'''
        for nb in self.neighbors:
            # This prevents going back in the direction we came
            if nb != prev_pipe:
                return nb


    def set_neighbor_status(self, grid) -> None:
        '''Set neighbors status as either Inside or Outside
        This is dependant on the shape of pipe, so special private functions are
        created for each shape'''
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


    def _set_nb_io(self, nb_x, nb_y, io, grid, flood=False) -> None:
        '''Private function to set the status of a neighbor'''
        
        # Check if it exists at all
        if nb_x >= 0 and nb_x < grid.x_size and \
            nb_y >= 0 and nb_y < grid.y_size:

            # Only change if status is unknown
            if grid.pipes[nb_x,nb_y].status == 'U':
                grid.pipes[nb_x,nb_y].status = io
                # print("setting status to {} for {},{}".format(io, nb_x, nb_y))

                # If called from the flood function
                if flood:
                    grid.pipes[nb_x,nb_y].flood(grid)


    def set_ori(self, prev_pipe) -> None:
        '''Set the orientation of the pipe, depending on the previous pipe.
        Also here, there is a private function for each shape'''

        # Set the status of the pipe as part of the loop
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
            self._set_ori_se(prev_pipe)


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
                'in_y': 1,
                'out_x': -1,
                'out_y': -1,
            }
        else:
            self.ori = {
                'in_x': -1,
                'in_y': -1,
                'out_x': 1,
                'out_y': 1,
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

    def flood(self, grid) -> None:
        '''Set all unknown neighbors to the same state and if you do, also start
        the flood process on that neighbor'''
        for y in range(self.y-1,self.y+2):
            for x in range(self.x-1,self.x+2):
                self._set_nb_io(x,y,self.status,grid,flood=True)


class Grid():
    '''The grid containing all the pipes'''

    def __init__(self, lines: list[str]) -> None:
        # The size of the matrix
        self.x_size = len(lines[0])
        self.y_size = len(lines)

        # The Pipe objects
        self.pipes = np.full((self.x_size, self.y_size), None)

        # Fill the Pipe objects
        for y in range(self.y_size):
            for x in range(self.x_size):
                self.pipes[x,y] = Pipe(lines[y][x],x,y)

                # If this is the start pipe
                if self.pipes[x,y].start:
                    # Create an attribute pointing to the start pipe
                    self.start = self.pipes[x,y]


    def set_relations(self) -> None:
        '''Walk through the matrix and set the connecting neighbors for each Pipe'''
        for y in range(self.y_size):
            for x in range(self.x_size):
                self.pipes[x,y].set_relations(self)


    def get_max_distance(self, dir = 2) -> None:
        '''Start retrieving the max distance by following the pipe
        In part 1, this needs to be done in both directions (dir=2), but for part 2,
        this is not required as the actual distance is not important there'''

        for i in range(dir):
            self.discover_path(i)


    def discover_path(self, i: int) -> None:
        '''Discover the path of the loop through the grid'''

        # Keep track of the distance
        steps = 1

        # We begin by setting the previous pipe for the firs step as the start pipe
        prev_pipe = self.start

        # Set the start orientation
        if Gv.test:
            prev_pipe.ori = START_ORI_TST
        else:
            prev_pipe.ori = START_ORI

        # Set the neighbors to I or O depending on the orientation
        prev_pipe.set_neighbor_status(self)

        # Set the current pipe as the next pipe from the start pipe
        cur_pipe = prev_pipe.neighbors[i]

        # Set the orientation of the current pipe, looking at the start pipe
        cur_pipe.set_ori(prev_pipe)
        # print('char:', prev_pipe.char)
        # pprint(prev_pipe.ori)
        # print()

        while True:
            # print('step', steps)
            # print('char:', cur_pipe.char)
            # pprint(cur_pipe.ori)
            # self.print_map()

            # If the distance has not been set yet, or the distance is bigger than steps, set
            # the distance to steps
            # The latter is to get the farthest distance from both ways (part 1)
            if cur_pipe.distance < 0 or cur_pipe.distance > steps:
                cur_pipe.distance = steps

            # Set the neighbors to I or O depending on the orientation
            cur_pipe.set_neighbor_status(self)
    
            # Retrieve the next pipe
            next_pipe = cur_pipe.get_next_pipe(prev_pipe)

            # When the loop is closed, abort the process
            # if next_pipe.start or steps > MAX_ROUNDS:
            if next_pipe.start:
                break

            # Increase steos
            steps += 1

            # Circulate the pipes
            prev_pipe = cur_pipe
            cur_pipe = next_pipe

            # Set the orientation of the current (new) pipe, looking at the previous pipe
            cur_pipe.set_ori(prev_pipe)


    def print_distances(self) -> None:
        '''Print a map showing all the distances of the loop.
        Note that this only works very well using the test input as with the normal input you
        will get double figures'''

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
        '''Print a map of the loop, showing also inside and outside.
        It uses uucode symbols rather than character to visualise the loop.
        Really useful for debugging as you can also use this step by step'''

        for y in range(self.y_size):
            # Start a new line
            line = ''

            for x in range(self.x_size):

                # Print S for startpoint
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


    def flood(self) -> None:
        '''Fill all the inside fields which are not marked yet'''
        for pipe in self.pipes.flat:
            # We're not really interested in the outside field and this caused
            # problems with recursion limits. Probably better to just itterate 
            # over the matrix until all unkown fields are gone.
            # if pipe.status == 'I' or pipe.status == 'O':
            if pipe.status == 'I':
                pipe.flood(self)


# Main functions
def get_solution_part1(lines: list[str], test=False) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = test
    grid = Grid(lines)
    grid.set_relations()
    grid.get_max_distance()

    # grid.print_distances()
    grid.print_map()

    # The result is the maximum distance
    return max([p.distance for p in grid.pipes.flat ])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], test=False) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = test
    grid = Grid(lines)
    grid.set_relations()
    grid.get_max_distance(dir=1)
    grid.flood()

    grid.print_map()

    # Count all fields with status I
    return [p.status for p in grid.pipes.flat].count('I')

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass