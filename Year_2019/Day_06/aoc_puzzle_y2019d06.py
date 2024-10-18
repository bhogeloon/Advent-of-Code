"""
Year 2019, Day 6

Problem description: See https://adventofcode.com/2019/day/6

The following classes are used:
- SpaceObject: An object in space, which orbits around another object.
- SpaceObjects: A dict container class of SpaceObject objects

Part 1: Register all SpaceObjects and for each input line link the first
one to the latter.
Then go through all objects and recursively count the connections back to
the one that doesn't orbit at all.

Part 2: Record the path of Santa to the origin. Then follow the path of YOU
and see where they meet.

"""

# Imports
from __future__ import annotations
from pprint import pprint


# Constants
YOU = 'YOU'
SAN = 'SAN'

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class SpaceObject:
    '''An object in space, orbitting another object'''

    # This class variable records the path that Santa needs to follow
    santa_path = []

    # This class variable records the path that YOU need to follow to meet
    # Santa
    you_path = []


    def __init__(self, name: str) -> None:
        self.name = name
        self.in_orbit_of = None


    def declare_in_orbit_of(self, other_space_object: SpaceObject):
        '''Register this SpaceObject to be in orbit of other_space_object'''
        # Raise exception if already in other orbit
        if self.in_orbit_of != None:
            msg = (
                f'{self.name} is already in orbit of {self.in_orbit_of.name}'
            )
            raise RuntimeError(msg)
        
        self.in_orbit_of = other_space_object


    def count_orbits(self, count = 0) -> int:
        '''Count the total amount of orbits for this SpaceObject'''
        if self.in_orbit_of == None:
            return count
        
        count += 1

        return self.in_orbit_of.count_orbits(count)
    

    def follow_santa(self) -> None:
        '''Record the path that SAN needs to follow to get to the start'''
        if self.in_orbit_of == None:
            return
        
        self.santa_path.append(self.in_orbit_of.name)
        self.in_orbit_of.follow_santa()


    def meet_santa(self) -> str:
        '''Follow the path of YOU until it crosses the path with Santa
        The function returns the name of the meeting point'''
        if self.name in self.santa_path:
            return self.name
        
        self.you_path.append(self.in_orbit_of.name)
        return self.in_orbit_of.meet_santa()
        

class SpaceObjects(dict[str, SpaceObject]):
    '''Dict container class of SpaceObject objects. The key is the name
    of the object'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            (target_name, in_orbit_name) = line.split(')')

            for object_name in (target_name, in_orbit_name):
                # Create if it doesn't exist
                if object_name not in self.keys():
                    self[object_name] = SpaceObject(object_name)

            self[in_orbit_name].declare_in_orbit_of(self[target_name])


    def count_orbits(self) -> int:
        '''Count the total number of orbits'''
        total_orbits = 0
        for space_object in self.values():
            total_orbits += space_object.count_orbits()

        return total_orbits
    

    def find_santa(self) -> int:
        '''Find the path between YOU and SAN and return the amount of
        orbital changes required (the part 2 answer)'''
        self[SAN].follow_santa()
        meeting_pt = self[YOU].meet_santa()
        meetin_index = SpaceObject.santa_path.index(meeting_pt)

        if Gv.test:
            pprint(SpaceObject.santa_path)
            pprint(SpaceObject.you_path)
            print(meetin_index)

        # To get the total distance, take the index number and add the
        # length of you_path. You'll have to substract one for the common
        # meeting point.
        return meetin_index + len(SpaceObject.you_path) - 1


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    space_objects = SpaceObjects(lines)

    return space_objects.count_orbits()

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    space_objects = SpaceObjects(lines)

    return space_objects.find_santa()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
