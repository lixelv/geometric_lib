import unittest

import numpy as np
import numpy.testing as npt

import circle as c
import rectangle as r
import square as s
import triangle as t

circle_test_cases = (
    (5, 78.53981633974483, 31.41592653589793),
    (12, 452.3893421169302, 75.39822368615503),
    (0, 0.0, 0.0),
    (693, 1508746.7302938444, 4354.247417875453),
)


rectangle_test_cases = (
    ((5, 10), 50, 30),
    ((3, 5), 15, 16),
    ((4.322, 6.123), 26.463606000000002, 20.89),
)

square_test_cases = (
    (5, 25, 20),
    (3, 9, 12),
    (0, 0, 0),
    (23, 529, 92),
    (52, 2704, 208),
)

triangle_test_cases = (
    ((5, 10, 12), 25.0, 27),
    ((3, 5, 8), 7.5, 16),
    ((4.322, 6.123, 8.54), 13.231803000000001, 18.985),
)


class CircleTest(unittest.TestCase):
    def test_area(self):
        for radius, expected_area, _ in circle_test_cases:
            result = c.area(radius)

            if isinstance(result, np.ndarray):
                npt.assert_allclose(result, expected_area)
            else:
                self.assertEqual(result, expected_area)

    def test_perimeter(self):
        for radius, _, expected_perimeter in circle_test_cases:
            result = c.perimeter(radius)

            if isinstance(result, np.ndarray):
                npt.assert_allclose(result, expected_perimeter)
            else:
                self.assertEqual(result, expected_perimeter)


class RectangleTest(unittest.TestCase):
    def test_area(self):
        for sides, expected_area, _ in rectangle_test_cases:
            result = r.area(*sides)

            if isinstance(result, np.ndarray):
                npt.assert_allclose(result, expected_area)
            else:
                self.assertEqual(result, expected_area)

    def test_perimeter(self):
        for sides, _, expected_perimeter in rectangle_test_cases:
            result = r.perimeter(*sides)

            if isinstance(result, np.ndarray):
                npt.assert_allclose(result, expected_perimeter)
            else:
                self.assertEqual(result, expected_perimeter)


class SquareTest(unittest.TestCase):
    def test_area(self):
        for side, expected_area, _ in square_test_cases:
            result = s.area(side)

            if isinstance(result, np.ndarray):
                npt.assert_allclose(result, expected_area)
            else:
                self.assertEqual(result, expected_area)

    def test_perimeter(self):
        for side, _, expected_perimeter in square_test_cases:
            result = s.perimeter(side)

            if isinstance(result, np.ndarray):
                npt.assert_allclose(result, expected_perimeter)
            else:
                self.assertEqual(result, expected_perimeter)


class TriangleTest(unittest.TestCase):
    def test_area(self):
        for side_and_h, expected_area, _ in triangle_test_cases:
            result = t.area(side_and_h[0], side_and_h[1])

            if isinstance(result, np.ndarray):
                npt.assert_allclose(result, expected_area)
            else:
                self.assertEqual(result, expected_area)

    def test_perimeter(self):
        for sides, _, expected_perimeter in triangle_test_cases:
            result = t.perimeter(*sides)

            if isinstance(result, np.ndarray):
                npt.assert_allclose(result, expected_perimeter)
            else:
                self.assertEqual(result, expected_perimeter)
