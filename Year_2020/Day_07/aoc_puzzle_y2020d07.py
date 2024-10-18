"""
Year 2020, Day 7

Problem description: See https://adventofcode.com/2020/day/7

The following classes are used:
- Bag: represents a bag with a certain colour. It also has an attribute
content, which is a list of dicts. The 'bag' key points to another Bag 
object and the 'nr' key indicates the amount of bags of that colour present.
-Bags: The complete list of bags. It is a dict class with colour as key.

Part 1: Build the Bags object with all the puzzle input information. Then 
for each bag, go through the content recursively until you find the shiny 
gold bag. If so, increase the counter.

Part 2: Recursively calculate the amount of bags inside the shiny gold one.
"""

# Imports
from __future__ import annotations
from pprint import pprint
import re

# Constants
CHECK_COLOUR = 'shiny gold'


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Bag:
    '''Represents a bag, containing other bags'''
    def __init__(self, colour: str) -> None:
        self.colour = colour
        # content is a a list of dicts. Each dict has a key 'bag' with as value
        # a link to another Bag and 'nr' with as value the number of bags
        self.content = []


    def fill_content(self, line: str, bags: Bags) -> None:
        '''Fill the bag with other bags, based on line'''
        bag_content_parts = line.split(', ')

        for bag_content_part in bag_content_parts:
            m = re.fullmatch(r'(\d+) (.*) bags?', bag_content_part)

            cont_amount = int(m.group(1))
            cont_colour = m.group(2)

            # Create new bag if it doesn't exist
            if cont_colour not in bags.keys():
                bags[cont_colour] = Bag(cont_colour)

            # Add bag to content
            new_content = {
                'bag': bags[cont_colour],
                'nr': cont_amount,
            }
            self.content.append(new_content)


    def find_my_bag(self) -> bool:
        '''Return True if the shiny gold bag is found'''
        for item in self.content:
            if item['bag'].colour == CHECK_COLOUR:
                return True
            elif item['bag'].find_my_bag():
                return True
        
        return False
    

    def get_nr_of_bags(self) -> int:
        '''Return the number of bags that fits into this one'''
        result = 0

        for item in self.content:
            result += item['nr'] + item['nr'] * item['bag'].get_nr_of_bags()

        return result


class Bags(dict[Bag]):
    '''Dict class of bags. The key is the bag colour, while the value
    is another Bags object (which may be an empty dict)'''
    def __init__(self, lines: list[str]=None) -> None:
        for line in lines:
            m = re.fullmatch(r'(.*) bags contain (.*)\.', line)

            bag_colour = m.group(1)
            bag_content_line = m.group(2)

            # If no bags with this colour exists, create one
            if bag_colour not in self.keys():
                self[bag_colour] = Bag(bag_colour)

            # If there is any content, add it
            if bag_content_line != 'no other bags':
                self[bag_colour].fill_content(bag_content_line, self)

    def find_my_bags(self) -> int:
        '''Find the bags, containing the shiny gold one as requested in
        part 1'''
        valid_bags = 0

        for bag in self.values():
            if bag.find_my_bag():
                valid_bags += 1

        return valid_bags


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    bags = Bags(lines)

    return bags.find_my_bags()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    bags = Bags(lines)

    return bags[CHECK_COLOUR].get_nr_of_bags()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
