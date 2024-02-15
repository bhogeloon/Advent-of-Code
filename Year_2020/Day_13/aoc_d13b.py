"""
Year 2020, Day 13, Part 1

Problem description: See https://adventofcode.com/2020/day/13

"""

# Imports
from calendar import c
from pprint import pprint
from collections import deque


# Constants
MIN_SOL = 100000000000000

# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes
class BusStation(list):
    def __init__(self, lines: list[str]) -> None:
        self.current_timestamp = int(lines[0])
        max_bus_line = 0
        self.max_bus = None

        bus_lines = lines[1].split(',')

        for (i, bus_line) in enumerate(bus_lines):
            if bus_line == 'x':
                continue

            bus_line_int = int(bus_line)
            new_bus = Bus(bus_line_int, i)
            self.append(new_bus)
            if bus_line_int > max_bus_line:
                max_bus_line = bus_line_int
                self.max_bus = new_bus


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


    def get_solution(self) -> int:
        # t = -self.max_bus.off_set
        t = MIN_SOL - (MIN_SOL % self.max_bus.bus_line) - self.max_bus.off_set
        found_solution = False
        report_t = 0

        while not found_solution:
            t += self.max_bus.bus_line
            # t += 1
            found_solution = True

            for bus in self:
                if t > report_t:
                    print(t)
                    report_t += 10000000000

                if (t+bus.off_set) % bus.bus_line > 0:
                    found_solution = False
                    break

        return t


class Bus():
    def __init__(self, bus_line, off_set) -> None:
        self.bus_line = bus_line
        self.off_set = off_set


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

    return bus_station.get_solution()

    return __name__


if __name__ == '__main__':
    pass