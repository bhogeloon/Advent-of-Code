"""
Year 2022, Day 6

Problem description: See https://adventofcode.com/2022/day/6

The following class is used:
- SignalBuffer: The sequence of signals. This is a list class containing the signals
as characters.

Part 1: Go through the list until we see that the last 4 characters are all different.

Part 2: Same excercise, but then for 14 characters
"""

# Imports
from pprint import pprint
from collections import deque

# Constants

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class SignalBuffer(list):
    '''Sequence of characters for the device signal'''

    def __init__(self, lines: list[str]) -> None:
        # Keeps track of the character being processed
        self.chars_processed = 0
        # Keeps track of the last 4 chars, to detect the start sequence
        self.last_4 = deque()
        # Keeps track of the last 14 chars, to detect the start-of-message
        self.last_14 = deque()

        # Keeps track of the last chars
        self.last = deque()

        for line in lines:
            self.extend(list(line))


    def process_char(self, nr=4) -> bool:
        '''Process a character. If last one return False, otherwise True'''

        # If last n is full, pop one out, so it can be filled again later
        if len(self.last) == nr:
            self.last.popleft()

        # Store the current char in the last 4
        self.last.append(self[self.chars_processed])
        self.chars_processed += 1

        # Check if the end is reached
        if self.chars_processed == len(self):
            return False
        else:
            return True


    def last_n_unique(self) -> bool:
        '''Return True if last n are all different'''
        return len(self.last) == len(set(self.last))


    def look_for_seq(self, nr=4) -> int:
        '''Find the sequence (nr different characters)'''
        while self.process_char(nr=nr):
            if self.chars_processed >= nr:
                if self.last_n_unique():
                    return self.chars_processed
                
        return 'Not found'


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    signal_buf = SignalBuffer(lines)

    return signal_buf.look_for_seq()

    # return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    signal_buf = SignalBuffer(lines)

    return signal_buf.look_for_seq(nr=14)

    # return 'part_2 ' + __name__


if __name__ == '__main__':
    pass