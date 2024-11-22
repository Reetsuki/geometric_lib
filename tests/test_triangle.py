import unittest
import math
from triangle import area, perimeter

class testtriangle(unittest.TestCase):
    def test_area(self):
        a = 4
        b = 5
        c = 7
        p = (a + b + c) / 2
        expect = math.sqrt(p * (p - a) * (p - b) * (p - c))
        self.assertEqual(expect, area(a, b, c))
    def test_perimeter(self):
        a = 5
        b = 8
        c = 6
        expect = a + b + c
        self.assertEqual(expect, perimeter(a, b, c))
