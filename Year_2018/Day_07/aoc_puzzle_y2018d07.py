"""
Year 2018, Day 7

Problem description: See https://adventofcode.com/2018/day/7

The following classes are used:
- Step: A step to be performed.
- Sleigh: Dict container class of Step objects.

Part 1: Determine all the Parents and Childs of each step. Then start by
finding all steps that have no parents. They are put in a list of steps
ready to be performed. Then each time select the smallest step_id in the list.
Once a step is performed, check for each child whether it is ready to be
performed (i.e. all parents are done) and if so include that in the list of 
steps ready to be done. Repeat this procedure until the list of steps ready
to be done is empty.
 
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

class Step:
    '''A step to assemble the sleigh. This has an id, a list of parents and a 
    list of childs and a done boolean field'''

    def __init__(self, id: str) -> None:
        self.id = id
        self.parents = []
        self.childs = []
        self.done = False


    def perform(self) -> list:
        '''Perform the step and return a list of child ids which are not yet
        ready'''
        self.done = True
        new_steps_ready = []

        for child in self.childs:
            if not child.done and child.is_ready_tbp():
                new_steps_ready.append(child.id)

        return new_steps_ready
    

    def is_ready_tbp(self) -> bool:
        '''Checks if the step is ready to be performed, i.e. all parents are 
        done'''
        for parent in self.parents:
            if not parent.done:
                return False
            
        return True


class Sleigh(dict[str, Step]):
    '''A dict container class of Step objects with Step id as key. Furthermore
    it contains a list of Step ids ready to be done and a step_order str 
    attribute to keep track of the order of steps'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            pattern = r'Step ([A-Z]) must be finished '
            pattern += r'before step ([A-Z]) can begin\.'
            m = re.fullmatch(pattern, line)
            parent_id = m.group(1)
            child_id = m.group(2)

            # Create objects if they don't yet exists
            for id in [parent_id, child_id]:
                if id not in self.keys():
                    self[id] = Step(id)

            # Set relations
            self[child_id].parents.append(self[parent_id])
            self[parent_id].childs.append(self[child_id])

        # This will contain the order of steps
        self.order = ''
        self.find_starting_steps()


    def find_starting_steps(self) -> None:
        '''Register the steps that have no parents in the ready_tbd list'''
        self.ready_tbd = []

        for step in self.values():
            if len(step.parents) == 0:
                self.ready_tbd.append(step.id)


    def perform_steps(self) -> None:
        '''Perform all steps in the right order'''
        # until there are no more steps to be done
        while len(self.ready_tbd) > 0:
            # Order the ready_tbd list in reverse order
            self.ready_tbd.sort(reverse=True)
            # select next step
            next_step = self[self.ready_tbd.pop()]
            # perform the step and put the childs in ready_tbd
            self.ready_tbd.extend(next_step.perform())
            # Register the step that has been done
            self.order += next_step.id


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    sleigh = Sleigh(lines)
    sleigh.perform_steps()

    return sleigh.order

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
