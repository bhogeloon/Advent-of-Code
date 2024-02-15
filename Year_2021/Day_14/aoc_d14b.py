"""
Day 14, Part 2

Problem description: See https://adventofcode.com/2021/day/14

My solution:
Part 1:
- Read the first line and store in variable polymer
- Read the rest of the lines and store it in a dict called pair_ins
- Create function to do the insertions (pol_insert). This will create
  a new polymer string which replaces the old one.
- Execute function 10 times
- Write a function to return a dict with the amount of occurrunces
  per element (get_element_occurences)

Part 2:
Simply run the cycle 40 times? Well that takes too long.
Instead we are going to build an alternative dict, which calculates the insertion string
of each entry after 20 cycles. We can then insert this string in 2 cycles each. In the second 
we only count the occurences.
This way, it only takes a bit more than 2 minutes to complete.
"""

# Imports
from collections import Counter

# Global values


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def pol_insert(old_pol: str, pair_ins: dict) -> str:
    '''Returns a new string with the inserted elements'''
    new_pol = ''

    for nr in range(len(old_pol)):
        # Write current char
        new_pol += old_pol[nr]
        # Don't look ahead if last char
        if nr < len(old_pol) - 1:
            char_left = old_pol[nr]
            char_right = old_pol[nr + 1]
            combi = char_left + char_right
            # Check if a key exist
            if combi in pair_ins.keys():
                # Write extra element
                new_pol += pair_ins[combi]

    return new_pol


def pol_insert_cnt(old_pol: str, pair_cnt20: Counter, cnt: Counter):
    '''updates the cnt object'''

    for nr in range(len(old_pol)):
        # Don't look ahead if last char
        if nr < len(old_pol) - 1:
            char_left = old_pol[nr]
            char_right = old_pol[nr + 1]
            combi = char_left + char_right
            # Check if a key exist
            if combi in pair_cnt20.keys():
                for element, el_amount in pair_cnt20[combi].items():
                    if element in cnt.keys():
                        cnt[element] += el_amount
                    else:
                        cnt[element] = el_amount

        if nr % 100000 == 0:
            print(nr * 100 // len(old_pol), '%')

def create_pair_ins(lines: list) -> dict:
    '''Returns dict with the pair as key and the insertion as value'''
    pair_ins = {}

    for line in lines:
        pair, ins = line.split(' -> ')
        pair_ins[pair] = ins

    return pair_ins


def build_20_database(pair_ins: dict) -> dict:
    '''Returns an alternative dict with as values the string
    after 20 cycles.
    Also return a dict with a Counter object per pair'''
    db20 = {}
    counter20 = {}

    print ("keys:", len(pair_ins.keys()))

    n = 0

    for pair in pair_ins.keys():
        n += 1
        if n % 10 == 0:
            print(n)

        value20 = pair

        for i in range(20):
            value20 = pol_insert(value20, pair_ins)

        # Extract original pair
        db20[pair] = value20[1:-1]
        counter20[pair] = Counter(db20[pair])

    return db20, counter20


def get_difference(lines):
    '''Main function to get the difference between max and min'''
    polymer = lines[0]

    pair_ins = create_pair_ins(lines[2:])

    db20, pair_cnt20 = build_20_database(pair_ins)

    # Now build the polymer string after 20 cycles
    polymer = pol_insert(polymer, db20)

    # Build counter object
    pol_cnt = Counter(polymer)

    # Calculate the next 20 cycles
    pol_insert_cnt(polymer, pair_cnt20, pol_cnt)

    min = -1
    max = 0

    for nr in pol_cnt.values():
        if nr > max:
            max = nr

        if min < 0 or nr < min:
            min = nr

    return max - min
 

if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Difference between max and min:", get_difference(lines))
