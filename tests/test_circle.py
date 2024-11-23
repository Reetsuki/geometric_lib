import unittest
import math
from circle import area, perimeter

class testcircle(unittest.TestCase):
    def test_area(self):
        radius = 4
        self.assertAlmostEqual(area(4), 50.2654825, 7)
    def test_perimeter(self):
        radius = 3
        self.assertAlmostEqual(perimeter(3), 18.8495559, 7)

if __name__ == "__main__":
    unittest.main()
