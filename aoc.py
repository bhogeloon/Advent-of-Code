# Imports

from read_input import read_input
from importlib import import_module
import argparse
from datetime import datetime
import sys

# Change path
sys.path.append('../aoc_lib')

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
    '--input', '-i', type=str, default=INPUT_FN,
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
    '--not_so_old_format', '-n', action='store_true',
    help="Use not so old format",
)


args = argp.parse_args()


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

if args.test:
    input_fn = 'test.txt'
else:
    input_fn = args.input

YEAR_DIR = "Year_{}".format(YEAR)
DAY_DIR = "Day_{:02d}".format(DAY)
INPUT_FILE = "{}/{}/{}".format(YEAR_DIR, DAY_DIR, input_fn)

if args.old_format:
    MODULE = "{year_dir}.{day_dir}.aoc_d{day:02d}{part}".format(
        year_dir = YEAR_DIR,
        day_dir = DAY_DIR,
        day = DAY,
        part = PART,
    )
elif args.not_so_old_format:
    MODULE = "{year_dir}.{day_dir}.aoc_y{year}_d{day:02d}".format(
        year_dir = YEAR_DIR,
        day_dir = DAY_DIR,
        day = DAY,
        year = YEAR,
    )
else:
    MODULE = "{year_dir}.{day_dir}.aoc_puzzle".format(
        year_dir = YEAR_DIR,
        day_dir = DAY_DIR,
    )


# Import current script
aoc_module = import_module(MODULE)

lines = read_input(INPUT_FILE)
# lines = read_input(DAY_DIR + '/example1.txt')

print()

if args.old_format:
    print("Solution:", aoc_module.get_solution(lines))
else:
    if PART == 'a':
        print("Solution part 1:", aoc_module.get_solution_part1(lines,test=args.test))
    else:
        print("Solution part 2:", aoc_module.get_solution_part2(lines,test=args.test))


# Print time consumed
end_time = datetime.now()
total_time = end_time - START_TIME
print()
print("Time to execute: {} hours, {} minutes, {} seconds".format(
    int(total_time.total_seconds() // 3600),
    int(total_time.total_seconds()//60 % 60),
    total_time.total_seconds() % 60,
))
