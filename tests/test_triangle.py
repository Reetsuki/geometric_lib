import unittest
from math import sqrt as sqrt
from triangle import area, perimeter

class testtriangle(unittest.TestCase):
    def test_area(self):
        a = 4
        b = 5
        c = 7
        self.assertAlmostEqual(area(a, b, c), 9.797959, 7)
    def test_perimeter(self):
        a = 5
        b = 8
        c = 6
        self.assertEqual(expect, perimeter(a, b, c), 19)
