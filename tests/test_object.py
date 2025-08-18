import unittest
from src.lib import object


class TestObjectParse(unittest.TestCase):
    def test_parse_empty_object(self):
        result = object.parse("{}")
        self.assertEqual(result.token.type.name, "object")
        self.assertEqual(result.token.members, [])

    def test_parse_single_pair(self):
        # Mock pair.parse to return a dummy token
        class DummyToken:
            pass

        def dummy_parse(slice, regex):
            return (3, DummyToken())

        original_parse = object.pair.parse
        object.pair.parse = dummy_parse
        result = object.parse("{abc}")
        self.assertIsInstance(result.token.members[0], DummyToken)
        object.pair.parse = original_parse

    def test_parse_invalid_type(self):
        try:
            object.parse(123)
            self.fail("TypeError not raised")
        except TypeError:
            pass

    def test_parse_missing_brace(self):
        try:
            object.parse("")
            self.fail("SyntaxError not raised")
        except SyntaxError:
            pass

    def test_parse_unexpected_character(self):
        try:
            object.parse("{abc")
            self.fail("SyntaxError not raised")
        except SyntaxError:
            pass

    def test_parse_incomplete_object(self):
        try:
            object.parse("{abc,")
            self.fail("SyntaxError not raised")
        except SyntaxError:
            pass


if __name__ == "__main__":
    unittest.main()
