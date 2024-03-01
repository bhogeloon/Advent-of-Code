This Project contains my solutions for the Advent of Code puzzles (see https://adventofcode.com/)

The aoc.py module in the main directory is the wrapper for executing all the different puzzle solutions.
Further more, there is a subdirectory for each year and in there, there is a subdirectory for each day.
Each day directory contains at least three files:
- aoc_puzzle.py: The python module which contains the solution (both part 1 and 2)
- input.txt: The puzzle input.
- test.txt: The input that is provided as example in the puzzle description. This can be used for
  debugging purposes.

I like to use classes, but in this case I don't bother to create a file for each class, so every
solution is in one file.

To run the code, run the aoc.py module as follows:
