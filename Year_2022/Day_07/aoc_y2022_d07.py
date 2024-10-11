"""
Year 2022, Day 7

Problem description: See https://adventofcode.com/2022/day/7

The following classes are used:
- File: a File with a certain size
- Dir: a Directory containing files or other Dirs
- Filesystem: the total filesystem, containing also the main Dir (/)

Part 1: Build the filesystem. Then calculate the size of each dir.
If another dir is encountered then start the calculation recursively.
Once calculated, determine if the filesize is below maximum and if so,
add to the total.

Part 2: Go through the same function as part 1 to determine all dir sizes
Then search in each directory (again recursively) for any directory which 
would free enough space. Put them all in a list and report the minimum.

"""

# Imports
from pprint import pprint
from collections import deque

# Constants

MAX_DIR_SIZE = 100000
AVAILABLE_SPACE = 70000000
REQUIRED_SPACE = 30000000

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class FileSystem():
    '''Class that holds the top directory and manages all file and dir 
    actions'''

    # Class variables
    total = 0
    available_space = AVAILABLE_SPACE
    free_space = None
    additional_space = None


    def __init__(self, instructions: list) -> None:
        self.instructions = deque(instructions)
        self.topdir = Dir('/')
        self.curdir = self.topdir


    def process_all_instructions(self) -> None:
        '''Process all instructions in the list'''
        while len(self.instructions) > 0:
            self.process_cmd()


    def process_cmd(self) -> None:
        '''Process next instruction on the list'''
        cmd = self.instructions.popleft()

        # If not command, bail out
        if cmd[0] != '$':
            raise RuntimeError("This is not a command: {}".format(cmd))
        
        if cmd[2:4] == 'cd':
            self.change_dir(cmd[5:])
        elif cmd[2:] == 'ls':
            self.reg_content()
        else:
            raise RuntimeError("Unkown command: {}".format(cmd))


    def change_dir(self, target:str) -> None:
        '''Change the current directory based on target'''
        if target == '/':
            self.curdir = self.topdir
        elif target == '..':
            self.curdir = self.curdir.parent
        else:
            self.curdir = self.curdir.dirs[target]


    def reg_content(self) -> None:
        '''register files and dirs in the next lines'''
        while len(self.instructions) > 0 and self.instructions[0][0] != '$':
            content_line = self.instructions.popleft()
            content_words = content_line.split()

            if content_words[0] == 'dir':
                # Create new dir in current dir
                self.curdir.dirs[content_words[1]] = Dir(
                    content_words[1],
                    self.curdir,
                )
            else:
                # Create new file in current dir
                self.curdir.files.append(File(content_line, self.curdir))


    def get_total_filesize_below_max(self) -> int:
        '''Calculate the total size of all files smaller than MAX_FILE_SIZE'''
        self.topdir.get_total_filesize()

        FileSystem.free_space = self.available_space - self.topdir.size
        FileSystem.additional_space = REQUIRED_SPACE - self.free_space
        print(self.available_space,
              self.topdir.size,
              FileSystem.free_space,
              FileSystem.additional_space,
        )

        return self.total


    def find_lowest_dir_to_delete(self) -> int:
        '''find the lowest size possible to delete to fullfill the 
        requirement'''

        found_sizes = self.topdir.find_lowest_dir_to_delete()
        return min(found_sizes)


class Dir():
    '''A dir has a list of files, a dict of dirs (with name as key) and a 
    parent dir'''

    def __init__(self, name: str, parent = None) -> None:
        self.name = name
        self.files = []
        self.dirs = {}
        self.parent = parent


    def get_total_filesize(self) -> int:
        '''Calculate the total size of all files smaller than MAX_FILE_SIZE'''
        total_dir = 0

        # print(self.name, ' {')
        for dir in self.dirs.values():
            total_dir += dir.get_total_filesize()

        for file in self.files:
            # print(file.name, file.size)
            total_dir += file.size
            # print('size added')

        # print('}')

        if total_dir <= MAX_DIR_SIZE:
            FileSystem.total += total_dir

        self.size = total_dir

        return total_dir


    def find_lowest_dir_to_delete(self) -> list:
        '''find the lowest size possible to delete to fullfill the 
        requirement'''

        found_sizes = []

        for dir in self.dirs.values():
            found_sizes.extend(dir.find_lowest_dir_to_delete())

        if self.size >= FileSystem.additional_space:
            found_sizes.append(self.size)

        return found_sizes


class File():
    '''File has a name and size. Also a pointer to which dir it belongs'''

    def __init__(self, instruction: str, parent: Dir) -> None:
        '''The instruction is the direct input line'''
        (size_str, self.name) = instruction.split()
        self.size = int(size_str)
        self.parent = parent


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    fs = FileSystem(lines)
    fs.process_all_instructions()

    return fs.get_total_filesize_below_max()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function'''

    fs = FileSystem(lines)
    fs.process_all_instructions()

    fs.get_total_filesize_below_max()

    return fs.find_lowest_dir_to_delete()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass