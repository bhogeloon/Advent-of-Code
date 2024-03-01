"""
Year 2022, Day 6

Problem description: See https://adventofcode.com/2022/day/6

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
        self.chars_processed = 0
        self.last_4 = deque()
        self.last_14 = deque()

        for line in lines:
            self.extend(list(line))


    def process_char(self) -> bool:
        '''Process a character. If last one return False, otherwise True'''

        if len(self.last_4) == 4:
            self.last_4.popleft()

        if len(self.last_14) == 14:
            self.last_14.popleft()
            
        self.last_4.append(self[self.chars_processed])
        self.last_14.append(self[self.chars_processed])
        self.chars_processed += 1

        if self.chars_processed == len(self):
            return False
        else:
            return True


    def last_4_unique(self) -> bool:
        '''Return True if last 4 are all different'''
        return len(self.last_4) == len(set(self.last_4))


    def last_14_unique(self) -> bool:
        '''Return True if last 4 are all different'''
        return len(self.last_14) == len(set(self.last_14))


    def look_for_start_seq(self) -> int:
        while self.process_char():
            if self.chars_processed >= 4:
                if self.last_4_unique():
                    return self.chars_processed
                
        return 'Not found'


    def look_for_msg_seq(self) -> int:
        while self.process_char():
            if self.chars_processed >= 14:
                if self.last_14_unique():
                    return self.chars_processed

        return 'Not found'


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    signal_buf = SignalBuffer(lines)

    return signal_buf.look_for_start_seq()

    # return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    signal_buf = SignalBuffer(lines)

    return signal_buf.look_for_msg_seq()

    # return 'part_2 ' + __name__


if __name__ == '__main__':
    pass