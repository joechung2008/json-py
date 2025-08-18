import unittest
from src.lib import value, types


class TestValueParse(unittest.TestCase):
    def test_parse_true(self):
        result = value.parse("true")
        self.assertIsInstance(result.token, types.TrueToken)
        self.assertEqual(result.token.value, True)

    def test_parse_false(self):
        result = value.parse("false")
        self.assertIsInstance(result.token, types.FalseToken)
        self.assertEqual(result.token.value, False)

    def test_parse_null(self):
        result = value.parse("null")
        self.assertIsInstance(result.token, types.NullToken)
        self.assertIsNone(result.token.value)


if __name__ == "__main__":
    unittest.main()
