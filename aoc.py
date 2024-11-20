"""
Main wrapper module for executing the aoc puzzle solutions
See Readme.md for more information
"""

# Imports

import sys
import os
from importlib import import_module
import argparse
from datetime import datetime
from aoc_lib.aoc_file_handling import read_input
from aoc_lib.aoc_file_handling import get_aoc_module
from aoc_lib.aoc_file_handling import get_input_file
import logging

sys.path.append(os.getcwd() + '/aoc_lib')

# Constants

START_YEAR = 2015
START_TIME = datetime.now()
CUR_YEAR = START_TIME.year
YEAR = 2023
DAY = 1
PART = 'a'
INPUT_FN = 'input.txt'
# INPUT_FN = 'test.txt'


# Argument parsing
argp = argparse.ArgumentParser(description="Advent of Code wrapper")

argp.add_argument(
    '--year', '-y', type=int, choices=[y for y in range(START_YEAR, CUR_YEAR+1)],
    help="Year",
)

argp.add_argument(
    '--day', '-d', type=int, choices=range(1, 26),
    help="Day",
)

argp.add_argument(
    '--part', '-p', type=str, choices=['a', 'b', '1', '2'],
    help="Part",
)

argp.add_argument(
    '--input', '-i', type=str, default='',
    help="Input file name",
)

argp.add_argument(
    '--test', '-t', action='store_true',
    help="Use test.txt as input file",
)

argp.add_argument(
    '--old_format', '-o', action='store_true',
    help="Use old format",
)

argp.add_argument(
    '--debug', '-b', action='store_true',
    help='Turn on debug messages'
)

argp.add_argument(
    '--log_file', '-l', action='store_true',
    help='Store logging in filename aoc.log'
)

args = argp.parse_args()

# Configure the logger
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(message)s',level=logging.INFO)

if args.debug:
    logger.setLevel(logging.DEBUG)

if args.year:
    YEAR = args.year

if args.day:
    DAY = args.day

if args.part:
    if args.part == '1':
        PART = 'a'
    elif args.part == '2':
        PART = 'b'
    else:
        PART = args.part

YEAR_DIR = f"Year_{YEAR}"
DAY_DIR = f"Day_{DAY:02d}"
DIR = f"{YEAR_DIR}/{DAY_DIR}/"

if args.old_format:
    MODULE = f"{YEAR_DIR}.{DAY_DIR}.aoc_d{DAY:02d}{PART}"
else:
    MODULE = f"{YEAR_DIR}.{DAY_DIR}.{get_aoc_module(DIR)}"

# Open log file if required
if args.log_file:
    LOG_FILE = f"{DIR}/aoc.log"
    logger.addHandler(logging.FileHandler(
        LOG_FILE,
        encoding='utf-8',
        mode='w',
    ))

# Import current script
aoc_module = import_module(MODULE)

# Determine input file
if args.test:
    input_fn = get_input_file(DIR, 'test')
elif args.input == '':
    input_fn = get_input_file(DIR)
else:
    input_fn = args.input

INPUT_FILE = DIR + input_fn

lines = read_input(INPUT_FILE)
# lines = read_input(DAY_DIR + '/example1.txt')

print()

if args.old_format:
    print("Solution:", aoc_module.get_solution(lines))
else:
    if PART == 'a':
        print(
            "Solution part 1:",
            aoc_module.get_solution_part1(lines,test=args.test,logger=logger)
        )
    else:
        print(
            "Solution part 2:",
            aoc_module.get_solution_part2(lines,test=args.test,logger=logger)
        )


# Print time consumed
end_time = datetime.now()
total_time = end_time - START_TIME
print()
hours = int(total_time.total_seconds() // 3600)
mins = int(total_time.total_seconds()//60 % 60)
secs = total_time.total_seconds() % 60
print(f"Time to execute: {hours} hours, {mins} minutes, {secs} seconds")
