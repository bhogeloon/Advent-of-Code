"""
Year 2019, Day 3, Part 2

Problem description: See https://adventofcode.com/2019/day/3

"""

# Imports
from itertools import count
from lib2to3.refactor import MultiprocessRefactoringTool
from pprint import pprint

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Grid(dict):
    def add_point(self, x, y , index):
        if y not in self.keys():
            self[y] = {}

        if x not in self[y].keys():
            self[y][x] = set()

        self[y][x].add(index)


    def get_distance(self, x, y) -> int:
        return abs(x) + abs(y)


    def get_closest_cross(self) -> int:
        min_dist = None

        for y in self.keys():
            for x in self[y].keys():
                if x == 0 and y == 0:
                    continue
                if len(self[y][x]) == 2:
                    this_dist = self.get_distance(x, y)
                    if min_dist == None or min_dist > this_dist:
                        min_dist = this_dist

        return min_dist


    def get_eff_cross(self, wires: list) -> int:
        min_dist = None

        for y in self.keys():
            for x in self[y].keys():
                if x == 0 and y == 0:
                    continue
                if len(self[y][x]) == 2:
                    this_dist = 0
                    for wire in wires:
                        this_dist += wire.get_distance(x, y, self)
                    if min_dist == None or min_dist > this_dist:
                        min_dist = this_dist

        return min_dist



class Instruction():
    def __init__(self, line: str) -> None:
        self.dir = line[0]
        self.amount = int(line[1:])


class Wire():
    def __init__(self, index: int, line: str) -> None:
        self.index = index
        self.instrs = [Instruction(line_part) for line_part in line.split(',')]
        self.ptr_x = 0
        self.ptr_y = 0


    def run_instr(self, instr: Instruction, grid: Grid, x=0, y=0):
        if instr.dir == "U":
            return self.follow_up(instr.amount, grid, x, y)
        elif instr.dir == "D":
            return self.follow_down(instr.amount, grid, x, y)
        elif instr.dir == "R":
            return self.follow_right(instr.amount, grid, x, y)
        elif instr.dir == "L":
            return self.follow_left(instr.amount, grid, x, y)
        else:
            raise RuntimeError("Unkown direction: '{}'.".format(instr.dir))


    def follow_up(self, y_amount: int, grid: Grid, x_lim: int, y_lim: int):
        nr_of_points = y_amount
        end_reached = False
        for y in range(self.ptr_y + 1, self.ptr_y + y_amount + 1):
            grid.add_point(self.ptr_x, y, self.index)
            if x_lim == 0 and y_lim == 0:
                continue
            if x_lim == self.ptr_x and y_lim == y:
                nr_of_points = y - self.ptr_y
                end_reached = True
                break

        self.ptr_y += y_amount
        return nr_of_points, end_reached


    def follow_down(self, y_amount: int, grid: Grid, x_lim: int, y_lim: int):
        nr_of_points = y_amount
        end_reached = False
        for y in range(self.ptr_y - 1, self.ptr_y - y_amount - 1, -1):
            grid.add_point(self.ptr_x, y, self.index)
            if x_lim == 0 and y_lim == 0:
                continue
            if x_lim == self.ptr_x and y_lim == y:
                nr_of_points = self.ptr_y - y
                end_reached = True
                break

        self.ptr_y -= y_amount
        return nr_of_points, end_reached


    def follow_right(self, x_amount: int, grid: Grid, x_lim: int, y_lim: int):
        nr_of_points = x_amount
        end_reached = False
        for x in range(self.ptr_x + 1, self.ptr_x + x_amount + 1):
            grid.add_point(x, self.ptr_y, self.index)
            if x_lim == 0 and y_lim == 0:
                continue
            if x_lim == x and y_lim == self.ptr_y:
                nr_of_points = x - self.ptr_x
                end_reached = True
                break

        self.ptr_x += x_amount
        return nr_of_points, end_reached


    def follow_left(self, x_amount: int, grid: Grid , x_lim: int, y_lim: int):
        nr_of_points = x_amount
        end_reached = False
        for x in range(self.ptr_x - 1, self.ptr_x - x_amount - 1, -1):
            grid.add_point(x, self.ptr_y, self.index)
            if x_lim == 0 and y_lim == 0:
                continue
            if x_lim == x and y_lim == self.ptr_y:
                nr_of_points = self.ptr_x - x
                end_reached = True
                break

        self.ptr_x -= x_amount
        return nr_of_points, end_reached


    def run_instrs(self, grid: Grid):
        for instr in self.instrs:
            self.run_instr(instr, grid)


    def get_distance(self, x: int, y: int, grid: Grid) -> int:
        counter = 0
        self.ptr_x = 0
        self.ptr_y = 0

        for instr in self.instrs:
            progress, end_reached = self.run_instr(instr, grid, x, y)
            counter += progress
            if end_reached:
                break

        return counter


# Functions




# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    grid = Grid()
    wires= []

    for i, line in enumerate(lines):
        wires.append(Wire(i, line))
        wires[i].run_instrs(grid)

    return grid.get_eff_cross(wires)

    return __name__


if __name__ == '__main__':
    pass