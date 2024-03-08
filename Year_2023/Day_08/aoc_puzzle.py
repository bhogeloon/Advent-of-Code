"""
Year 2023, Day 8

Problem description: See https://adventofcode.com/2023/day/8

I created the following classes:
- Instruction: An instruction to go left ('L') or right ('R').
- Instructions: A circular list of Instruction objects
- Node: A node with a 3 letter name containing left and right
neighbor nodes
- Nodes: Dict of nodes (with name as key)

Part 1 is reasonbly straigt forward: Start at the beginning
following the nodes based on the instruction list keeping track
of the number of steps until the end is reached.

Part 2 is trickier. At first, I simply did the same as in part 1,
but then for a whole list of starting point at the same time.
It stops when all instances in the list have reached a end point
at the same time. However, this will take forever.
So instead I calculated the amount of steps required one by one
and then try to find the common multiplier of those amounts.
This got me the answer (although it still takes almost 2 minutes to compute
the common factor), but I must
remark that this is only because the puzzle input behaves nicely. I can think
of all kinds of scenarios which could complicate things, like when one
cycle suddenly ends up with another.

"""

# Imports
from pprint import pprint
from collections import deque

# Constants
# Begin and end string
BEGIN = 'AAA'
END = 'ZZZ'


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''



# Classes
class Instruction():
    '''An instruction has a direction (dir), which is either 'L' or 'R'
    '''

    def __init__(self, char: str) -> None:
        self.dir = char


class Instructions(list):
    '''Container class (list) of Instruction objects'''

    def __init__(self, line: str) -> None:
        for char in line:
            self.append(Instruction(char))

        # Set the circular relationships
        for i in range(len(self)):
            if i == len(self) - 1:
                self[i].next_instr = self[0]
            else:
                self[i].next_instr = self[i+1]


class Node():
    '''A Node object has the following attributes:
        - name
        - str_dirs: dict with names of left and right nodes
        - ptr_dirs: dict with values that point directly to the next
            left and right nodes
    '''

    def __init__(self, line: str) -> None:
        # Define name
        self.name = line[0:3]
        # Define left and right neighbor names
        # Direct pointers will be set later
        self.str_dirs = {
            'L': line[7:10],
            'R': line[12:15],
        }
        
        # Create an empty dicts where later the pointers will be put
        self.ptr_dirs = {}

        # If the name ends with an A, it is a starting point
        if self.name[2] == 'A':
            self.start_node = True
        else:
            self.start_node = False

        # If the name ends with a Z, it is an ending point
        if self.name[2] == 'Z':
            self.end_node = True
        else:
            self.end_node = False


class Nodes(dict):
    '''Container class of all nodes. This is a dict with the name as key'''

    def __init__(self, lines: deque[str]) -> None:
        self.start_pts = []

        for line in lines:
            node = Node(line)
            self[node.name] = node

            # Maintain a list of starting points
            if node.start_node:
                self.start_pts.append(node)


    def set_relations(self) -> None:
        '''Set all the pointers'''
        for node in self.values():
            for (dir, node_name) in node.str_dirs.items():
                node.ptr_dirs[dir] = self[node_name]


    def find_exit(self, instrs: Instructions, start_node: Node,
                  exact_match = True) -> int:
        '''This function simply follows
        the nodes and instructions until the end is reached'''
        steps = 0
        cur_node = start_node
        cur_instr = instrs[0]

        while True:
            steps += 1
            # Discover next node depending on the instr.
            cur_node = cur_node.ptr_dirs[cur_instr.dir]

            # Exact match is used for solution 1
            if exact_match:
                # If end is reached, terminate
                if cur_node.name == END:
                    break
            else:
                if cur_node.name[2] == 'Z':
                    break

            # Go to next intruction
            cur_instr = cur_instr.next_instr

        return steps


def find_solution(freqs: list[int]) -> int:
    '''This function tries to find a mutual factor where all
    frequencies match'''
    # Using the maximum of the frequencies as a base
    # That will decrease the computation time
    step = max(freqs)
    solution = 0
    all_match = False

    while not all_match:
        solution += step
        # print(solution)
        all_match = True

        for freq in freqs:
            # Check if the solution is a multiple factor of freq
            if solution / freq != solution // freq:
                all_match = False
                break


    return solution


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    # define lines as a deque so I can easily remove
    # the top few lines
    lines = deque(lines)
    # Use the top line to define Instructions
    instrs = Instructions(lines.popleft())
    # Remove empty line
    lines.popleft()

    # Use the rest to define Nodes
    nodes = Nodes(lines)
    # Set the pointer attributes of the Nodes
    nodes.set_relations()

    return nodes.find_exit(instrs, nodes[BEGIN])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    lines = deque(lines)
    instrs = Instructions(lines.popleft())
    lines.popleft()

    nodes = Nodes(lines)
    nodes.set_relations()

    # This is a list of the frequencies in which each start point
    # reaches an end point
    freqs = []

    # Now find the end points one by one and note down the steps (frequencies)
    for start_node in nodes.start_pts:
        freqs.append(nodes.find_exit(instrs, start_node, exact_match=False))

    pprint(freqs)

    return find_solution(freqs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass