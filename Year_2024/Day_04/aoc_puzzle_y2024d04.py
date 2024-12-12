"""
Year 2024, Day 4

Problem description: See https://adventofcode.com/2024/day/4

The following class is used:
- WordSearch: Numpy grid class containing the letters.

Part 1: Walk through the grid searching for letter X. When found go in all
directions and see if you can form the word XMAS.

Part 2: Walk through the grid searching for the letter A. When found check
the cross positions, looking for MAS or SAM.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from grid import Grid2D

# Constants

WORD = 'XMAS'
MAS = 'MAS'
SAM = 'SAM'


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

class WordSearch(Grid2D):
    '''Grid2D class containing the letters'''
    def __init__(self, lines:str):
        self.x_size = len(lines[0])
        self.y_size = len(lines)
        super().__init__(sizes=(self.x_size,self.y_size),input_lines=lines)
        self.letters = self.grid
        Gv.log.debug(f'{self.x_size}, {self.y_size}')
        Gv.log.debug(str(self))


    def find_xmas_words(self) -> int:
        '''Find all XMAS words'''
        words = 0

        for y in range(self.y_size):
            for x in range(self.x_size):
                # Skip if not X
                if self.letters[x,y] != WORD[0]:
                    continue

                # Search in all directions
                for dir_y in range(-1,2):
                    for dir_x in range(-1,2):
                        # If both directions are 0, skip
                        if dir_x == 0 and dir_y == 0:
                            pass
                        elif self.is_xmas(x,y,dir_x,dir_y):
                            words += 1

        return words


    def find_x_mas(self) -> int:
        '''Find all cross MAS words'''
        words = 0

        for y in range(self.y_size):
            for x in range(self.x_size):
                # Skip if not A
                if self.letters[x,y] != MAS[1]:
                    continue

                # Check on borders
                if (
                    x == 0 or x == self.x_size-1 or
                    y == 0 or y == self.y_size-1
                ):
                    continue

                # Check cross word
                x_word1 = self.letters[x-1,y-1] + self.letters[x,y]
                x_word1 += self.letters[x+1,y+1]
                x_word2 = self.letters[x-1,y+1] + self.letters[x,y]
                x_word2 += self.letters[x+1,y-1]

                if (
                    (x_word1 == MAS or x_word1 == SAM) and
                    (x_word2 == MAS or x_word2 == SAM)
                ):
                    words += 1

        return words


    def is_xmas(self, x, y, dir_x, dir_y) -> bool:
        '''Return True if you can find XMAS in this direction'''
        # Skip if you go past borders
        if (
            x + (dir_x * len(WORD)) < -1 or
            x + (dir_x * len(WORD)) > self.x_size or
            y + (dir_y * len(WORD)) < -1 or
            y + (dir_y * len(WORD)) > self.y_size
        ):
            Gv.log.debug(f'border found: {x}, {y}, {dir_x}, {dir_y}')
            return False
        
        check_word = WORD[0]

        for i in range(1,len(WORD)):
            check_x = x + i * dir_x
            check_y = y + i * dir_y
            check_word += self.letters[check_x,check_y]

        Gv.log.debug(f'check_word: {check_word} for {x}, {y}, {dir_x}, {dir_y}')

        return check_word == WORD


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    ws = WordSearch(lines)

    return ws.find_xmas_words()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    ws = WordSearch(lines)

    return ws.find_x_mas()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
