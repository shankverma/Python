import unittest
from search.sort import sort_search_algorithms
from search.jsonSerializer import json_serializer, json_deserializer
from search.regex import find_pattern

class TestSortSearchAlgorithms(unittest.TestCase):

    def setUp(self):
        self.lst1 = [10, 23, 45, 70, 11]
        self.key = 45
        self.sort1 = sort_search_algorithms(self.lst1, self.key)

    def test_linear_search(self):
        result = self.sort1.linear_search()
        self.assertEqual(result, 2, "Should be 2")

    def test_search_rotated_array(self):
        result = self.sort1.search_rotated_array()
        self.assertEqual(result, 2, "Should be 2")

    def test_bubble_sort(self):
        sorted_list = self.sort1.bubble_sort()
        self.assertEqual(sorted_list, [10, 11, 23, 45, 70], "Should be [10, 11, 23, 45, 70]")

    def test_bubble_sort_2(self):
        sorted_list2 = self.sort1.bubble_sort_2()
        self.assertEqual(sorted_list2, [10, 11, 23, 45, 70], "Should be [10, 11, 23, 45, 70]")

    def test_selection_sort(self):
        sorted_list3 = self.sort1.selection_sort()
        self.assertEqual(sorted_list3, [10, 11, 23, 45, 70], "Should be [10, 11, 23, 45, 70]")

    def test_insertion_sort(self):
        sorted_list4 = self.sort1.insertion_sort()
        self.assertEqual(sorted_list4, [10, 11, 23, 45, 70], "Should be [10, 11, 23, 45, 70]")

class TestJsonSerializer(unittest.TestCase):

    def setUp(self):
        self.dict = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }

    def test_json_serializer(self):
        json_str = json_serializer(self.dict)
        self.assertIsInstance(json_str, str, "Should be a string")

    def test_json_deserializer(self):
        json_str = json_serializer(self.dict)
        dict_deserialized = json_deserializer(json_str)
        self.assertIsInstance(dict_deserialized, dict, "Should be a dictionary")
        self.assertEqual(dict_deserialized, self.dict, "Should be equal to the original dictionary")

class TestRegex(unittest.TestCase):

    def test_find_pattern(self):
        result = find_pattern("This is a test string", "test")
        self.assertTrue(result, "Pattern should be found")

if __name__ == '__main__':
    unittest.main()
