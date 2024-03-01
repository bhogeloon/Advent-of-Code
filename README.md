# Advent of Code puzzle solutions

## Author: Bert van Hogeloon

This Project contains my solutions for the Advent of Code puzzles (see [adventofcode.com](https://adventofcode.com/))

The aoc.py module in the main directory is the wrapper for executing all the different puzzle solutions.
Further more, there is a subdirectory for each year and in there, there is a subdirectory for each day.
Each day directory contains at least three files:

- aoc_puzzle.py: The python module which contains the solution (both part 1 and 2)
- input.txt: The puzzle input (the default input file).
- test.txt: The input that is provided as example in the puzzle description. This can be used for
  debugging purposes.

I like to use classes, but in this case I don't bother to create a file for each class, so every
solution is in one file.

To run the code, run the aoc.py module as follows:

```text
usage: aoc.py [-h] [--year {2019,2020,2021,2022,2023}]
              [--day {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25}] [--part {a,b,1,2}]
              [--input INPUT] [--test] [--old_format] [--not_so_old_format]

Advent of Code wrapper

options:
  -h, --help            show this help message and exit
  --year {2019,2020,2021,2022,2023}, -y {2019,2020,2021,2022,2023}
                        Year
  --day {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25}, -d {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25}
                        Day
  --part {a,b,1,2}, -p {a,b,1,2}
                        Part
  --input INPUT, -i INPUT
                        Input file name
  --test, -t            Use test.txt as input file
  ```
  