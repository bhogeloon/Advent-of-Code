"""
Test modudule to test the functions in the lib.sortable_dict module
"""

import unittest
from aoc_lib.sortable_dict import SortableDict

# Test data

test_data_normal_json = """
[
    {
        'in': {
            'a': 4,
            'd': 2,
            'c': 1,
            'b': 2,
        }
        'out': {
            'c': 1,
            'b': 2,
            'd': 2,
            'a': 4,
        }
    }
]
"""

class SortableDictTest(unittest.TestCase):
    def test_test(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
