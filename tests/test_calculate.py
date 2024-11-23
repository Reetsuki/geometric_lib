import unittest
import math
from calculate import calc

class testcalculate(unittest.TestCase):
    def test_calc_circle_area_valid(self):
        fig = 'circle'
        func = 'area'
        size = [9]
        self.assertAlmostEqual(calc(fig, func, size), 254.4690049, 7)
    def test_calc_circle_perimeter_valid(self):
        fig = 'circle'
        func = 'perimeter'
        size = [4]
        self.assertAlmostEqual(calc(fig, func, size), 25.1327412, 7)
    def test_calc_square_area_valid(self):
        fig = 'square'
        func = 'area'
        size = [7]
        self.assertEqual(calc(fig, func, size), 49)
    def test_calc_square_perimeter_valid(self):
        fig = 'square'
        func = 'perimeter'
        size = [8]
        self.assertEqual(calc(fig, func, size), expect, 32)
    def test_calc_triangle_area_valid(self):
        fig = 'triangle'
        func = 'area'
        size = [8, 6, 5]
        self.assertAlmostEqual(calc(fig, func, size), 14.9812383, 7)
    def test_calc_triangle_perimeter_valid(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [6, 5, 6]
        self.assertEqual(calc(fig, func, size), 17)
    def test_calc_raises_error_for_figure_invalid(self):
        fig = 'notfig'
        func = 'area'
        size = [4]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)
    def test_calc_raises_error_for_function_invalid(self):
        fig = 'circle'
        func = 'notfunc'
        size = [3]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)
    def test_calc_raises_error_for_size_invalid(self):
        fig = 'square'
        func = 'area'
        size = [-8]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)
    def test_calc_raises_error_for_triangle_area_inequality_invalid(self):
        fig = 'triangle'
        func = 'area'
        size = [4, 5, 13]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)
    def test_calc_raises_error_for_triangle_perimeter_inequality_invalid(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [1, 8, 2]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

