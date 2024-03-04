"""
Year 2018, Day 1

Problem description: See https://adventofcode.com/2018/day/1

I have created the following classes:
Frequency: The actual frequency (the end result of part 1)
FrequencyChange: The change in frequency (each line in the puzzle input)
FrequencyChanges: The list of all changes.

For the first part: go through the list and keep adding the change.

For the second part, I first make the FrequencyChanges list a circular list.
Then I itterate over that list, keeping track of all frequencies outcome.
This takes a bit more than 2 minutes to execute, so this could
be optimized I guess, but I currently don't have any ideas on how to 
do that.

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

class Frequency():
    '''The resulting frequency'''

    def __init__(self) -> None:
        self.freq = 0

        # Create a list of frequencies that have already been seen
        self.seen_freqs = [0]

    
    def change(self, fc) -> bool:
        '''Change the frequency according the the FrequencyChange.
        Returns True if the frequency was already seen'''
        self.freq += fc.change

        # If frequency already seen
        if self.freq in self.seen_freqs:
            return True
        # Otherwise add freq to seen freqs
        else:
            self.seen_freqs.append(self.freq)
            return False


    def change_all(self, fcs) -> None:
        '''Change the frequence following the list of changes'''
        for fc in fcs:
            self.change(fc)


    def get_recurring(self, fcs) -> int:
        '''Get the first recurring frequency'''
        fc = fcs[0]

        n = 0

        while not self.change(fc):
            fc = fc.next
            n += 1

            if n % 10000 == 0:
                print(n)
            #     pprint(self.seen_freqs)
            #     break

        return self.freq



class FrequencyChange():
    '''The change in frequency'''
    def __init__(self, line:str) -> None:
        self.change = int(line)



class FrequencyChanges(list[FrequencyChange]):
    '''Container class (list) of FrequencyChange objects'''
    def __init__(self, lines:list[str]) -> None:
        for line in lines:
            self.append(FrequencyChange(line))


    def set_relations(self) -> None:
        '''This function creates a pointer in each FrequencyChange
        object to the next one. The last one will loop back to the
        first'''

        for i in range(len(self)-1):
            self[i].next = self[i+1]

        self[-1].next = self[0]


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    fcs = FrequencyChanges(lines)

    freq = Frequency()
    freq.change_all(fcs)

    return freq.freq

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    fcs = FrequencyChanges(lines)
    fcs.set_relations()

    freq = Frequency()

    return freq.get_recurring(fcs)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
