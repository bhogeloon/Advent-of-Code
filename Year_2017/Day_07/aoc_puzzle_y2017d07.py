"""
Year 2017, Day 7

Problem description: See https://adventofcode.com/2017/day/7

The following classes are used:
- Program: A program with a name, weight, a parent and a list of childs
- Tower: Dict container class of Program objects with the Program name as key.

Part 1: Register all Programs with the child names. Then set all the parent-
child relations and finally find the program with no parent.

Part 2: The way to check if a tower is balanced or not is to calculate the
total weight for each child, and then see if there is exactly one different
value.
However, to get the weight that needs to be corrected, you need to discover
the 'unbalancement' on the deepest level in the tree. So we use a recursive
function that first checks if the unbalancement is somewhere deeper and if not
tries to find the unbalacement of its own object.
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


    def get_tot_weight(self) -> int:
        '''Return the total weight of the program tower'''
        tot_weight = self.weight

        for child in self.childs:
            tot_weight += child.get_tot_weight()

        return tot_weight
    

    def check_balance(self) -> int:
        '''Return the proper weight of the child that needs to be fixed.
        If the program tower is balanced, then return -1'''
        # If the program has 0 or 1 child, it is always balanced, so we don't
        # have to bother
        if len(self.childs) < 2:
            return -1

        # record all child tower weights and the childs they are reported on
        child_weights = {}

        for child in self.childs:
            child_weight = child.get_tot_weight()

            if child_weight in child_weights.keys():
                child_weights[child_weight].append(child)
            else:
                child_weights[child_weight] = [child]

        # If only one weight has been found, the program tower is balanced.
        if len(child_weights.keys()) == 1:
            return -1
        
        # Otherwise, if we have only two childs, we cannot determine the
        # wrong one.
        if len(self.childs) == 2:
            raise RuntimeError(
                f'Unbalanced program tower with only 2 childs: {self.name}:'
                f'{self.child_names}'
            )

        # If number of weights reported is larger than 2, something is wrong
        if len(child_weights.keys()) > 2:
            raise RuntimeError(
                f'More than 2 different weight values for {self.name}'
            )
        
        print(f'Found unbalanced tower for {self.name}')

        for child in self.childs:
            print(
                f'Weight for child {child.name}: {child.weight}, '
                f'total weight: {child.get_tot_weight()}'
            )

        # Record difference between weights
        weight_list = list(child_weights.keys())
        weight_diff = weight_list[0] - weight_list[1]

        # Then find the weight which has only one child
        for child_weight, childs in child_weights.items():
            if len(childs) == 1:
                # Repair the childs weight
                if child_weight == min(weight_list):
                    return childs[0].weight + abs(weight_diff)
                else:
                    return childs[0].weight - abs(weight_diff)

        raise RuntimeError(f'Something went wrong for {self.name}')
    

    def find_unbalanced_program(self) -> int:
        '''Return the proper weight of the unbalanced program. This is achieved
        by looking at the bottom program and then following all the branches.
        The deepest unbalanced program is the one to fix'''
        # First check if one of your children is unbalanced and if so, return
        # that value
        for child in self.childs:
            balance = child.find_unbalanced_program()

            # If not balanced:
            if balance >= 0:
                return balance
            
        # If all children are balanced, do the check on yourself
        return self.check_balance()


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
                self.bottom_program = program
                return program
            
        # If none found
        raise RuntimeError('No bottom program found')
    

    def print_tot_weights(self) -> None:
        '''Prints all total tower weights of each program. For debugging.'''
        for program in self.values():
            print(
                f'Total weight for {program.name}: {program.get_tot_weight()}'
            )


    def get_unbalanced_program(self) -> int:
        '''Return the proper weight of the unbalanced program. This is achieved
        by looking at the bottom program and then following all the branches.
        The deepest unbalanced program is the one to fix'''
        return self.bottom_program.find_unbalanced_program()


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

    tower = Tower(lines)
    tower.set_relations()
    tower.get_bottom_program()

    if Gv.test:
        tower.print_tot_weights()

    return tower.get_unbalanced_program()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
