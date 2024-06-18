"""
Year 2015, Day 3

Problem description: See https://adventofcode.com/2015/day/3

We use the following Classes:
- Dir: Represents a direction
- Dirs: Container class for Dir object
- House: Represents a house and keeps track if it has been visited or not
- Houses: Grid containing House objects.

For part 1: Go through all the Dirs and move Santa in the right direction. Check
if the house has been visited and if not, increase the counter.

For part 2: Keep different coordinates for Santa and Robo and then move them one by
one.
"""

# Imports
from pprint import pprint
from grid import Grid2D


# Constants

GRID_SIZE = 1000
GRID_START = 1000//2

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Dir():
    '''Direction'''

    def __init__(self, char: str) -> None:
        self.dir_char = char


class Dirs(list[Dir]):
    '''List container class of Dir objects'''

    def __init__(self, line: str) -> None:
        for char in line:
            self.append(Dir(char))


class House():
    '''House to visit. Contains an indication if a present has been reveived'''

    def __init__(self) -> None:
        self.present_rcvd = False


    def give_present(self) -> None:
        '''Give this house a present'''
        self.present_rcvd = True


class Houses(Grid2D):
    '''Class containing a grid (numpy) of House objects'''

    def __init__(self, line: str) -> None:
        super().__init__(
            sizes=(GRID_SIZE,GRID_SIZE),
            cell_class=House
        )
        self.houses = self.grid

        self.santa_x = GRID_START
        self.santa_y = GRID_START
        self.robo_x = GRID_START
        self.robo_y = GRID_START
        self.houses[self.santa_x, self.santa_y].give_present()
        self.houses_visited = 1
        self.dirs = Dirs(line)


    def go_santa(self) -> None:
        '''Let Santa follow the directions'''
        for dir in self.dirs:
            self.santa_x,self.santa_y = self.change_dir(
                self.santa_x,
                self.santa_y,
                dir,
            )


    def go_robo_santa(self) -> None:
        '''Let Santa and RoboSanta follow directions'''
        robo_turn = False

        for dir in self.dirs:
            # If it is Robo's turn, cange_dir with Robo's coordinates
            if robo_turn:
                self.robo_x,self.robo_y = self.change_dir(
                    self.robo_x,
                    self.robo_y,
                    dir,
                )
                robo_turn = False
            # And otherwise use Santa's coordinates
            else:
                self.santa_x,self.santa_y = self.change_dir(
                    self.santa_x,
                    self.santa_y,
                    dir,
                )
                robo_turn = True


    def change_dir(self, x: int, y:int, dir: Dir) -> tuple:
        '''Function that moves either Santa or RoboSanta'''

        if dir.dir_char == '>':
            x += 1
        elif dir.dir_char == '<':
            x -= 1
        elif dir.dir_char == '^':
            y += 1
        elif dir.dir_char == 'v':
            y -= 1
        else:
            raise RuntimeError("Unknown dir: {}".format(dir))
        
        cur_house = self.houses[x, y]

        if not cur_house.present_rcvd:
            cur_house.give_present()
            self.houses_visited += 1

        return (x,y)
            

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    houses = Houses(lines[0])
    houses.go_santa()

    return houses.houses_visited

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    houses = Houses(lines[0])
    houses.go_robo_santa()

    return houses.houses_visited

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
