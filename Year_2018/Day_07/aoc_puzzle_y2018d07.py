"""
Year 2018, Day 7

Problem description: See https://adventofcode.com/2018/day/7

The following classes are used:
- Step: A step to be performed.
- Sleigh: Dict container class of Step objects.
- Worker (part 2): A worker which is working on a job (or not)
- Workers: List container class of Worker objects.

Part 1: Determine all the Parents and Childs of each step. Then start by
finding all steps that have no parents. They are put in a list of steps
ready to be performed. Then each time select the smallest step_id in the list.
Once a step is performed, check for each child whether it is ready to be
performed (i.e. all parents are done) and if so include that in the list of 
steps ready to be done. Repeat this procedure until the list of steps ready
to be done is empty.

Part 2: Create 5 workers under the Sleigh object. Create a set with all step
ids which are not yet completed.
So now we itterate over a loop, increasing the seconds, in which we look each
time at the jobs which can be picked up and try to assign those to available
workers. Also within the loop we decrease the TTL value of each active step.
If it reaches 0, complete it and check if the childs can be picked up (in the 
same way as in part 1). We repeat this until the set with uncompleted jobs
is empty.
 
"""

# Imports
from __future__ import annotations
from pprint import pprint
import re


# Constants

NR_OF_WORKERS = 5
NR_OF_WORKERS_TEST = 2

TTL_DELAY = 60
TTL_DELAY_TEST = 0


# Global variables

class Gv():
    '''Class to store global variables'''

    # Variable that can be used to indicate we're using the test input
    test = False


# Classes

class Worker:
    '''Each worker can pick up a job'''
    def __init__(self) -> None:
        self.job = None


class Workers(list[Worker]):
    '''A list container class of Worker objects'''
    def __init__(self, nr: int) -> None:
        for i in range(nr):
            self.append(Worker())


class Step:
    '''A step to assemble the sleigh. This has an id, a list of parents and a 
    list of childs and a done boolean field'''

    def __init__(self, id: str) -> None:
        self.id = id
        self.parents = []
        self.childs = []
        self.done = False

        if Gv.test:
            self.ttl = TTL_DELAY_TEST + ord(id) - ord('A') + 1
        else:
            self.ttl = TTL_DELAY + ord(id) - ord('A') + 1


    def perform(self) -> list:
        '''Perform the step and return a list of child ids which are not yet
        ready'''
        self.done = True
        new_steps_ready = []

        for child in self.childs:
            if not child.done and child.is_ready_tbp():
                new_steps_ready.append(child.id)

        return new_steps_ready
    

    def is_ready_tbp(self) -> bool:
        '''Checks if the step is ready to be performed, i.e. all parents are 
        done'''
        for parent in self.parents:
            if not parent.done:
                return False
            
        return True


class Sleigh(dict[str, Step]):
    '''A dict container class of Step objects with Step id as key. Furthermore
    it contains a list of Step ids ready to be done and a step_order str 
    attribute to keep track of the order of steps'''

    def __init__(self, lines: list[str]) -> None:
        self.not_completed = set()

        for line in lines:
            pattern = r'Step ([A-Z]) must be finished '
            pattern += r'before step ([A-Z]) can begin\.'
            m = re.fullmatch(pattern, line)
            parent_id = m.group(1)
            child_id = m.group(2)

            # Create objects if they don't yet exists
            for id in [parent_id, child_id]:
                if id not in self.keys():
                    self[id] = Step(id)

            # Set relations
            self[child_id].parents.append(self[parent_id])
            self[parent_id].childs.append(self[child_id])

            # Mark as not completed
            self.not_completed.add(parent_id)
            self.not_completed.add(child_id)

        # This will contain the order of steps
        self.order = ''
        self.find_starting_steps()

        if Gv.test:
            self.nr_workers = NR_OF_WORKERS_TEST
        else:
            self.nr_workers = NR_OF_WORKERS

        self.workers = Workers(self.nr_workers)
        self.available_workers = self.nr_workers


    def find_starting_steps(self) -> None:
        '''Register the steps that have no parents in the ready_tbd list'''
        self.ready_tbd = []

        for step in self.values():
            if len(step.parents) == 0:
                self.ready_tbd.append(step.id)


    def perform_steps(self) -> None:
        '''Perform all steps in the right order'''
        # until there are no more steps to be done
        while len(self.ready_tbd) > 0:
            # Order the ready_tbd list in reverse order
            self.ready_tbd.sort(reverse=True)
            # select next step
            next_step = self[self.ready_tbd.pop()]
            # perform the step and put the childs in ready_tbd
            self.ready_tbd.extend(next_step.perform())
            # Register the step that has been done
            self.order += next_step.id


    def get_time_to_complete(self) -> int:
        '''Calculate the amount of seconds to complete all steps (part 2)'''
        time_passed = -1
        
        while len(self.not_completed) > 0:
            # Increase time
            time_passed += 1

            # Decrease TTL for all active workers
            for worker in self.workers:
                # Skip if not active
                if worker.job == None:
                    continue

                worker.job.ttl -= 1

                # If job is done
                if worker.job.ttl == 0:
                    # perform the step and put the childs in ready_tbd
                    self.ready_tbd.extend(worker.job.perform())

                    # Remove from not_completed set
                    self.not_completed.remove(worker.job.id)
                    # Increase available workers
                    self.available_workers += 1
                    # Release job
                    worker.job = None

            # If no worker available, go to next cycle
            if self.available_workers == 0:
                continue

            # If no jobs ready to pick up, also continue
            if len(self.ready_tbd) == 0:
                continue

            # Now assign the jobs
            # Order the ready_tbd list in reverse order
            self.ready_tbd.sort(reverse=True)

            # Go through the list of workers
            for worker in self.workers:
                # If no more jobs to pick up, break out
                if len(self.ready_tbd) == 0:
                    break

                # If worker busy, go to the next one
                if worker.job != None:
                    continue

                # Assign worker to next step
                next_step = self[self.ready_tbd.pop()]
                worker.job = next_step

                # Decrease available workers
                self.available_workers -= 1

        return time_passed


# Functions


# Main functions
def get_solution_part1(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 1 solution'''

    Gv.test = kwargs.get('test', False)

    sleigh = Sleigh(lines)
    sleigh.perform_steps()

    return sleigh.order

    return 'part_1 ' + __name__


def get_solution_part2(lines: list[str], *args, **kwargs) -> int:
    '''Main function for the part 2 solution'''

    Gv.test = kwargs.get('test', False)

    sleigh = Sleigh(lines)

    return sleigh.get_time_to_complete()

    return 'part_2 ' + __name__


if __name__ == '__main__':
    pass
