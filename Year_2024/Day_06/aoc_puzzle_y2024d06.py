"""
Year 2024, Day 6

Problem description: See https://adventofcode.com/2024/day/6

The following classes are used:
- Position: A single position on the map
- Map: A grid class of Position objects
- Guard: Represents the guard with a position on the map

Part 1: Keep track of the visited positions. Keep trying to move the guard:
- If it walks off the map, end process
- If it runs into an obstruction, change the direction instead of the position
- Otherwise, mark the new position as visited and change it to the current
    position.

Part 2: For this puzzle, I needed to place an additional obstruction each time
and then do the calculation for that. If a loop is detected, increase the 
counter. It is only required to do that on the positions on the original path.
The way a loop is detected is to check whether the position has been visited
already, but also using the same direction. So I needed to record the
direction for each position as well.
Instead of using a variable for each Position to record whether it has been
visited, I used class variables to record the Positions visited and in which
direction. The reason for this is that they can be resetted easier after each
run. Otherwise I would need to copy the complete grid before each run to
preserve the states. I still use a 'visited' flag, but that is to record the
original path, so I can determine whether to place an extra obstruction there.
Still, it takes a bit more than a minute to get the solution. I see some room
for improvement. I am now calculating the whole path each time, while the 
path up to the extra obstruction is already known. But for now, I leave it like
this. 
"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from grid import Grid2D
from copy import deepcopy

# Constants

# starting direction
STARTDIR = (0,-1)

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False

    # Variable that will be used for holding the logger object
    log = None

    def __init__(self, test: bool, logger: Logger, **kwargs) -> None:
        '''Initialize the global variables'''
        Gv.test = test
        Gv.log = logger


# Classes

class Position:
    '''Position on the map'''

    # Class variables

    # Tracks all visited positions
    vis_pos = set()
    # Tracks all visited positions with the direction added
    vis_posdir = set()

    def __init__(self, char: str):
        # If this is the guard
        if char == '^':
            self.obstr = False
            self.start = True
            # This attribute is used for the first run in part 2 without extra 
            # obstruction to record which fields are visited
            self.visited = True
        elif char == '#':
            self.obstr= True
            self.start = False
            self.visited = False
        else:
            self.obstr = False
            self.start = False
            self.visited = False


class Map(Grid2D):
    '''Grid class of Position objects'''
    def __init__(self, lines: list[str]):
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        super().__init__(
            sizes=(self.x_size,self.y_size),
            cell_class=Position,
            input_lines=lines,
        )


    def get_visited_pos(self) -> int:
        '''Return the positions visited by the guard'''
        result = 0

        for pos in self.grid.flat:
            if (pos.x, pos.y) in Position.vis_pos:
                result += 1

        return result


class Guard:
    '''Represents the guard'''
    def __init__(self, lines: list[str]):
        self.map = Map(lines)
        self.dir_x = STARTDIR[0]
        self.dir_y = STARTDIR[1]
        self.off_map = False

        # Find guard position
        for y in range(self.map.y_size):
            for x in range(self.map.x_size):
                if self.map.grid[x,y].start:
                    Position.vis_pos.add((x, y))
                    Position.vis_posdir.add((x, y)+STARTDIR)
                    self.pos_x = x
                    self.pos_y = y
                    self.orig_start_pos = (x,y)


    def get_visited_pos(self) -> int:
        '''Return the number of visited positions'''
        return self.map.get_visited_pos()
    

    def follow(self) -> bool:
        '''Follow the Guard movements until it drops out of the map. Return
        True if a loop was detected'''
        loop = False

        while (not self.off_map) and (not loop):
            loop = self.move()
            # Gv.log.debug(loop)

        return loop


    def move(self) -> bool:
        '''Move the guard one position further. Returns True if a loop
        is detected'''
        # Calculate candidate for new position
        new_pos_x = self.pos_x + self.dir_x
        new_pos_y = self.pos_y + self.dir_y

        # See if guard drops off map
        if (
            new_pos_x < 0 or new_pos_x == self.map.x_size or
            new_pos_y < 0 or new_pos_y == self.map.y_size 
        ):
            self.off_map = True
            return False
        
        new_pos = self.map.grid[new_pos_x,new_pos_y]

        # Check if new position is an obstruction
        if new_pos.obstr:
            new_coord = (-self.dir_y,self.dir_x)
            self.dir_x = new_coord[0]
            self.dir_y = new_coord[1]
            return False
        
        # Detect a loop
        if (
            (new_pos_x,new_pos_y, self.dir_x,self.dir_y) in Position.vis_posdir
        ):
            return True
        
        # Otherwise set new position
        Position.vis_pos.add((new_pos_x,new_pos_y))
        Position.vis_posdir.add((new_pos_x,new_pos_y, self.dir_x,self.dir_y))
        self.map.grid[new_pos_x,new_pos_y].visited = True
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y

        return False
    

    def get_loops(self) -> int:
        '''Return the amount of instances where we can create a loop'''
        result = 0

        # First create a copy of the map and run the standard procedure on it
        copy_map = deepcopy(self.map)
        self.follow()
        orig_map = self.map
        self.map = copy_map

        # try_count = 0

        # Loop through all postitions
        for y in range(self.map.y_size):
            for x in range(self.map.x_size):
                # reset start pos
                (self.pos_x,self.pos_y) = self.orig_start_pos
                # reset off_map
                self.off_map = False
                # Reset dir
                self.dir_x = STARTDIR[0]
                self.dir_y = STARTDIR[1]
                # Reset class variables
                Position.vis_pos = set()
                Position.vis_posdir = set()

                Gv.log.debug(self.get_visited_pos())
                # Skip if pos is obstruction or start
                if self.map.grid[x,y].obstr or self.map.grid[x,y].start:
                    Gv.log.debug(
                        f'skipping {x}, {y}: {self.map.grid[x,y].obstr}, '
                        f'{self.map.grid[x,y].start}'
                    )
                    continue

                # Also skip if this position is not visited in the original
                # procedure
                if not orig_map.grid[x,y].visited:
                    continue

                # try_count += 1
                # Gv.log.info(f'{try_count}: Trying to find loop for {x}, {y}')

                # Set this position as obstr
                self.map.grid[x,y].obstr = True

                # Run the guard
                if self.follow():
                    result += 1
                    Gv.log.debug(f'Loop: {x}, {y}')

                # Restore obstruction
                self.map.grid[x,y].obstr = False

        return result


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    guard = Guard(lines)
    guard.follow()

    return guard.get_visited_pos()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    guard = Guard(lines)

    return guard.get_loops()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
