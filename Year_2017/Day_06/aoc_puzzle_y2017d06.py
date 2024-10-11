"""
Year 2017, Day 6

Problem description: See https://adventofcode.com/2017/day/6

The following class is used:
- MemoryBanks: A list class containing integer values (the memory content)

Part 1: Loop through the redestribution process, keeping a list of hash values
of each list situation. If a hash value is already in the list, break the
loop.

Part 2: Do the same as in part 1, but substract the index value of the found
matching hash.

"""

# Imports
from pprint import pprint


# Constants


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class MemoryBanks(list[int]):
    '''Represents the total amount of memory banks. It is a list
    of intergers.'''
    def __init__(self, line: str) -> None:
        self.extend([int(b) for b in line.split()])
        # List of hashes that is stored previously to detect a identical
        # combination
        self.found_hashes = []


    def find_loop(self) -> int:
        '''Find out at which point we create a loop.'''
        steps = 0

        while True:
            # Calculate new hash
            cur_hash = self.calculate_hash()

            if Gv.test:
                print(f'Step {steps}: {self}, hash: {cur_hash}')

            # If hash already found, terminate
            if cur_hash in self.found_hashes:
                # Store the answer to part 2
                self.loop_size = steps - self.found_hashes.index(cur_hash)
                return steps
            
            # Store hash
            self.found_hashes.append(cur_hash)

            # Get maximum
            max_nr = max(self)
            max_bank = self.index(max_nr)

            # Empty max_bank
            self[max_bank] = 0

            # Redistribute stuff
            i = max_bank + 1

            while max_nr > 0:
                if i == len(self):
                    i = 0

                self[i] += 1
                max_nr -= 1
                i += 1
            
            # Increase steps
            steps += 1
    

    def calculate_hash(self) -> int:
        '''Calculate the hash of the current list content'''
        return hash(tuple(self))


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    membanks = MemoryBanks(lines[0])

    return membanks.find_loop()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    membanks = MemoryBanks(lines[0])
    membanks.find_loop()

    return membanks.loop_size

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
