import enum
import re
from . import types
from . import value


class Mode(enum.Enum):
    scanning = 0
    elements = 1
    comma = 2
    end = 3


def parse(array):
    if type(array) is not str:
        raise TypeError("array expected string")

    mode = Mode.scanning
    pos = 0
    result = types.ArrayToken(type=types.Type.array, value=[])

    while pos < len(array) and mode != Mode.end:
        ch = array[pos]

        if mode == Mode.scanning:
            if re.match("[ \n\r\t]", ch):
                pos += 1
            elif ch == "[":
                pos += 1
                mode = Mode.elements
            else:
                raise SyntaxError("expected '[', actual '{ch}'".format(**locals()))
        elif mode == Mode.elements:
            if re.match("[ \n\r\t]", ch):
                pos += 1
            elif ch == "]":
                if len(result.value) > 0:
                    raise SyntaxError("unexpected ','")
                pos += 1
                mode = Mode.end
            else:
                slice = array[pos:]
                skip, token = value.parse(slice, r"[,\]\s]")
                result = types.ArrayToken(
                    type=types.Type.array, value=result.value + [token]
                )
                pos += skip
                mode = Mode.comma
        elif mode == Mode.comma:
            if re.match("[ \n\r\t]", ch):
                pos += 1
            elif ch == "]":
                pos += 1
                mode = Mode.end
            elif ch == ",":
                pos += 1
                mode = Mode.elements
            else:
                raise SyntaxError(
                    "expected ',' or ']', actual '{ch}'".format(**locals())
                )
        elif mode == Mode.end:
            pass
        else:
            raise SyntaxError(
                "unexpected mode {mode}".format(**locals())
            )  # f'Unexpected mode {mode}'

    if mode != Mode.end:
        raise SyntaxError("incomplete array expression, mode {mode}".format(**locals()))

    return types.Result(skip=pos, token=result)
