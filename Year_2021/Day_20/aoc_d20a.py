"""
Day 20, Part 1

Problem description: See https://adventofcode.com/2021/day/20

My solution:
Part 1:

"""

# Imports
from collections import Counter

# Constants

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def get_pixel_number(image_lines: list, x: int, y: int, border_char: str) -> int:
    '''Get the binary number from the 9 surrounding pixels'''

    def insert_row(image_lines, x, sub_y, border_char):
        '''Inserts a row with data from the image_lines'''
        if x == 0:
            row = border_char + image_lines[sub_y][x] + image_lines[sub_y][x+1]
        elif x == len(image_lines[sub_y]) - 1:
            row = image_lines[sub_y][x-1] + image_lines[sub_y][x] + border_char
        else:
            row = image_lines[sub_y][x-1:x+2]

        return row


    sub_matrix = []

    # For y-1
    if y == 0:
        sub_matrix.append(border_char * 3)
    else:
        sub_matrix.append(insert_row(image_lines, x, y-1, border_char))

    # For y
    sub_matrix.append(insert_row(image_lines, x, y, border_char))

    # For y+1
    if y == len(image_lines) - 1:
        sub_matrix.append(border_char * 3)
    else:
        sub_matrix.append(insert_row(image_lines, x, y+1, border_char))

    # Now calculate bin_string
    bin_str = ''
    for row in sub_matrix:
        for char in row:
            if char == '#':
                bin_str += '1'
            else:
                bin_str += '0'

    return int(bin_str, 2)


def enhance_image(input_lines: list, algorithm: str, border_char: str) -> list:
    '''Return a new image which is the enhanced version of the input'''
    output_lines = []

    for y, input_line in enumerate(input_lines):
        output_line = ''

        for x, input_char in enumerate(input_line):
            # Enhancement to be done
            pixel_number = get_pixel_number(input_lines, x, y, border_char)
            output_line += algorithm[pixel_number]

        output_lines.append(output_line)

    return output_lines


def count_light_pixels(image_lines: list) -> int:
    '''Counts the number of # in all lines'''
    total_light_pixels = 0

    for image_line in image_lines:
        ctr = Counter(image_line)
        total_light_pixels += ctr['#']

    return total_light_pixels


def extend_image(image_lines: list, extend_char: str) -> list:
    '''return an image extended with the char extend_char'''
    new_image = []

    # First append an entire row with new chars
    new_image.append(extend_char * (len(image_lines[0]) + 2))

    for image_line in image_lines:
        new_line = extend_char + image_line + extend_char
        new_image.append(new_line)

    new_image.append(extend_char * (len(image_lines[0]) + 2))

    return new_image


def get_nr_of_light_pixels(image_lines: list, algorithm: str) -> int:
    '''Main function'''

    image_lines = extend_image(image_lines, '.')
    image_lines = enhance_image(image_lines, algorithm, '.')
    image_lines = extend_image(image_lines, algorithm[0])
    image_lines = enhance_image(image_lines, algorithm, algorithm[0])

    for image_line in image_lines:
        print(image_line)

    return count_light_pixels(image_lines)


if __name__ == '__main__':
    lines = read_input('input.txt')
    algorithm = read_input('algorithm.txt')[0]
    # lines = read_input('example1.txt')
    print("Number of light pixels:", get_nr_of_light_pixels(lines, algorithm))
