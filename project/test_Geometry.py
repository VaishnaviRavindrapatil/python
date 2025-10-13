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


class TestCalculate_square_area_and_perimeter(unittest.TestCase):
    def test_calculate_square_area_and_perimeter_valid_side_length():
        result = Geometry.calculate_square_area_and_perimeter(4)
        assert result == (16, 16)
    def test_calculate_square_area_and_perimeter_side_length_zero():
        result = Geometry.calculate_square_area_and_perimeter(0)
        assert result == (0, 0)
    def test_calculate_square_area_and_perimeter_negative_side_length():
        try:
            Geometry.calculate_square_area_and_perimeter(-5)
            assert False, "Expected ValueError for negative side length"
        except ValueError as e:
            assert str(e) == "Side length must be non-negative"
    def test_calculate_square_area_and_perimeter_non_numeric_side_length():
        try:
            Geometry.calculate_square_area_and_perimeter("abc")
            assert False, "Expected TypeError for non-numeric side length"
        except TypeError as e:
            assert str(e) == "Side length must be a number"
    def test_calculate_square_area_and_perimeter_large_side_length():
        result = Geometry.calculate_square_area_and_perimeter(1_000_000)
        assert result == (1_000_000_000_000, 4_000_000)

if __name__ == '__main__':
    unittest.main()


class TestCalculate_perimeter(unittest.TestCase):
    def test_calculate_perimeter_valid_rectangle():
        result = calculate_perimeter("rectangle", length=5, width=3)
        assert result == 16, f"Expected 16, got {result}"
    def test_calculate_perimeter_valid_square():
        result = calculate_perimeter("square", side=4)
        assert result == 16, f"Expected 16, got {result}"
    def test_calculate_perimeter_valid_triangle():
        result = calculate_perimeter("triangle", side1=3, side2=4, side3=5)
        assert result == 12, f"Expected 12, got {result}"
    def test_calculate_perimeter_invalid_shape_type():
        try:
            calculate_perimeter("circle", radius=7)
        except ValueError as e:
            assert str(e) == "Unsupported shape type", f"Unexpected error message: {str(e)}"
        else:
            assert False, "Expected ValueError for unsupported shape type"
    def test_calculate_perimeter_missing_arguments_rectangle():
        try:
            calculate_perimeter("rectangle", length=5)
        except TypeError as e:
            assert str(e) == "Missing required arguments for rectangle", f"Unexpected error message: {str(e)}"
        else:
            assert False, "Expected TypeError for missing arguments"
    def test_calculate_perimeter_missing_arguments_square():
        try:
            calculate_perimeter("square")
        except TypeError as e:
            assert str(e) == "Missing required arguments for square", f"Unexpected error message: {str(e)}"
        else:
            assert False, "Expected TypeError for missing arguments"
    def test_calculate_perimeter_missing_arguments_triangle():
        try:
            calculate_perimeter("triangle", side1=3, side2=4)
        except TypeError as e:
            assert str(e) == "Missing required arguments for triangle", f"Unexpected error message: {str(e)}"
        else:
            assert False, "Expected TypeError for missing arguments"
    def test_calculate_perimeter_negative_values():
        try:
            calculate_perimeter("rectangle", length=-5, width=3)
        except ValueError as e:
            assert str(e) == "Length and width must be positive values", f"Unexpected error message: {str(e)}"
        else:
            assert False, "Expected ValueError for negative values"
    def test_calculate_perimeter_non_numeric_values():
        try:
            calculate_perimeter("square", side="four")
        except TypeError as e:
            assert str(e) == "Side must be a numeric value", f"Unexpected error message: {str(e)}"
        else:
            assert False, "Expected TypeError for non-numeric values"
    def test_calculate_perimeter_zero_values():
        try:
            calculate_perimeter("triangle", side1=0, side2=4, side3=5)
        except ValueError as e:
            assert str(e) == "Side lengths must be greater than zero", f"Unexpected error message: {str(e)}"
        else:
            assert False, "Expected ValueError for zero values"

if __name__ == '__main__':
    unittest.main()
