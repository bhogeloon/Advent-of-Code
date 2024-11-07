"""
Year 2017, Day 7

Problem description: See https://adventofcode.com/2017/day/7

The following classes are used:
- Program: A program with a name, weight, a parent and a list of childs
- Tower: Dict container class of Program objects with the Program name as key.

Part 1: Register all Programs with the child names. Then set all the parent-
child relations and finally find the program with no parent.
"""

# Imports
from __future__ import annotations
from pprint import pprint
import re


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Program:
    '''A program has a name, a parent Program and a list of child Programs'''

    def __init__(self, line: str) -> None:
        pattern = r'(\w+)\s+\((\d+)\)(.*)'
        m = re.fullmatch(pattern, line)

        self.name = m.group(1)
        self.weight = int(m.group(2))

        remainder = m.group(3)

        # Register child names if any
        if remainder == '':
            self.child_names = []
        else:
            remainder = remainder.removeprefix(' -> ')
            self.child_names = remainder.split(', ')

        # Will be used for relations
        self.parent = None
        self.childs = []


    def set_relations(self, tower: Tower) -> None:
        '''Set the Parent and Child relations for this Program'''
        for child_name in self.child_names:
            child_program = tower[child_name]
            self.childs.append(child_program)

            # Cause an error if more than one parent
            if child_program.parent != None:
                raise RuntimeError(f'More than one parent for {child_name}')

            # Set yourself as parent of the child            
            child_program.parent = self


class Tower(dict[str, Program]):
    '''A Dict container class of Program objects. The key is the name of the
    Program'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            program = Program(line)
            self[program.name] = program


    def set_relations(self) -> None:
        '''Set parent and child relations for each Program'''
        for program in self.values():
            program.set_relations(self)


    def get_bottom_program(self) -> Program:
        '''Return the program with no parent'''
        for program in self.values():
            if program.parent == None:
                return program
            
        # If none found
        raise RuntimeError('No bottom program found')


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    tower = Tower(lines)
    tower.set_relations()

    return tower.get_bottom_program().name

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
