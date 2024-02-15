"""
Year 2023, Day 8

Problem description: See https://adventofcode.com/2023/day/8

"""

# Imports
from pprint import pprint
from collections import deque

# Constants
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
        self.name = line[0:3]
        self.str_dirs = {
            'L': line[7:10],
            'R': line[12:15],
        }
        
        self.ptr_dirs = {}

        if self.name[2] == 'A':
            self.start_node = True
        else:
            self.start_node = False

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
            if node.start_node:
                self.start_pts.append(node)


    def set_relations(self) -> None:
        for node in self.values():
            for (dir, node_name) in node.str_dirs.items():
                node.ptr_dirs[dir] = self[node_name]


    def find_exit(self, instrs: Instructions, start_node: Node,
                  exact_match = True) -> int:
        steps = 0
        cur_node = start_node
        cur_instr = instrs[0]

        while True:
            steps += 1
            cur_node = cur_node.ptr_dirs[cur_instr.dir]

            if exact_match:
                if cur_node.name == END:
                    break
            else:
                if cur_node.name[2] == 'Z':
                    break

            cur_instr = cur_instr.next_instr

        return steps


    def find_exit2(self, instrs: Instructions) -> int:
        steps = 0
        all_end = False
        cur_instr = instrs[0]

        while not all_end:
            all_end = True
            steps += 1

            for i in range(len(self.start_pts)):
                self.start_pts[i] = self.start_pts[i].ptr_dirs[cur_instr.dir]
                if not self.start_pts[i].end_node:
                    all_end = False

            cur_instr = cur_instr.next_instr

        return steps


def find_solution(freqs: list[int]) -> int:
    step = max(freqs)
    solution = 0
    all_match = False

    while not all_match:
        solution += step
        # print(solution)
        all_match = True

        for freq in freqs:
            if solution / freq != solution // freq:
                all_match = False
                break


    return solution


# Main functions
def get_solution_part1(lines: list[str]) -> int:
    '''Main function'''

    lines = deque(lines)
    instrs = Instructions(lines.popleft())
    lines.popleft()

    nodes = Nodes(lines)
    nodes.set_relations()

    return nodes.find_exit(instrs, nodes[BEGIN])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str]) -> int:
    '''Main function'''

    lines = deque(lines)
    instrs = Instructions(lines.popleft())
    lines.popleft()

    nodes = Nodes(lines)
    nodes.set_relations()

    freqs = []

    for start_node in nodes.start_pts:
        freqs.append(nodes.find_exit(instrs, start_node, exact_match=False))

    pprint(freqs)

    return find_solution(freqs)

    solution = 1

    for freq in freqs:
        solution *= freq

    return solution

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass