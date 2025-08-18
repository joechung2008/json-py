import unittest
from src.lib import array


class TestArrayParse(unittest.TestCase):
    def test_parse_empty_array(self):
        result = array.parse("[]")
        self.assertEqual(result.token.type.name, "array")
        self.assertEqual(result.token.value, [])

    def test_parse_single_element(self):
        # Mock value.parse to return a dummy token
        class DummyToken:
            pass

        def dummy_parse(slice, regex):
            return (1, DummyToken())

        original_parse = array.value.parse
        array.value.parse = dummy_parse
        result = array.parse("[a]")
        self.assertIsInstance(result.token.value[0], DummyToken)
        array.value.parse = original_parse

    def test_parse_multiple_elements(self):
        # Mock value.parse to return different dummy tokens
        class DummyToken1:
            pass

        class DummyToken2:
            pass

        def dummy_parse(slice, regex):
            if slice.startswith("a"):
                return (1, DummyToken1())
            else:
                return (1, DummyToken2())

        original_parse = array.value.parse
        array.value.parse = dummy_parse
        result = array.parse("[a,b]")
        self.assertIsInstance(result.token.value[0], DummyToken1)
        self.assertIsInstance(result.token.value[1], DummyToken2)
        array.value.parse = original_parse

    def test_parse_invalid_type(self):
        try:
            array.parse(123)
            self.fail("TypeError not raised")
        except TypeError:
            pass

    def test_parse_missing_bracket(self):
        try:
            array.parse("")
            self.fail("SyntaxError not raised")
        except SyntaxError:
            pass

    def test_parse_unexpected_character(self):
        try:
            array.parse("[a")
            self.fail("SyntaxError not raised")
        except SyntaxError:
            pass

    def test_parse_incomplete_array(self):
        try:
            array.parse("[a,")
            self.fail("SyntaxError not raised")
        except SyntaxError:
            pass


if __name__ == "__main__":
    unittest.main()
