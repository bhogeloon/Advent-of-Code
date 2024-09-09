"""
Year 2018, Day 4

Problem description: See https://adventofcode.com/2018/day/4

The following classes are used:
- Event: represents an event (the puzzle input lines)
- Events: List container class of Event objects
- Guard: contains the information about a guard
- Guards: Dict container class of Guard objects
- Day: contains the information on a day for a guard, including a list
    of booleans representing each minute

Part 1: Consists of the following parts:
- Building the Events list by processing the input.
- Gathering the guards and on which Day they are active
- Building a list of minutes, per guard per day, in which it is stated wheter
    the guard is awake of asleep.
- Finding the guard which is asleep for the most minutes.
- For this guard, find the minute in which he is most asleep.
The product of these last two steps will be returned.

"""

# Imports
from pprint import pprint
import re
from datetime import datetime, timedelta, date


# Constants

ONE_HOUR = timedelta(hours=1)

# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Event():
    '''An event can be:
    - Guard starts shift
    - Guard falls asleep
    - Guard wakes up'''
    def __init__(self, line: str) -> None:
        m = re.fullmatch(r'\[(.*)\] (.*)', line)
        date_time_str = m.group(1)
        self.action = m.group(2)

        self.date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')


class Events(list[Event]):
    '''List container class of Event objects'''
    def __init__(self, lines: list[str]) -> None:
        for line in lines:
            self.append(Event(line))

        self.sort_dt()

        # if test 
        if Gv.test:
            self.print()


    def sort_dt(self) -> None:
        '''Sort the events on date_time'''
        self.sort(key=lambda event: event.date_time)


    def print(self) -> None:
        for event in self:
            print(event.date_time.isoformat(), event.action)

        print()


class Day():
    '''Represents a day within a guard. Here the information about
    being awake is stored'''
    def __init__(self) -> None:
        self.events = []


    def add_event(self, event: Event) -> None:
        self.events.append(event)


    def fill_schedule(self) -> None:
        '''Fill the awake_state schedule for this day'''
        next_event_nr = 0
        self.awake_status = []
        current_awake = True
        
        for minute in range(60):
            # If no more events
            if next_event_nr >= len(self.events):
                self.awake_status.append(current_awake)
                continue

            # If next event is in this minute
            if self.events[next_event_nr].date_time.minute == minute:
                action = self.events[next_event_nr].action
                # If event is go to sleep
                if action == 'falls asleep':
                    current_awake = False
                elif action == 'wakes up':
                    current_awake = True
                else:
                    raise RuntimeError(f"Unkown action {action}")
                
                # Go to next event
                next_event_nr += 1

            # Finally store status
            self.awake_status.append(current_awake)


    def get_minutes_asleep(self) -> int:
        '''Get the total minutes of sleep for this day'''
        total_mins = 0
        
        for awake in self.awake_status:
            if not awake:
                total_mins += 1

        if Gv.test:
            print(total_mins)

        return total_mins


class Guard():
    '''Represents a guard which holds a number of days in which he
    checks in'''
    def __init__(self, nr: int) -> None:
        self.nr = nr
        self.days = {}


    def add_day(self, day: date) -> Day:
        self.days[day] = Day()

        if Gv.test:
            print(f'Adding day {str(day)} to Guard {self.nr}')

        return self.days[day]
    

    def fill_schedule(self) -> None:
        '''Fill the awake_state schedule for each day'''
        for day in self.days.values():
            day.fill_schedule()


    def get_minutes_asleep(self) -> int:
        '''Get the total number of minutes that a guard is asleep'''
        total_mins = 0

        for day in self.days.values():
            total_mins += day.get_minutes_asleep()

        if Gv.test:
            print(f'Guard {self.nr}: total mins: {total_mins}')

        return total_mins


    def get_minute_most_asleep(self) -> int:
        '''Get the minute of the shift where the guard is most asleep'''
        result = None
        max_sleep_time = 0

        for minute in range(60):
            total_sleep_time = 0

            for day in self.days.values():
                if not day.awake_status[minute]:
                    total_sleep_time += 1

            if result == None:
                result = minute
                max_sleep_time = total_sleep_time
            elif total_sleep_time > max_sleep_time:
                result = minute
                max_sleep_time = total_sleep_time

        return result
    

class Guards(dict[Guard]):
    '''Dict Container class of Guard objects'''
    def __init__(self, events: Events) -> None:
        current_day = None

        for event in events:
            m = re.fullmatch(r'Guard #(\d+) begins shift', event.action)

            if m:
                # Determine guard nr
                guard_nr = int(m.group(1))

                # Create new guard if not yet exists
                if guard_nr not in self.keys():
                    self[guard_nr] = Guard(guard_nr)

                # Add a day to the guard and mark as current
                # Add one hour in case the check in time is before midnight
                day = (event.date_time + ONE_HOUR).date()
                current_day = self[guard_nr].add_day(day)

                if Gv.test:
                    print(f"Added day {str(day)} for guard {guard_nr}")

                continue

            # If we have another event, but no guard_day yet, raise exception
            if current_day == None:
                raise RuntimeError('No guard has yet started a shift')
            
            # Then add the event to the current day:
            current_day.add_event(event)
            

    def fill_schedule(self) -> None:
        '''Fill the awake_status schedule for each guard'''
        for guard in self.values():
            guard.fill_schedule()


    def find_laziest_guard(self) -> int:
        '''Find the guard who spends the most minutes asleep'''
        laziest_guard = None
        max_sleep_mins = 0

        for guard in self.values():
            mins_asleep = guard.get_minutes_asleep()

            if laziest_guard == None:
                laziest_guard = guard.nr
                max_sleep_mins = mins_asleep
            elif mins_asleep > max_sleep_mins:
                laziest_guard = guard.nr
                max_sleep_mins = mins_asleep

        return laziest_guard

            
# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    events = Events(lines)
    guards = Guards(events)
    guards.fill_schedule()
    laziest_guard = guards.find_laziest_guard()
    min_most_asleep = guards[laziest_guard].get_minute_most_asleep()

    return laziest_guard * min_most_asleep

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
