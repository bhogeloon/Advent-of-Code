"""
Year 2018, Day 2

Problem description: See https://adventofcode.com/2018/day/2

I created the following classes:
- Box: a box with items (letters) and also a set of item_types (unique letters)
- Boxes: Container class (list) of Box

For part 1: For each box, for each item_type, check the amount of occurences, 2 times and 3 times.

For part 2, I built a compare Box method, comparing each character one by one. The Boxes method
find_match, looks for a match using the compare function for all boxes that are further in the
list. It then removes the character from the position that differs and returns the remaining
string.
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

class Box():
    '''Candidate Box'''
    def __init__(self, line: str) -> None:
        self.items = line
        # Create a set of unique letters
        self.item_types = set(line)


    def check_multiple_entries(self, n: int) -> bool:
        '''Check if any letter appears n times in the items'''
        for char in self.item_types:
            if self.items.count(char) == n:
                return True
        
        # If no match found
        return False
    

    def compare(self, otherbox) -> int:
        '''This function compares the box with another Box object.
        If there is exactly one position different, it will return
        the position number that differs. If not, it will return -1'''
        diff_nr = 0
        pos = -1

        # Examine the string
        for i, char in enumerate(self.items):
            # If chars are different
            if char != otherbox.items[i]:
                diff_nr += 1
                pos = i

        # If exactly one difference
        if diff_nr == 1:
            return pos
        else:
           return -1


class Boxes(list[Box]):
    '''Container class of Box obects'''
    def __init__(self, lines: str) -> None:
        for line in lines:
            self.append(Box(line))


    def get_checksum(self) -> int:
        '''Get the checksum by checking all letters appearing two 
        or three times'''
        double_count = 0
        triple_count = 0

        for box in self:
            if box.check_multiple_entries(2):
                double_count += 1
            if box.check_multiple_entries(3):
                triple_count += 1

        return double_count * triple_count
    

    def find_match(self) -> str:
        '''This function will try and find a match between two
        boxes where only one letter is different. It will return
        the remaining letters.'''

        # For all boxes
        for i, box in enumerate(self):

            # For all remaining boxes
            for j in range(i, len(self)):
                pos = box.compare(self[j])

                if pos == -1:
                    continue

                result = box.items
                result_list = list(result)

                # Remove the character from pos
                del result_list[pos]

                return ('').join(result_list)

        return 'no match found'


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    boxes = Boxes(lines)

    return boxes.get_checksum()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    boxes = Boxes(lines)

    return boxes.find_match()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
