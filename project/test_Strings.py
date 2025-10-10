import unittest



import unittest

def contains_only_digits(s):
    return s.isdigit()

class TestGeneratedFunction(unittest.TestCase):
    def test_only_digits(self):
        self.assertTrue(contains_only_digits("1234567890"))
        self.assertTrue(contains_only_digits("0"))
        self.assertTrue(contains_only_digits("987654321"))

    def test_empty_string(self):
        self.assertFalse(contains_only_digits(""))

    def test_contains_letters(self):
        self.assertFalse(contains_only_digits("abc123"))
        self.assertFalse(contains_only_digits("123abc"))
        self.assertFalse(contains_only_digits("a1b2c3"))

    def test_contains_special_characters(self):
        self.assertFalse(contains_only_digits("123!@#"))
        self.assertFalse(contains_only_digits("!@#"))
        self.assertFalse(contains_only_digits("123 456"))

    def test_contains_whitespace(self):
        self.assertFalse(contains_only_digits("123 "))
        self.assertFalse(contains_only_digits(" 123"))
        self.assertFalse(contains_only_digits("12 34"))

    def test_mixed_input(self):
        self.assertFalse(contains_only_digits("123.456"))
        self.assertFalse(contains_only_digits("123,456"))
        self.assertFalse(contains_only_digits("123-456"))

if __name__ == "__main__":
    unittest.main()


import unittest

def is_palindrome(s):
    return s == s[::-1]

class TestGeneratedFunction(unittest.TestCase):
    def test_palindrome_valid(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome(""))

    def test_palindrome_invalid(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_palindrome_edge_cases(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("aa"))
        self.assertFalse(is_palindrome("ab"))

if __name__ == "__main__":
    unittest.main()
