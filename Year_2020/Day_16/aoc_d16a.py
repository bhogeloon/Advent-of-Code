"""
Year 2020, Day 16, Part 1

Problem description: See https://adventofcode.com/2020/day/16

"""

# Imports
from posixpath import split
from pprint import pprint
from unittest import result


# Constants


# Global variables

class Gv():
    '''Class to store global variables that are immutable, so they can be
    reassigned within a function'''

# Classes

class Field():
    '''Ticket Field:
    {
        ranges: [
            {
                start,
                end,
            } 
        ]
    }
    '''

    def __init__(self, line:str) -> None:
        self.fieldname, line_rmd = line.split(': ')
        ranges_str = line_rmd.split(' or ')

        self.ranges = []
        for range_str in ranges_str:
            start_str, end_str = range_str.split('-')
            field_range = {
                'start': int(start_str),
                'end': int(end_str),
            }
            self.ranges.append(field_range)


class Fields(list[Field]):
    pass


class Ticket():
    '''Ticket. Will initially just contain a list with field_values'''

    def __init__(self, line:str) -> None:
        self.field_values = [ int(val) for val in line.split(',') ]


    def validate(self, fields: Fields) -> int:
        result = 0

        for field_value in self.field_values:
            valid_value = False
            for field in fields:
                for field_range in field.ranges:
                    if field_value in range(
                                       field_range['start'],
                                       field_range['end'] + 1,
                                       ):
                        valid_value = True
                        break

                if valid_value:
                    break

            if not valid_value:
                result += field_value

        return result


class NbTickets(list):
    def validate(self, fields: Fields):
        result = 0
        for ticket in self:
            result += ticket.validate(fields)

        return result


# Functions

def read_input(lines: list[str]) -> tuple:
    i = 0
    fields = Fields()

    while lines[i] != '':
        fields.append(Field(lines[i]))

        i += 1

    i += 2
    my_ticket = Ticket(lines[i])

    i += 3

    nb_tickets = NbTickets()
    for line in lines[i:]:
        nb_tickets.append(Ticket(line))

    return fields, my_ticket, nb_tickets


# Main function
def get_solution(lines: list[str]) -> int:
    '''Main function'''

    fields, my_ticket, nb_tickets = read_input(lines)

    return nb_tickets.validate(fields)

    return __name__


if __name__ == '__main__':
    pass