from unittest import TestCase
from decodejson import get_specified_attributes

class TestGet_specified_attributes(TestCase):
    def test_get_specified_attributes(self):
        filepath = "test.json"  # json file path
        find_str = "april"  # in the json file, it will search the attributes which the name contains 'april'.
        return_list = get_specified_attributes(filepath, find_str)
        self.assertEqual(return_list, [1, 2, 6, 7, 8])
