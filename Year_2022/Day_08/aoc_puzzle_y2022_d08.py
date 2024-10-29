"""
Year 2022, Day 8

Problem description: See https://adventofcode.com/2022/day/8

The following classes are used:
- Tree: A tree with a certain height
- Wood: A 2DGrid collection of Tree objects

Part 1: For each Tree, check the neighbors until the grid border in each
direction. If a Tree is visible in one direction, then it is visible.

Part 2: For each Tree, look in each direction for a 'blocking' Tree, i.e.
same size or bigger. Count the number of trees visible in each direction and
multiply them.
"""

# Imports
from pprint import pprint
from grid import Grid2D


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Tree():
    '''Tree with a certain height and visible (True or False)'''

    def __init__(self, char, x, y, wood) -> None:
        self.height = int(char)
        self.x = x
        self.y = y
        self.wood = wood
        self.visible = False
        self.scenic_score = 0


    def check_visibility(self) -> None:
        '''Check visibility of tree'''
        x = self.x
        y = self.y
        wood = self.wood

        visible = True

        # Check for each left neighbor if it is smaller
        for neighbor_x in range(x):
            if wood.trees[neighbor_x,y].height >= wood.trees[x,y].height:
                visible = False
                break

        # If visible then increase wood counter and exit
        if visible:
            wood.trees[x,y].visible = True
            wood.visible_trees += 1
            return
        
        visible = True

        # Do the check for all right neighbors
        for neighbor_x in range(x+1, wood.x_size):
            if wood.trees[neighbor_x,y].height >= wood.trees[x,y].height:
                visible = False
                break

        if visible:
            wood.trees[x,y].visible = True
            wood.visible_trees += 1
            return

        visible = True

        # Check all upper neighbors
        for neighbor_y in range(y):
            if wood.trees[x,neighbor_y].height >= wood.trees[x,y].height:
                visible = False
                break

        if visible:
            wood.trees[x,y].visible = True
            wood.visible_trees += 1
            return
        
        visible = True

        # Check all lower neighbors
        for neighbor_y in range(y+1, wood.y_size):
            if wood.trees[x,neighbor_y].height >= wood.trees[x,y].height:
                visible = False
                break

        if visible:
            wood.trees[x,y].visible = True
            wood.visible_trees += 1
            return
        
        return


    def check_scenic_score(self) -> None:
        '''Check the scenic score for this tree'''
        x = self.x
        y = self.y
        wood = self.wood

        # If on border, score = 0
        if (
            x == 0 or
            y == 0 or
            x == self.wood.x_size-1 or
            y == self.wood.y_size-1
        ):
            self.scenic_score = 0
            return

        # Total score of all directions multiplied
        total_score = 1

        # Score for current direction
        this_score = 1

        # Check left side
        for x_nb in range(x-1, 0, -1):
            # If a blocking tree is found exit
            if wood.trees[x_nb,y].height >= wood.trees[x,y].height:
                break

            this_score += 1

        # Update total score
        total_score *= this_score

        # Repeat for right side
        this_score = 1

        for x_nb in range(x+1, wood.x_size-1):
            if wood.trees[x_nb,y].height >= wood.trees[x,y].height:
                break

            this_score += 1

        total_score *= this_score

        # Repeat for upper side
        this_score = 1

        for y_nb in range(y-1, 0, -1):
            if wood.trees[x,y_nb].height >= wood.trees[x,y].height:
                break

            this_score += 1

        total_score *= this_score

        # Repeat for down side
        this_score = 1

        for y_nb in range(y+1, wood.y_size-1):
            if wood.trees[x,y_nb].height >= wood.trees[x,y].height:
                break

            this_score += 1

        total_score *= this_score

        self.scenic_score = total_score

        if total_score > wood.max_scenic_score:
            wood.max_scenic_score = total_score
            wood.max_scenic_coord = (x,y)


class Wood(Grid2D):
    '''Matrix of Trees'''

    def __init__(self, lines: list[str]) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)

        def set_tree_heigth( 
            lines=lines,
            x= None,
            y=None,
            wood=self
        ) -> None:
            '''Function to Initialise Tree objects'''
            return Tree(lines[y][x], x, y, wood)

        super().__init__(
            sizes=(self.x_size,self.y_size),
             func=set_tree_heigth,
        )

        self.trees = self.grid


    def print_heigths(self) -> None:
        '''Function to check if the input was read successfully'''
        for y in range(self.y_size):
            line = ''
            for x in range(self.x_size):
                line += str(self.trees[x,y].height)
            print(line)


    def check_visibility(self) -> None:
        '''Check the visibility of each Tree'''
        self.visible_trees = 0

        for tree in self.trees.flat:
            tree.check_visibility()


    def check_scenic_score(self) -> None:
        '''Determine scenic score for each tree'''
        self.max_scenic_score = 0

        for tree in self.trees.flat:
            tree.check_scenic_score()


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    wood = Wood(lines)

    if Gv.test:
        wood.print_heigths()

    wood.check_visibility()

    return wood.visible_trees

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    wood = Wood(lines)
    wood.check_scenic_score()

    if Gv.test:
        print(wood.max_scenic_coord)

    return wood.max_scenic_score

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
