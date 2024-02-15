"""
Day 12, Part 2

Problem description: See https://adventofcode.com/2021/day/12

My solution:
First we store all known paths in a dict, with the starting point as 
the key. The value is the list of possible end-points.
Note that the start point can be the A end or the B end (because you
can also travel the other way).

We create an additional function to check the current_path on
validity. An occurence of a single small cave  is allowed, but
when we find a second one, we return it as invalid.
"""


# Global values
current_path = []
connections = {}


def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename) as f:
        data = f.read()

    return data.splitlines()


def invalid_path():
    '''Look at current_path and return True if invalid'''
    # First create a new path
    copy_path = []
    # This boolean will become True if one duplicat has been found
    one_dupl_small_cave = False

    # Now iterate over the current path
    for hop in current_path:
        # Check if hop is upper case
        if hop.isupper():
            pass
        elif hop in copy_path:
            # Check if the hop is a second start:
            if hop == 'start':
                return True
            # Check if there is already in occurance
            elif one_dupl_small_cave:
                return True
            else:
                one_dupl_small_cave = True
            
        # addn hop to copy_path
        copy_path.append(hop)

    return False

def calculate_path(start_point: str) -> int:
    '''Recursive function to calculate the path'''
    # If the current start_point is 'end', then we have a valid path
    if start_point == 'end':
        return 1

    # Then add this point to the path
    current_path.append(start_point)

    # If this point is a small cage we already visited, don't bother
    if invalid_path():
        current_path.pop()
        return 0

    paths_found = 0

    for end_point in connections[start_point]:
        paths_found += calculate_path(end_point)
    
    # Now remove the current point before returning
    current_path.pop()

    return paths_found


def get_paths_found(lines):
    '''Main function to get the number of paths'''
    # Read the lines in the dict
    for line in lines:
        (a_point, b_point) = line.split('-')

        if a_point not in connections.keys():
            connections[a_point] = []
        connections[a_point].append(b_point)

        # Reverse path
        if b_point not in connections.keys():
            connections[b_point] = []
        connections[b_point].append(a_point)

    # Now start the recursive function from start
    paths_found = calculate_path('start')

    return paths_found


if __name__ == '__main__':
    lines = read_input('input.txt')
    print("Number of paths found:", get_paths_found(lines))
