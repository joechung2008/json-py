import unittest
from src.lib import number


class TestNumberParse(unittest.TestCase):
    def test_parse_integer(self):
        result = number.parse("42")
        self.assertEqual(result.token.value, 42.0)
        self.assertEqual(result.token.valueAsString, "42")

    def test_parse_negative_integer(self):
        result = number.parse("-7")
        self.assertEqual(result.token.value, -7.0)
        self.assertEqual(result.token.valueAsString, "-7")

    def test_parse_decimal(self):
        result = number.parse("3.14")
        self.assertEqual(result.token.value, 3.14)
        self.assertEqual(result.token.valueAsString, "3.14")

    def test_parse_scientific(self):
        result = number.parse("1.23e4")
        self.assertEqual(result.token.value, 12300.0)
        self.assertEqual(result.token.valueAsString.lower(), "1.23e4")

    def test_parse_invalid_type(self):
        try:
            number.parse(123)
            self.fail("TypeError not raised")
        except TypeError:
            pass

    def test_parse_incomplete_expression(self):
        try:
            number.parse("-")
            self.fail("SyntaxError not raised")
        except SyntaxError:
            pass

    def test_parse_unexpected_character(self):
        try:
            number.parse("12a")
            self.fail("SyntaxError not raised")
        except SyntaxError:
            pass


if __name__ == "__main__":
    unittest.main()
