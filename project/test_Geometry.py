import unittest



import unittest

def triangle_area(base, height):
    return 0.5 * base * height

class TestGeneratedFunction(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(triangle_area(10, 5), 25)
        self.assertEqual(triangle_area(8, 2), 8)
        self.assertEqual(triangle_area(0, 10), 0)
        self.assertEqual(triangle_area(10, 0), 0)

    def test_negative_inputs(self):
        self.assertEqual(triangle_area(-10, 5), -25)
        self.assertEqual(triangle_area(10, -5), -25)
        self.assertEqual(triangle_area(-10, -5), 25)

    def test_non_numeric_inputs(self):
        with self.assertRaises(TypeError):
            triangle_area("10", 5)
        with self.assertRaises(TypeError):
            triangle_area(10, "5")
        with self.assertRaises(TypeError):
            triangle_area([10], 5)
        with self.assertRaises(TypeError):
            triangle_area(10, {5})
        with self.assertRaises(TypeError):
            triangle_area(None, 5)

if __name__ == '__main__':
    unittest.main()


import unittest

class TestGeneratedFunction(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(trapezoid_area(5, 7, 10), 60)
        self.assertEqual(trapezoid_area(0, 0, 10), 0)
        self.assertEqual(trapezoid_area(3, 3, 4), 12)
        self.assertEqual(trapezoid_area(1.5, 2.5, 3), 6)
        self.assertEqual(trapezoid_area(8, 12, 0), 0)

    def test_negative_inputs(self):
        self.assertEqual(trapezoid_area(-3, 5, 6), 6)
        self.assertEqual(trapezoid_area(4, -2, 5), 5)
        self.assertEqual(trapezoid_area(-4, -6, 7), -35)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            trapezoid_area("5", 7, 10)
        with self.assertRaises(TypeError):
            trapezoid_area(5, [7], 10)
        with self.assertRaises(TypeError):
            trapezoid_area(5, 7, None)
        with self.assertRaises(TypeError):
            trapezoid_area(5, 7, "height")
        with self.assertRaises(TypeError):
            trapezoid_area(5, 7)


class TestCalculate_circumference(unittest.TestCase):
    def test_calculate_circumference_valid_radius():
        result = Geometry.calculate_circumference(5)
        assert result == 31.41592653589793  # Assuming π = 3.141592653589793
    def test_calculate_circumference_zero_radius():
        result = Geometry.calculate_circumference(0)
        assert result == 0
    def test_calculate_circumference_negative_radius():
        try:
            Geometry.calculate_circumference(-5)
            assert False, "Expected ValueError for negative radius"
        except ValueError:
            pass
    def test_calculate_circumference_non_numeric_radius_string():
        try:
            Geometry.calculate_circumference("abc")
            assert False, "Expected TypeError for non-numeric radius"
        except TypeError:
            pass
    def test_calculate_circumference_non_numeric_radius_none():
        try:
            Geometry.calculate_circumference(None)
            assert False, "Expected TypeError for None as radius"
        except TypeError:
            pass
    def test_calculate_circumference_large_radius():
        result = Geometry.calculate_circumference(1e6)
        assert result == 6283185.307179586  # Assuming π = 3.141592653589793
    def test_calculate_circumference_float_radius():
        result = Geometry.calculate_circumference(2.5)
        assert result == 15.707963267948966  # Assuming π = 3.141592653589793

if __name__ == '__main__':
    unittest.main()


class TestHalf_circle_circumference(unittest.TestCase):
    def test_half_circle_circumference_valid_radius():
        result = Geometry.half_circle_circumference(10)
        expected = 10 * 3.14159 + 20  # πr + 2r
        assert result == expected
    def test_half_circle_circumference_zero_radius():
        result = Geometry.half_circle_circumference(0)
        expected = 0  # πr + 2r where r=0
        assert result == expected
    def test_half_circle_circumference_negative_radius():
        try:
            Geometry.half_circle_circumference(-5)
            assert False, "Expected ValueError for negative radius"
        except ValueError:
            pass
    def test_half_circle_circumference_non_numeric_radius():
        try:
            Geometry.half_circle_circumference("ten")
            assert False, "Expected TypeError for non-numeric radius"
        except TypeError:
            pass
    def test_half_circle_circumference_large_radius():
        result = Geometry.half_circle_circumference(1e6)
        expected = 1e6 * 3.14159 + 2 * 1e6  # πr + 2r
        assert result == expected

if __name__ == '__main__':
    unittest.main()


class TestHalf_circle_circumference(unittest.TestCase):
    def test_half_circle_circumference_valid_radius():
        result = Geometry.half_circle_circumference(10)
        expected = 10 * 3.141592653589793 + 20  # π * r + 2r
        assert result == expected
    def test_half_circle_circumference_zero_radius():
        result = Geometry.half_circle_circumference(0)
        expected = 0
        assert result == expected
    def test_half_circle_circumference_negative_radius():
        try:
            Geometry.half_circle_circumference(-5)
            assert False, "Expected ValueError for negative radius"
        except ValueError:
            pass
    def test_half_circle_circumference_non_numeric_radius():
        try:
            Geometry.half_circle_circumference("ten")
            assert False, "Expected TypeError for non-numeric radius"
        except TypeError:
            pass
    def test_half_circle_circumference_large_radius():
        result = Geometry.half_circle_circumference(1e6)
        expected = 1e6 * 3.141592653589793 + 2 * 1e6  # π * r + 2r
        assert result == expected
    def test_half_circle_circumference_float_radius():
        result = Geometry.half_circle_circumference(7.5)
        expected = 7.5 * 3.141592653589793 + 15  # π * r + 2r
        assert result == expected

if __name__ == '__main__':
    unittest.main()
