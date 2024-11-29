"""
Year 2018, Day 8

Problem description: See https://adventofcode.com/2018/day/8

The following class is used:
- Node: Represents a node with the following attributes:
    - childs: list of child Node objects
    - parent: Parent Node (None if root Node)
    - metadata: list of metadata entries
    - metadata_sum: Class variable keepint track of the summary

Part 1: I defined the input numbers as a deque. I started with creating a
root Node and processed all input numbers in order:
    - number of childs
    - number of metadata entries
    - Then recursivelt create the new childs from the same input deque
    - finally read the metadata entries (updating the sum)

Part 2: To calculate the node value (for root to start with), a new recursive
function is used (Node.get_value()). It does the following:
- If the value is already known, simply return it.
- If there are no childs, return the sum of all the metadata entries.
- If there are childs, look at the metadata entries and for each one:
    - If it exceeds the number of childs, ignore it.
    - Otherwise (recursively) calculate the node value for that child node.
- In the end, return the total.

"""

# Imports
from __future__ import annotations
from pprint import pprint
from logging import Logger
from collections import deque


# Constants


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

class Node:
    '''A single node with a list of child nodes, a single Parent node
    and a list of metadata entries'''
    
    # Class variable to keep track of the summary of metadata values
    metadata_sum = 0

    def __init__(self, input:deque[int], parent:Node|None=None) -> None:
        self.parent = parent
        self.childs = []
        self.metadata = []

        # Set node value to None, indicating that it hasn't yet been
        # calculated
        self.node_value = None

        # Retrieve nr of childs
        nr_of_childs = input.popleft()

        # Retrieve nr of metadata entries
        nr_of_metadata = input.popleft()

        # Create child nodes
        for i in range(nr_of_childs):
            self.childs.append(Node(input,self))

        # Assign Metadata values
        for i in range(nr_of_metadata):
            metadata_entry = input.popleft()
            Node.metadata_sum += metadata_entry
            self.metadata.append(metadata_entry)
            Gv.log.debug(f'Adding metadata: {metadata_entry}')


    def get_value(self) -> int:
        '''Calculate the Node value'''
        # If the value is already calculated, just return it
        if self.node_value is not None:
            return self.node_value
        
        # If no child nodes, set node value to sum of metadata
        if len(self.childs) == 0:
            self.node_value = sum(self.metadata)
            return self.node_value

        self.node_value = 0

        # Calculate node value for all references child nodes
        for ref in self.metadata:
            # If outside range, ignore:
            if ref > len(self.childs):
                Gv.log.debug(f'Ignoring {ref}')
                continue

            # otherwise add the node value for the child
            Gv.log.debug(f'Adding for child {ref}')
            self.node_value += self.childs[ref-1].get_value()

        return self.node_value


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv(**kwargs)

    input = deque([int(nr) for nr in lines[0].split()])

    root = Node(input)

    return Node.metadata_sum

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv(**kwargs)

    input = deque([int(nr) for nr in lines[0].split()])

    root = Node(input)

    return root.get_value()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
