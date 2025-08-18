import enum
import re
from . import types


class Mode(enum.Enum):
    scanning = 0
    char = 1
    escaped_char = 2
    unicode = 3
    end = 4


def parse(string):
    if type(string) is not str:
        raise TypeError("string expected string")

    mode = Mode.scanning
    pos = 0
    token = types.StringToken(types.Type.string, None)

    while pos < len(string) and mode != Mode.end:
        ch = string[pos]

        if mode == Mode.scanning:
            if re.match("[ \n\r\t]", ch):
                pos += 1
            elif ch == '"':
                token = types.StringToken(type=types.Type.string, value="")
                pos += 1
                mode = Mode.char
            else:
                raise SyntaxError(f"expected '\"', actual '{ch}'")
        elif mode == Mode.char:
            if ch == "\\":
                pos += 1
                mode = Mode.escaped_char
            elif ch == '"':
                pos += 1
                mode = Mode.end
            elif ch != "\n" and ch != "\r":
                token = types.StringToken(
                    type=types.Type.string, value=token.value + ch
                )
                pos += 1
            else:
                raise SyntaxError(f"unexpected character '{ch}'")
        elif mode == Mode.escaped_char:
            if ch == '"' or ch == "\\" or ch == "/":
                token = types.StringToken(
                    type=types.Type.string, value=token.value + ch
                )
                pos += 1
                mode = Mode.char
            elif ch == "b" or ch == "f" or ch == "n" or ch == "r" or ch == "t":
                token = types.StringToken(
                    type=types.Type.string,
                    value=token.value
                    + {"b": "\b", "f": "\f", "n": "\n", "r": "\r", "t": "\t"}[ch],
                )
                pos += 1
                mode = Mode.char
            elif ch == "u":
                pos += 1
                mode = Mode.unicode
            else:
                raise SyntaxError(f"unexpected escape character '{ch}'")
        elif mode == Mode.unicode:
            slice = string[pos : pos + 4]
            if len(slice) != 4:
                raise SyntaxError(f"incomplete Unicode code '{slice}'")
            try:
                hex = int(slice, 16)
            except ValueError:
                raise SyntaxError(f"unexpected Unicode code '{slice}'")
            token = types.StringToken(
                type=types.Type.string, value=token.value + chr(hex)
            )
            pos += 4
            mode = Mode.char
        elif mode == Mode.end:
            pass
        else:
            raise SyntaxError(f"unexpected mode {mode}")

    if mode != Mode.end:
        raise SyntaxError(f"incomplete string expression, mode {mode}")

    return types.Result(skip=pos, token=token)
