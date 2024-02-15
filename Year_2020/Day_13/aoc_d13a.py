"""
Year 2020, Day 13, Part 1

Problem description: See https://adventofcode.com/2020/day/13

"""

# Imports
from calendar import c
from pprint import pprint
from collections import deque
from tkinter import N

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes
class BusStation(list):
    def __init__(self, lines: list[str]) -> None:
        super().__init__()
        self.current_timestamp = int(lines[0])

        bus_lines = lines[1].split(',')

        for bus_line in bus_lines:
            if bus_line == 'x':
                continue

            self.append(Bus(int(bus_line)))


    def get_min_waiting_time(self):
        min_waiting_time = 1000000000
        mybus = None

        for bus in self:
            waiting_time = bus.get_waiting_time(self.current_timestamp)
            if waiting_time < min_waiting_time:
                min_waiting_time = waiting_time
                mybus = bus

        mybus.waiting_time = min_waiting_time
        return mybus


class Bus():
    def __init__(self, bus_line) -> None:
        self.bus_line = bus_line


    def get_waiting_time(self, current_timestamp: int) -> int:
        mod_value = current_timestamp % self.bus_line

        if mod_value == 0:
            return 0
        else:
            return self.bus_line - mod_value


# Functions



# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    bus_station = BusStation(lines)

    mybus = bus_station.get_min_waiting_time()

    return mybus.waiting_time * mybus.bus_line

    return __name__


if __name__ == '__main__':
    pass