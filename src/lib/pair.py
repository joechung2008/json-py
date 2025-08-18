import enum
import re
from . import string
from . import types
from . import value


class Mode(enum.Enum):
    scanning = 0
    string = 1
    colon = 2
    value = 3
    end = 4


def parse(pair, delimiters=None):
    if type(pair) is not str:
        raise TypeError("pair expected string")

    mode = Mode.scanning
    pos = 0
    result = types.PairToken(type=types.Type.pair, key=None, value=None)

    while pos < len(pair) and mode != Mode.end:
        ch = pair[pos]

        if mode == Mode.scanning:
            if re.match("[ \n\r\t]", ch):
                pos += 1
            else:
                mode = Mode.string
        elif mode == Mode.string:
            slice = pair[pos:]
            skip, token = string.parse(slice)
            result = types.PairToken(type=types.Type.pair, key=token, value=None)
            pos += skip
            mode = Mode.colon
        elif mode == Mode.colon:
            if re.match("[ \n\r\t]", ch):
                pos += 1
            elif ch == ":":
                pos += 1
                mode = Mode.value
            else:
                raise SyntaxError("expected ':', actual '{ch}'".format(**locals()))
        elif mode == Mode.value:
            slice = pair[pos:]
            skip, token = value.parse(slice, delimiters)
            result = types.PairToken(type=types.Type.pair, key=result.key, value=token)
            pos += skip
            mode = Mode.end
        elif mode == Mode.end:
            pass
        else:
            raise SyntaxError("unexpected mode {mode}".format(**locals()))

    if mode != Mode.end:
        raise SyntaxError("incomplete pair expression, mode {mode}".format(**locals()))

    return types.Result(skip=pos, token=result)
