"""
Day 13, Part 2

Problem description: See https://adventofcode.com/2021/day/13

My solution:
For part 1:
This solution was solved step by step.
First step is to read the coordinates into a coordinate list (get_coord_list).
Next is to create an empty sheet (all values False) with MAX_X, MAX_Y size (create_empty_sheet).
Then this map needs to be filled with the coordinate list (fill_sheet).
Next, we need a function to read the instructions and store it in a list of dicts,
with keys 'xy' and 'nr' (create_instr_table).

Next comes the tricky part: the folding. For now, I only implement the x-folding as we
only have to process the first instruction (x_fold).

For this we create a new sheet with a maximum x value of the folding side. Then we go through
the new matrix and consider each time the point with the same coordinates on the old
sheet, as well as the 'mirrored' point (if it exists at all of course). If one of
them is True, the new value is True.
In the end, the old map is replaced with the new map.

The final function is to count the dots (count_dots).

For part 2:
First we make the y_fold function in the same way as the x_fold.
Then we execute all instructions in the main function.
Then finally, we create a function to write the matrix to a file so we can have a
look at the characters that will appear (write_sheet)

"""


# Global values
MAX_X = 1400
MAX_Y = 1000

def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def get_coord_list(coord_lines: list) -> list:
    '''This function returns a list of coordinate tuples'''
    coord_list = []

    for line in coord_lines:
        (x,y) = line.split(',')
        coord_list.append((int(x),int(y)))

    return coord_list


def create_empty_sheet(x_size:int, y_size:int) -> list:
    '''This function returns a matrix with all values False'''
    return [[False for x in range(x_size)] for y in range(y_size)]


def fill_sheet(coord_list:list, sheet:list):
    '''This function will fill the sheet according to the coordinate list'''
    for x,y in coord_list:
        sheet[y][x] = True


def create_instr_table(instr_lines: list) -> list:
    '''Creates a list of instructions'''
    instr_table = []

    for line in instr_lines:
        instr_entry = {}
        (instr_entry['xy'], nr_str) = line[11:].split('=')
        instr_entry['nr'] = int(nr_str)
        instr_table.append(instr_entry)

    return instr_table


def x_fold(old_sheet: list, x_axis: int) -> list:
    '''Returns a new sheet wich folds the old sheet on the x_axis'''
    # Create new empty sheet
    new_sheet = create_empty_sheet(x_axis, len(old_sheet))

    # Go through the new sheet
    for y in range(len(new_sheet)):
        for x in range(len(new_sheet[y])):
            # Determin if mirrord x is off the sheet
            mirror_x = (2 * x_axis) - x
            if mirror_x >= len(old_sheet[y]):
                new_sheet[y][x] = old_sheet[y][x]
            else:
                new_sheet[y][x] = old_sheet[y][x] or old_sheet[y][mirror_x]

    return new_sheet


def y_fold(old_sheet: list, y_axis: int) -> list:
    '''Returns a new sheet wich folds the old sheet on the y_axis'''
    # Create new empty sheet
    new_sheet = create_empty_sheet(len(old_sheet[0]), y_axis)

    # Go through the new sheet
    for y in range(len(new_sheet)):
        for x in range(len(new_sheet[y])):
            # Determin if mirrord x is off the sheet
            mirror_y = (2 * y_axis) - y
            if mirror_y >= len(old_sheet):
                new_sheet[y][x] = old_sheet[y][x]
            else:
                new_sheet[y][x] = old_sheet[y][x] or old_sheet[mirror_y][x]

    return new_sheet


def count_dots(sheet: list) -> int:
    '''Returns the number of True values in the matrix'''
    nr_of_dots = 0
    for row in sheet:
        for dot in row:
            if dot:
                nr_of_dots += 1

    return nr_of_dots


def write_sheet(sheet: list, filename: str):
    '''Writes the matrix to a file'''
    data = ''

    for row in sheet:
        for dot in row:
            if dot:
                data += '#'
            else:
                data += ' '
        
        data += '\n'

    with open(filename, 'w') as f:
        f.write(data)


def get_nr_of_dots(coord_lines, instr_lines):
    '''Main function to get the number of paths'''
    nr_of_dots = 0

    coord_list = get_coord_list(coord_lines)
    sheet = create_empty_sheet(MAX_X, MAX_Y)
    fill_sheet(coord_list, sheet)
    instr_table = create_instr_table(intr_lines)

    # Now fold sheet according to the instructions
    for instr in instr_table:
        if instr['xy'] == 'x':
            sheet = x_fold(sheet, instr['nr'])
        else:
            sheet = y_fold(sheet, instr['nr'])

    write_sheet(sheet, 'output.txt')

    return count_dots(sheet)


if __name__ == '__main__':
    coord_lines = read_input('coord.txt')
    intr_lines = read_input('instr.txt')
    print("Number of dots after first fold:", get_nr_of_dots(coord_lines, intr_lines))
