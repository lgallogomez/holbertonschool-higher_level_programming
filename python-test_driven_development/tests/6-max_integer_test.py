#!/usr/bin/python3

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-1, -3]), -1)
        self.assertEqual(max_integer([2, -1, 2]), 2)
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()