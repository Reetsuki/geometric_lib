import unittest
import math
from circle import area, perimeter

class testcircle(unittest.TestCase):
    def test_area(self):
        radius = 4
        expect = math.pi * radius * radius
        self.assertEqual(area(4), expect)
    def test_perimeter(self):
        radius = 3
        expect = 2 * math.pi * radius
        self.assertEqual(perimeter(3), expect)
