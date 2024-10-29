"""
Year 2022, Day 8

Problem description: See https://adventofcode.com/2022/day/8

"""

# Imports
from pprint import pprint
import numpy as np

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

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

        for neighbor_x in range(x):
            if wood.trees[neighbor_x,y].height >= wood.trees[x,y].height:
                visible = False
                break

        if visible:
            wood.trees[x,y].visible = True
            wood.visible_trees += 1
            return
        
        visible = True

        for neighbor_x in range(x+1, wood.x_size):
            if wood.trees[neighbor_x,y].height >= wood.trees[x,y].height:
                visible = False
                break

        if visible:
            wood.trees[x,y].visible = True
            wood.visible_trees += 1
            return

        visible = True

        for neighbor_y in range(y):
            if wood.trees[x,neighbor_y].height >= wood.trees[x,y].height:
                visible = False
                break

        if visible:
            wood.trees[x,y].visible = True
            wood.visible_trees += 1
            return
        
        visible = True

        for neighbor_y in range(y+1, wood.y_size):
            if wood.trees[x,neighbor_y].height >= wood.trees[x,y].height:
                visible = False
                break

        if visible:
            wood.trees[x,y].visible = True
            wood.visible_trees += 1
            return
        
        return
    

    @property
    def scenic_score(self) -> int:
        return self.wood.tree_scenic_scores[self.x, self.y]
    

    @scenic_score.setter
    def scenic_score(self, value: int) -> None:
        self.wood.tree_scenic_scores[self.x, self.y] = value


    def check_scenic_score(self) -> None:
        x = self.x
        y = self.y
        wood = self.wood

        total_score = 1

        this_score = 1

        for x_nb in range(x-1, 0, -1):
            if wood.trees[x_nb,y].height >= wood.trees[x,y].height:
                break

            this_score += 1

        total_score *= this_score

        this_score = 1

        for x_nb in range(x+1, wood.x_size-1):
            if wood.trees[x_nb,y].height >= wood.trees[x,y].height:
                break

            this_score += 1

        total_score *= this_score

        this_score = 1

        for y_nb in range(y-1, 0, -1):
            if wood.trees[x,y_nb].height >= wood.trees[x,y].height:
                break

            this_score += 1

        total_score *= this_score

        this_score = 1

        for y_nb in range(y+1, wood.y_size-1):
            if wood.trees[x,y_nb].height >= wood.trees[x,y].height:
                break

            this_score += 1

        total_score *= this_score

        self.scenic_score = total_score

        if total_score > wood.max_scenic_score:
            wood.max_scenic_score = total_score


class Wood():
    '''Matrix of Trees'''

    def __init__(self, lines: list[str]) -> None:
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        self.trees = np.full((self.x_size, self.y_size), None)
        self.tree_scenic_scores = np.ones_like(self.trees)
        self.set_tree_heigths(lines)


    def print_heigths(self) -> None:
        for y in range(self.y_size):
            line = ''
            for x in range(self.x_size):
                line += str(self.trees[x,y].height)
            print(line)


    def set_tree_heigths(self, lines: list[str]) -> None:
        for x in range(self.x_size):
            for y in range(self.y_size):
                self.trees[x,y] = Tree(lines[y][x], x, y, self)


    def check_visibility(self) -> None:

        self.visible_trees = 0

        for tree in self.trees.flat:
            tree.check_visibility()


    def check_scenic_score(self) -> None:
        self.max_scenic_score = 0

        for tree in self.trees.flat:
            tree.check_scenic_score()

    def get_max_scenic_score(self) -> int:
        return self.tree_scenic_scores.max()


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    wood = Wood(lines)

    # wood.print_heigths()

    wood.check_visibility()

    return wood.visible_trees

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    wood = Wood(lines)
    wood.check_scenic_score()

    print(wood.get_max_scenic_score())

    return wood.max_scenic_score

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
	