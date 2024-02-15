"""
Year 2023, Day 5

Problem description: See https://adventofcode.com/2023/day/5

"""

# Imports
from pprint import pprint
from collections import deque

# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''



# Classes
class Item():
    '''
    An Item object can be any item, from seed to location.
    In fact an Item object generally contains a whole range of those items
    as it has two attributes: base and length.
    '''

    def __init__(self, base: int, length=1) -> None:
        self.base = base
        self.length = length


class MapEntry():
    '''Contains the information for one map entry'''

    def __init__(self, line: str) -> None:
        dest_start, source_start, length = [int(nr) for nr in line.split()]
        self.source_min = source_start
        self.source_max = source_start + length -1
        self.dest_base = dest_start


    def get_dest(self, source: Item) -> Item:
        '''This function will return a destination as well as an additional
        split source that remains to be tested. If there are no sources remaining,
        the second return value will be None'''
        # if source base is within the mapentry range
        if source.base >= self.source_min and source.base <= self.source_max:
            # if the source range fits in the mapentry range
            if source.base + source.length - 1 <= self.source_max:
                dest_length = source.length
                new_source = None
            else:
                dest_length = self.source_max - source.base + 1
                new_source = Item(
                    self.source_max + 1,
                    source.length - dest_length,
                )

            new_item = Item(
                self.dest_base + (source.base - self.source_min),
                dest_length,
            )
            return new_item, new_source

        else:
            return None,None


class Map(list):
    '''Class containing a list of MapEntries'''

    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(MapEntry(line))


    def get_dest(self, source: Item) -> list[Item]:
        '''This function returns a list of items as the source
        item may be split into multiple ranges'''
        dests = []

        for map_entry in self:
            dest, new_source = map_entry.get_dest(source)

            if dest != None:
                dests.append(dest)
                # If additional sources need to be checked, call yourself
                if new_source != None:
                    dests.extend(self.get_dest(new_source))
                return dests
            
        return [source]


def ignore_empty_lines(lines: deque[str]) -> None:
    while lines[0] == '':
        lines.popleft()


def process_input(lines: deque[str]) -> list:
    '''Returns list of seeds'''
    # Get seeds
    line = lines.popleft()
    seeds_str, rest = line.split(':')
    seed_info = [int(s) for s in rest.split()]

    # Get seed-to-soil map
    map_lines = read_map_lines(lines)
    Map.seed_to_soil = Map(map_lines)

    # Get soil-to-fertilizer map
    map_lines = read_map_lines(lines)
    Map.soil_to_fertilizer = Map(map_lines)

    # Get fertilizer-to-water map
    map_lines = read_map_lines(lines)
    Map.fertilizer_to_water = Map(map_lines)

    # Get water-to-light map
    map_lines = read_map_lines(lines)
    Map.water_to_light = Map(map_lines)

    # Get light-to-temperature map
    map_lines = read_map_lines(lines)
    Map.light_to_temperature = Map(map_lines)

    # Get temperature-to-humidity map
    map_lines = read_map_lines(lines)
    Map.temperature_to_humidity = Map(map_lines)

    # Get humidity-to-location map
    map_lines = read_map_lines(lines)
    Map.humidity_to_location = Map(map_lines)

    return seed_info


def read_map_lines(lines: deque[str]) -> list:
    ignore_empty_lines(lines)
    lines.popleft()
    map_lines = []
    while lines[0] != '':
        map_lines.append(lines.popleft())
    return map_lines


def get_soils(seeds: list) -> list:
    soils = []

    for seed in seeds:
        soils.extend(Map.seed_to_soil.get_dest(seed))

    return soils


def get_fertilizers(seeds: list) -> list:
    soils = get_soils(seeds)
    fertilizers = []

    for soil in soils:
        fertilizers.extend(Map.soil_to_fertilizer.get_dest(soil))

    return fertilizers


def get_waters(seeds: list) -> list:
    fertilizers = get_fertilizers(seeds)
    waters = []

    for fertilizer in fertilizers:
        waters.extend(Map.fertilizer_to_water.get_dest(fertilizer))

    return waters


def get_lights(seeds: list) -> list:
    waters = get_waters(seeds)
    lights = []

    for water in waters:
        lights.extend(Map.water_to_light.get_dest(water))

    return lights


def get_temperatures(seeds: list) -> list:
    lights = get_lights(seeds)
    temps = []

    for light in lights:
        temps.extend(Map.light_to_temperature.get_dest(light))

    return temps


def get_humidities(seeds: list) -> list:
    temps = get_temperatures(seeds)
    hums = []

    for temp in temps:
        hums.extend(Map.temperature_to_humidity.get_dest(temp))

    return hums


def get_locations(seeds: list) -> list:
    hums = get_humidities(seeds)
    locations = []

    for hum in hums:
        locations.extend(Map.humidity_to_location.get_dest(hum))

    return locations


# Main functions
def get_solution_part1(lines: list[str]) -> int:
    '''Main function'''

    seed_info = process_input(deque(lines))

    seeds = [Item(s) for s in seed_info]

    locations = get_locations(seeds)

    return min([loc.base for loc in locations])

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str]) -> int:
    '''Main function'''

    seed_info = process_input(deque(lines))

    seeds = []

    for i in range(0,len(seed_info),2):
        seeds.append(Item(seed_info[i],seed_info[i+1]))

    locations = get_locations(seeds)

    return min([loc.base for loc in locations])


    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass