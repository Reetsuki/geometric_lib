import unittest
import math
from calculate import calc

class testcalculate(unittest.TestCase):
    def test_calc_circle_area_valid(self):
        fig = 'circle'
        func = 'area'
        size = [9]
        expect = math.pi * 9 * 9
        self.assertEqual(calc(fig, func, size), expect)
    def test_calc_circle_perimeter_valid(self):
        fig = 'circle'
        func = 'perimeter'
        size = [4]
        expect = 2 * math.pi * 4
        self.assertEqual(calc(fig, func, size), expect)
    def test_calc_square_area_valid(self):
        fig = 'square'
        func = 'area'
        size = [7]
        expect = 7 * 7
        self.assertEqual(calc(fig, func, size), expect)
    def test_calc_square_perimeter_valid(self):
        fig = 'square'
        func = 'perimeter'
        size = [8]
        expect = 4 * 8
        self.assertEqual(calc(fig, func, size), expect)
    def test_calc_triangle_area_valid(self):
        fig = 'triangle'
        func = 'area'
        size = [8, 6, 5]
        p = (8 + 6 + 5) / 2
        expect = math.sqrt(p * (p - 8) * (p - 6) * (p - 5))
        self.assertEqual(calc(fig, func, size), expect)
    def test_calc_triangle_perimeter_valid(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [6, 5, 6]
        expect = 6 + 5 + 6
        self.assertEqual(calc(fig, func, size), expect)
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

