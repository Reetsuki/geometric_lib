import unittest
import math
from circle import area, perimeter

class testcircle(unittest.TestCase):
    def test_area(self):
        radius = 4
        expect = 50.2654825
        self.assertAlmostEqual(area(4), expect, 7)
    def test_perimeter(self):
        radius = 3
        expect = 18.8495559
        self.assertAlmostEqual(perimeter(3), expect, 7)

if __name__ == "__main__":
    unittest.main()
