"""
Test modudule to test the functions in the lib.sortable_dict module
"""

import unittest
from aoc_lib.sortable_dict import SortableDict
import json

# Test data

test_data_sort_by_value_then_key_json = """
[
    {
        "in": {
            "a": 4,
            "d": 2,
            "c": 1,
            "b": 2
        },
        "out": {
            "c": 1,
            "b": 2,
            "d": 2,
            "a": 4
        }
    }
]
"""
test_data_sort_by_value_then_key = json.loads(test_data_sort_by_value_then_key_json)

class SortableDictTest(unittest.TestCase):
    def test_sort_by_value_then_key(self):
        for test_data in test_data_sort_by_value_then_key:
            sortdict = SortableDict(test_data["in"])
            sortdict.sort_by_value_then_key()
            self.assertEqual(sortdict,SortableDict(test_data["out"]))


if __name__ == "__main__":
    unittest.main()
