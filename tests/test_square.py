import unittest
from square import area, perimeter

class testsquare(unittest.TestCase):
    def test_area(self):
        side = 6
        self.assertEqual(area(6), 36)
    def test_perimeter(self):
        side = 8
        self.assertEqual(perimeter(8), 32)
