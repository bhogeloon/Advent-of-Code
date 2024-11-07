"""
Year 2022, Day 9

Problem description: See https://adventofcode.com/20xx/day/xx

The following classes are used:
- Knot: represents a knot (head or tail or - in part 2 - an in between tail)
- RopeGrid: A Grid2D class, containing boolean values. If the tail has passed
    a point in the grid, the value will become True

Part 1: Update the head Knot according to the input and then follow the
specified rules for the tail Knot. Afterwards mark the tail spot.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from grid import Grid2D


# Constants

GRID_SIZE = 10000
S_X = GRID_SIZE//2
S_Y = S_X


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Knot():
    '''A Knot (head, tail or something in between)'''

    def __init__(self, x = S_X, y = S_Y) -> None:
        self.x = x
        self.y = y


class RopeGrid(Grid2D):
    '''Grid of ropes with a head and tail'''

    def __init__(self, nr_of_knots: int) -> None:
        self.head_x = S_X
        self.head_y = S_Y
        self.tail_x = S_X
        self.tail_y = S_Y

        super().__init__(sizes=(GRID_SIZE,GRID_SIZE), default_value=False)

        self.grid_array = self.grid
        # Mark starting points
        self.grid_array[S_X,S_Y] = True
        self.knots = [ Knot() for var in range(nr_of_knots) ]


    def count_visited(self) -> int:
        '''Return the number of grid values True'''
        return self.grid_array.sum()


    def move_tails(self) -> None:
        '''Move all the tails after the head'''
        for i in range(1, len(self.knots)):
            self.move_tail(i)
        
        self.update_tail_pos()


    def move_up(self, n: int) -> None:
        '''Move the knots when the head is going up'''
        for i in range(n):
            # Move head
            self.knots[0].y += 1
            self.move_tails()


    def move_down(self, n: int) -> None:
        '''Move the knots when the head is going down'''
        for i in range(n):
            # Move head
            self.knots[0].y -= 1
            self.move_tails()


    def move_right(self, n: int) -> None:
        '''Move the knots when the head is going right'''
        for i in range(n):
            # Move head
            self.knots[0].x += 1
            self.move_tails()


    def move_left(self, n: int) -> None:
        '''Move the knots when the head is going left'''
        for i in range(n):
            # Move head
            self.knots[0].x -= 1
            self.move_tails()


    def move(self, line: str) -> None:
        '''Move the knots according to the input line'''
        # print('moving: {}'.format(line))
        (dir, n_str) = line.split()
        n = int(n_str)

        if dir == 'U':
            self.move_up(n)
        elif dir == 'D':
            self.move_down(n)
        elif dir == 'R':
            self.move_right(n)
        elif dir == 'L':
            self.move_left(n)
        else:
            raise RuntimeError('Unknown dir: {}'.format(dir))


    def move_tail(self, knot_nr: int) -> None:
        '''Move this tail following its head'''
        head = self.knots[knot_nr-1]
        tail = self.knots[knot_nr]

        # Calculate the difference in position
        diff_x = head.x - tail.x
        diff_y = head.y - tail.y

        # We move each head one step at the time, so the difference can never
        # be more than 2
        if abs(diff_x) > 2 or abs(diff_y) > 2:
            raise RuntimeError('Head too far ahead')
        elif abs(diff_x) <=1 and abs(diff_y) <= 1:
            # No need to move tail as it is in sight
            return
        # If more than 1 behind on x, follow head on x
        elif abs(diff_x) > 1:
            tail.x += diff_x - (diff_x//abs(diff_x))
            # Follow also on y or step on same level
            if abs(diff_y) > 1:
                tail.y += diff_y - (diff_y//abs(diff_y))
            else:
                tail.y = head.y
        # Otherwise follow on y
        elif abs(diff_y) > 1:
            tail.y += diff_y - (diff_y//abs(diff_y))
            # Step on same x level
            tail.x = head.x
        else:
            raise RuntimeError('Something very weird just happened')


    def update_tail_pos(self) -> None:
        '''Mark the tail position to be True'''
        # print('Updating ({}, {})'.format(self.tail_x, self.tail_y))
        tail = self.knots[len(self.knots)-1]
        self.grid_array[tail.x, tail.y] = True


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    rope_grid = RopeGrid(2)

    for line in lines:
        rope_grid.move(line)

    return rope_grid.count_visited()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    rope_grid = RopeGrid(10)

    for line in lines:
        rope_grid.move(line)

    return rope_grid.count_visited()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
