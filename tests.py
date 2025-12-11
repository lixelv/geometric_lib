import unittest

import numpy as np
import numpy.testing as npt

import circle as c
import rectangle as r
import square as s
import triangle as t

circle_test_cases = (
    (5, 78.53981633974483, 31.41592653589793),
    (-3, 28.274333882308138, -18.84955592153876),
    (12, 452.3893421169302, 75.39822368615503),
    (0, 0.0, 0.0),
    (693, 1508746.7302938444, 4354.247417875453),
    (-2234, 15678922.38545918, -14036.635976239195),
    (
        (2 + 4j),
        (-37.69911184307752 + 50.26548245743669j),
        (12.566370614359172 + 25.132741228718345j),
    ),
    (
        (-5 - 43j),
        (-5730.265000147782 + 1350.884841043611j),
        (-31.41592653589793 - 270.1769682087222j),
    ),
    (
        np.array([[1, 2], [-4, 3]]),
        [[3.14159265, 12.56637061], [50.26548246, 28.27433388]],
        [[6.28318531, 12.56637061], [-25.13274123, 18.84955592]],
    ),
    (
        np.array([[1, 2, -5], [-4, 3, 2], [0, 3, -1]]),
        np.array(
            [
                [3.14159265, 12.56637061, 78.53981634],
                [50.26548246, 28.27433388, 12.56637061],
                [0.0, 28.27433388, 3.14159265],
            ]
        ),
        np.array(
            [
                [6.28318531, 12.56637061, -31.41592654],
                [-25.13274123, 18.84955592, 12.56637061],
                [0.0, 18.84955592, -6.28318531],
            ]
        ),
    ),
)


rectangle_test_cases = (
    ((5, 10), 50, 30),
    ((3, 5), 15, 16),
    ((4.322, 6.123), 26.463606000000002, 20.89),
    ((1.75775, -2.001), -3.5172577499999997, -0.48649999999999993),
    ((1024.537, -204), -209005.548, 1641.074),
    (
        ((-43992.54 + 288j), (-5730.26 + 1350j)),
        (251699892.26040003 - 61040243.88j),
        (-99445.6 + 3276j),
    ),
    (((-9938.149 + 153j), 54), (-536660.046 + 8262j), (-19768.298 + 306j)),
    (
        (np.array([[1, 2], [-4, 3]]), np.array([[3.1415, 12.442], [50.265, 28.27]])),
        np.array([[3.1415, 24.884], [-201.06, 84.81]]),
        np.array([[8.283, 28.884], [92.53, 62.54]]),
    ),
    (
        (np.array([[1, 2], [-4, 3]]), 52),
        np.array([[52, 104], [-208, 156]]),
        np.array([[106, 108], [96, 110]]),
    ),
    (
        (53, np.array([[1, 2], [-4, 3]])),
        np.array([[53, 106], [-212, 159]]),
        np.array([[108, 110], [98, 112]]),
    ),
)

square_test_cases = (
    (5, 25, 20),
    (3, 9, 12),
    (0, 0, 0),
    (-10, 100, -40),
    (23, 529, 92),
    (52, 2704, 208),
    ((59 + 100j), (-6519 + 11800j), (236 + 400j)),
    (
        np.array([[1, 2], [-4, 3]]),
        np.array([[1, 4], [16, 9]]),
        np.array([[4, 8], [-16, 12]]),
    ),
    (
        np.array([[6, 0, 0], [1, 0, 0], [-4, 3, 2]]),
        np.array([[36, 0, 0], [1, 0, 0], [16, 9, 4]]),
        np.array([[24, 0, 0], [4, 0, 0], [-16, 12, 8]]),
    ),
    (
        np.array([[1.38, 2.11], [-4.2, 3.54]]),
        np.array([[1.9044, 4.4521], [17.64, 12.5316]]),
        np.array([[5.52, 8.44], [-16.8, 14.16]]),
    ),
)

triangle_test_cases = (
    ((5, 10, 12), 25.0, 27),
    ((3, 5, 8), 7.5, 16),
    ((4.322, 6.123, 8.54), 13.231803000000001, 18.985),
    ((1.75775, -2.001, 8.23), -1.7586288749999999, 7.986750000000001),
    ((1024.537, -204, 1024.537), -104502.774, 1845.074),
    (
        ((-43992.54 + 288j), (-5730.26 + 1350j), (-97.22 + 30j)),
        (125849946.13020001 - 30520121.94j),
        (-49820.020000000004 + 1668j),
    ),
    (
        ((-9938.149 + 153j), 54, (40.26 + 153j)),
        (-268330.023 + 4131j),
        (-9843.889 + 306j),
    ),
    (
        (np.array([[1, 2], [-4, 3]]), np.array([[3.1415, 12.442], [50.265, 28.27]]), 2),
        np.array([[1.57075, 12.442], [-100.53, 42.405]]),
        np.array([[6.1415, 16.442], [48.265, 33.27]]),
    ),
    (
        (np.array([[1, 2], [-4, 3]]), 52, 11),
        np.array([[26.0, 52.0], [-104.0, 78.0]]),
        np.array([[64, 65], [59, 66]]),
    ),
    (
        (53, np.array([[1, 2], [-4, 3]]), -0.5),
        np.array([[26.5, 53.0], [-106.0, 79.5]]),
        np.array([[53.5, 54.5], [48.5, 55.5]]),
    ),
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
