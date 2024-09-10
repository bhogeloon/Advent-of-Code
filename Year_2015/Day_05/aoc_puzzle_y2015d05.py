"""
Year 2015, Day 5

Problem description: See https://adventofcode.com/2015/day/5

The following classes are used:
- SantaString: str class containing the string
- TextFile: container class of SantaString objects

Part 1: Run the three checks on each string and count the nice ones.

Part 2:
- For the first check, divice the string each time in three sections:
    - The substring of two characters (iterating over the whole string)
    - The remainder before the substring
    - The remainder after the substring
    If the substring is part of either remainder, the check is valid.
- For the second check, consider a group of three characters through
    the string. Then compare the first and last character of that group
    of three.

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

class SantaString(str):
    '''A string which is either nice or naughty'''
    # def __init__(self, line: str) -> None:
    #     pass

    # Class variables
    vowels = 'aeiou'
    substr_not_allowed = (
        'ab', 
        'cd',
        'pq',
        'xy',
    )


    def is_nice(self, part=1) -> bool:
        '''Check if the string is nice or naughty'''
        if part == 1:
            return (
                self.has_3_vowels() and 
                self.check_double() and 
                self.check_allowed_substr()
            )
        else:
            return (
                self.has_repeating_pair() and
                self.repeating_char_with_1_between()
            )
    

    def has_3_vowels(self) -> bool:
        '''Returns True if the string has 3 vowels'''
        nr_of_vowels = 0

        for char in self:
            if char in self.vowels:
                nr_of_vowels += 1

        return nr_of_vowels >= 3


    def check_double(self):
        '''Returns True if a double value is detected'''
        prev_char = ''
        for char in self:
            if char == prev_char:
                return True
            prev_char = char

        return False
    

    def check_allowed_substr(self) -> bool:
        '''Returns True if the string does not contain any of the 
        disallowed substr'''
        for substring in self.substr_not_allowed:
            if substring in self:
                return False
            
        return True
    

    def has_repeating_pair(self) -> bool:
        '''Returns True if it has a repeating, non-overlapping pair'''
        # Repeat for all character pairs
        for i in range(len(self) - 1):
            substring = self[i:i+2]
            remainder1 = self[:i]
            remainder2 = self[i+2:]

            if substring in remainder1 or substring in remainder2:
                return True

        return False
    

    def repeating_char_with_1_between(self) -> bool:
        '''Returns True if it finds a character that repeats itself with
        one character in between'''
        # Repeat for all character trios
        for i in range(len(self) - 2):
 
            # If character in i equals the character two places away
            if self[i] == self[i+2]:
                return True

        return False


class TextFile(list[SantaString]):
    '''List container class of SantaString objects'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(SantaString(line))


    def get_nr_of_nice(self, part=1) -> int:
        '''Return the number of nice strings'''
        nr_of_nice = 0

        for santastring in self:
            if santastring.is_nice(part=part):
                nr_of_nice += 1

        return nr_of_nice
    

# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    text_file = TextFile(lines)

    return text_file.get_nr_of_nice()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    text_file = TextFile(lines)

    return text_file.get_nr_of_nice(part=2)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
