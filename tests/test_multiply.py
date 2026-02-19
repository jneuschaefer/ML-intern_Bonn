
import sys
import os

import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from algebra import multiply

class AdditionTestCase(unittest.TestCase):
    def test_simple_int(self):
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(2, 1), 2)
        self.assertEqual(multiply(0, 12), 0)
        self.assertEqual(multiply(12, 0), 0)
        
    def test_negative_int(self):
        self.assertEqual(multiply(5, -2), -10)
        self.assertEqual(multiply(-5, 2), -10)
        self.assertEqual(multiply(-5, -2), 10)

if __name__ == '__main__':
    unittest.main()