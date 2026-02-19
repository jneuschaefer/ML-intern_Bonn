
import sys
import os

import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from algebra import add

class AdditionTestCase(unittest.TestCase):
    def test_simple_int(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 1), 3)
        self.assertEqual(add(0, 12), 12)
        self.assertEqual(add(12, 0), 12)
        
    def test_negative_int(self):
        self.assertEqual(add(5, -2), 3)
        self.assertEqual(add(-5, 2), -3)
        self.assertEqual(add(-5, -2), -7)

if __name__ == '__main__':
    unittest.main()