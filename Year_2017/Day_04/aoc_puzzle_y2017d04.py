"""
Year 2017, Day 4

Problem description: See https://adventofcode.com/2017/day/4

The following classes are used:
- Word: A word in a passphrase
- Passphrase: represents a passphrase with multiple Word objects
- Passphrases: List container class of Passphrase objects

Part 1 is simple: just check if there are any duplicates by putting all words in a 
set and then see if the amount of words in the set is still the same (as every word
should be unique).

Part 2 is slightly more complicated. To decide whether a word is an anagram of 
another word, two things must be checked:
- If the length is different, it is for sure no anagram.
- If the length is the same, check for every occuring character whether the amount 
    occurring characters is the same in both words. If this is the case for all 
    characters, then it is an anagram.
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

class Word():
    '''Represents a single word in passphrase'''
    def __init__(self, word:str) -> None:
        self.wrd = word


    def is_anagram_of(self, other_word) -> bool:
        '''Check if other_word is an anagram of word'''
        if len(self.wrd) != len(other_word.wrd):
            return False
        
        for char in set(self.wrd):
            if self.wrd.count(char) != other_word.wrd.count(char):
                return False

        return True


class Passphrase():
    '''Contains a passphrase of several words'''
    def __init__(self, line:str) -> None:
        self.passphrase = line
        self.words = [Word(word) for word in line.split()]


    def is_valid_p1(self) -> bool:
        '''Checks if there no duplicate words in the passphrase'''
        return len(self.words) == len(set([word.wrd for word in self.words]))
    

    def is_valid_p2(self) -> bool:
        '''Check if no anagrams occur'''
        for (i, word) in enumerate(self.words):
            for j in range(i+1,len(self.words)):
                if word.is_anagram_of(self.words[j]):
                    return False
                
        return True


class Passphrases(list[Passphrase]):
    '''List container class of Passphrase objects'''
    def __init__(self, lines:list[str]) -> None:
        for line in lines:
            self.append(Passphrase(line))


    def valid_amount_p1(self) -> int:
        '''Return the number of valid passwords for part 1'''
        result = 0

        for passphrase in self:
            if passphrase.is_valid_p1():
                result += 1

        return result
    

    def valid_amount_p2(self) -> int:
        '''Return the number of valid passwords for part 2'''
        result = 0

        for passphrase in self:
            if passphrase.is_valid_p2():
                result += 1

        return result



# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    passphrases = Passphrases(lines)

    return passphrases.valid_amount_p1()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    passphrases = Passphrases(lines)

    return passphrases.valid_amount_p2()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
