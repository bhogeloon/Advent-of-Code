"""
Year 2020, Day 16, Part 1

Problem description: See https://adventofcode.com/2020/day/16

"""

# Imports
from pprint import pprint
from time import sleep


# Constants

SEARCH_STRING = 'departure'
# SEARCH_STRING = 'test'


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


    def init_candidates(self, nr: int) -> None:
        self.candidates = [ i for i in range(nr) ]


class Fields(list[Field]):
    def init_candidates(self, nr: int) -> None:
        self.numbers_checked = []

        for field in self:
            field.init_candidates(nr)


    def all_clear(self) -> bool:
        for field in self:
            # if SEARCH_STRING in field.fieldname:
            if len(field.candidates) == 0:
                raise RuntimeError("No more candidates for {}".format(
                    field.fieldname
                ))
            elif len(field.candidates) > 1:
                return False

        return True


    def clean_up(self) -> None:
        nr = -1

        for field in self:
            if len(field.candidates) == 1:
                if field.candidates[0] not in self.numbers_checked:
                    nr = field.candidates[0]

        if nr == -1:
            for field in self:

                for candidate in field.candidates:
                    this_cand_found = False
                    for other_field in self:
                        if field == other_field:
                            continue
                        if candidate in other_field.candidates:
                            this_cand_found = True
                            break

                    if not this_cand_found:
                        nr = candidate
                        field.candidates = [ nr ]
                        break

                if nr > -1:
                    break

        if nr == -1:
            raise RuntimeError("No unique number found")

        for field in self:
            if len(field.candidates) > 1 and nr in field.candidates:
                field.candidates.remove(nr)

        self.numbers_checked.append(nr)


class Ticket():
    '''Ticket. Will initially just contain a list with field_values'''

    def __init__(self, line:str) -> None:
        self.field_values = [ int(val) for val in line.split(',') ]


    def validate(self, fields: Fields) -> bool:
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
                return False

        return True


    def check_candidates(self, fields: Fields) -> None:
        for (nr, field_value) in enumerate(self.field_values):
            for field in fields:
                in_range = False
                for field_range in field.ranges:
                    if field_value in range(
                                       field_range['start'],
                                       field_range['end'] + 1,
                                       ):
                        in_range = True
                        break

                if not in_range and nr in field.candidates:
                    field.candidates.remove(nr)
                    '''
                    if nr == 13 and SEARCH_STRING in field.fieldname:
                        print('{}: Number 13 removed for ticket:\n{}'.format(
                            field.fieldname,
                            self.field_values,
                        ))
                    '''

    def calc_values(self, fields: Fields) -> int:
        result = 1

        for field in fields:
            if SEARCH_STRING not in field.fieldname:
                continue

            result *= self.field_values[field.candidates[0]]

        return result


class NbTickets(list[Ticket]):
    def check_candidates(self, fields:Fields) -> None:
        for ticket in self:
            if ticket.validate(fields):
                ticket.check_candidates(fields)


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

    fields.init_candidates(len(my_ticket.field_values))

    nb_tickets.check_candidates(fields)

    print()
    for field in fields:
        print(field.fieldname, field.candidates)
    sleep(3)

    while not fields.all_clear():
        fields.clean_up()

        print()
        for field in fields:
            print(field.fieldname, field.candidates)
        sleep(3)

    return my_ticket.calc_values(fields)

    '''
    fin_res = 1
    fin_res *= my_ticket.field_values[13]
    fin_res *= my_ticket.field_values[14]
    fin_res *= my_ticket.field_values[15]
    fin_res *= my_ticket.field_values[1]
    fin_res *= my_ticket.field_values[4]
    fin_res *= my_ticket.field_values[17]

    return fin_res
    '''

    return __name__


if __name__ == '__main__':
    pass