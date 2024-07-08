"""
This module contains several function for handling input, output and module files.
"""

import os
import re

def read_input (filename):
    '''Open the input file and store it in a list of lines'''
    with open(filename,encoding='utf-8') as f:
        data = f.read()

    return data.splitlines()


def _get_candidates(search_str: str, files: list[str]) -> list[str]:

    def _search_py(filename: str) -> bool:
        return re.search(search_str+'\.py$', filename)
    
    return list(filter(_search_py, files))


def get_aoc_module(dir: str) -> str:
    # Get all files in dir
    all_files = os.listdir(path=dir)

    # Check for aoc_puzzle
    # candidates = list(filter(_search_py(all_files, 'aoc_puzzle.*')))
    candidates = _get_candidates('^aoc_puzzle.*', all_files)

    # If no candidates found, try to look for anything that starts with aoc
    if len(candidates) == 0:
        candidates = _get_candidates('^aoc.*', all_files)

    # If more than one candidate found, report the one that is being used
    if len(candidates) > 1:
        print("More than one module found. Using: {}".format(candidates[0]))

    # Strip off .py
    return candidates[0][:-3]


if __name__ == '__main__':
    curdir = os.curdir
    dir = curdir + '/test-dir/'

    print(get_aoc_module(dir))