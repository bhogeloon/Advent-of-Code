"""
This module contains a function to get the aoc module from a particular directory.
It tries to get the best choice.
"""

import os
import re


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


if __name__ == '__main__':
    curdir = os.curdir
    dir = curdir + '/test-dir'

    get_aoc_module(dir)