"""
Day 8, Part 1

Problem description: See https://adventofcode.com/2021/day/8

My solution:

Divide the lines in two sections and look at the second sections.
Count the number of instances with the unique length size. 

"""

def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def get_nr_of_hits(lines):
    nr_of_hits = 0

    for line in lines:
        (input_str, output_str) = line.split(' | ')
        digits = output_str.split()

        for digit in digits:
            if len(digit) in (2, 4, 3, 7):
                nr_of_hits += 1

    return nr_of_hits


if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Nr of hits:", get_nr_of_hits(lines))
