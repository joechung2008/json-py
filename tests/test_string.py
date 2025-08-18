import unittest
from src.lib import string, types


class TestStringParse(unittest.TestCase):
    def test_parse_basic_string(self):
        result = string.parse('"hello"')
        self.assertIsInstance(result.token, types.StringToken)
        self.assertEqual(result.token.value, "hello")

    def test_parse_escaped_quote(self):
        result = string.parse('"he\\"llo"')
        self.assertIsInstance(result.token, types.StringToken)
        self.assertEqual(result.token.value, 'he"llo')

    def test_parse_unicode(self):
        result = string.parse('"hi\\u0041"')
        self.assertIsInstance(result.token, types.StringToken)
        self.assertEqual(result.token.value, "hiA")


if __name__ == "__main__":
    unittest.main()
