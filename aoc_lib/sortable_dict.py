"""
This module contains a class SortableDict, which extends the OrderedDict class with sort
methods
"""

# Imports
from collections import OrderedDict
from operator import itemgetter
from pprint import pprint

class SortableDict(OrderedDict):

    def _sort(self, key, reverse) -> None:
        # First create a list with tuples
        dict_as_list = self._dict_to_list()
        # Then perform the sort
        dict_as_list.sort(key=key,reverse=reverse)
        # Then put the list back in dict format
        self._list_to_dict(dict_as_list)


    def sort_by_value_then_key(self, reverse=False) -> None:
        '''This function orders the dict entries by value and then by key'''

        self._sort(key=itemgetter(1,0), reverse=reverse)


    def sort_by_value(self, reverse=False) -> None:
        '''This function orders the dict entries by value and then by key'''

        self._sort(key=itemgetter(1), reverse=reverse)


    def sort_by_key(self, reverse=False) -> None:
        '''This function orders the dict entries by value and then by key'''

        self._sort(key=itemgetter(0), reverse=reverse)


    def _dict_to_list(self) -> list[tuple]:
        return [t for t in self.items()]
    

    def _list_to_dict(self, dict_as_list) -> None:
        # First empty the self object
        self.clear()

        # Then fill the dict again
        for key, value in dict_as_list:
            self[key] = value


if __name__ == '__main__':
    example_dict = {
        'a': 4,
        'd': 2,
        'c': 1,
        'b': 2,
    }

    example_sortdict = SortableDict(example_dict)

    example_sortdict.sort_by_value_then_key()

    pprint(example_sortdict)
