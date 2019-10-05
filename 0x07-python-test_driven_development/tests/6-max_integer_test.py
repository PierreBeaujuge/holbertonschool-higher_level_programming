#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """define variables and methods"""

    def test_max(self):
        """
        Test function that checks the max of the list
        """
        list_1 = [1, 2, 3, 4]
        list_6 = [4, 3, 2, 1]
        list_2 = [1, 3, 4, 2]
        list_3 = [1]
        list_4 = [-1]
        list_5 = [1.1]
        self.assertEqual(max(list_1), max_integer(list_1))
        self.assertEqual(max(list_2), max_integer(list_2))
        self.assertEqual(max(list_3), max_integer(list_3))
        self.assertEqual(max(list_4), max_integer(list_4))
        self.assertEqual(max(list_5), max_integer(list_5))
        self.assertEqual(max(list_6), max_integer(list_6))

    def test_empty(self):
        """
        Test function that passes an empty list
        """
        list_1 = []
        self.assertEqual(max_integer(list_1), None)

    def test_string(self):
        """
        Test function that passes a string and checks for
        the proper error message
        """
        list_1 = [1, "a"]
        self.assertEqual(max_integer([1, 2]), max([1, 2]))
        with self.assertRaises(TypeError):
            max_integer(list_1)

    def test_none(self):
        """
        Test function that passes None as num and checks for
        the proper error message
        """
        list_1 = [1, None]
        self.assertEqual(max_integer([1, 2]), max([1, 2]))
        with self.assertRaises(TypeError):
            max_integer(list_1)

    def test_notalist_none(self):
        """
        Test function that passes None instead of a list
        and checks for the proper error message
        """
        list_1 = None
        self.assertEqual(max_integer([1, 2]), max([1, 2]))
        with self.assertRaises(TypeError):
            max_integer(list_1)

    def test_notalist_int(self):
        """
        Test function that passes an int instead of a list
        and checks for the proper error message
        """
        list_1 = 1
        self.assertEqual(max_integer([1, 2]), max([1, 2]))
        with self.assertRaises(TypeError):
            max_integer(list_1)

    def test_notalist_char(self):
        """
        Test function that passes a char instead of a list
        """
        list_1 = "a"
        self.assertEqual(max_integer("a"), 'a')

    def test_notalist_str(self):
        """
        Test function that passes a string instead of a list
        """
        list_1 = "abc"
        self.assertEqual(max_integer("abc"), 'c')

    def test_listofstr(self):
        """
        Test function that passes a list of strings
        """
        list_1 = ["abc", "def"]
        self.assertEqual(max_integer(["abc", "def"]), 'def')

    def test_listoflists(self):
        """
        Test function that passes a list of lists
        """
        list_1 = [[1, 2], [3, 4]]
        list_2 = [[1], [3, 4]]
        list_3 = [[1, 2], [3, 4, 5]]
        list_4 = [[], [3, 4]]
        self.assertEqual(max_integer(list_1), [3, 4])
        self.assertEqual(max_integer(list_2), [3, 4])
        self.assertEqual(max_integer(list_3), [3, 4, 5])
        self.assertEqual(max_integer(list_4), [3, 4])

    def test_listofothers(self):
        """
        Test function that passes a list of others
        """
        list_1 = [(1, 2), (3, 4)]
        list_2 = [{1, 2}, {3, 4}]
        self.assertEqual(max_integer(list_1), (3, 4))
        self.assertEqual(max_integer(list_2), {1, 2})

    def test_listofothers(self):
        """
        Test function that passes a list of dicts
        and checks for the proper error message
        """
        list_1 = [{1: 1, 2: 2}, {3: 3, 4: 4}]
        self.assertEqual(max_integer([1, 2]), max([1, 2]))
        with self.assertRaises(TypeError):
            max_integer(list_1)

if __name__ == '__main__':
    unittest.main()
