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
