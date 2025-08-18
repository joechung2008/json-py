from . import array
import enum
from . import number
from . import object
import re
from . import string
from . import types


class Mode(enum.Enum):
    scanning = 0
    array = 1
    false = 2
    null = 3
    number = 4
    object = 5
    string = 6
    true = 7
    end = 8


def parse(value, delimiters=None):
    if type(value) is not str:
        raise TypeError("value expected string")

    mode = Mode.scanning
    pos = 0
    token = None

    while pos < len(value) and mode != Mode.end:
        ch = value[pos]

        if mode == Mode.scanning:
            if re.match(r"[ \n\r\t]", ch):
                pos += 1
            elif ch == "[":
                mode = Mode.array
            elif ch == "f":
                mode = Mode.false
            elif ch == "n":
                mode = Mode.null
            elif re.match(r"[-\d]", ch):
                mode = Mode.number
            elif ch == "{":
                mode = Mode.object
            elif ch == '"':
                mode = Mode.string
            elif ch == "t":
                mode = Mode.true
            elif delimiters is not None and re.match(delimiters, ch):
                mode = Mode.end
            else:
                raise SyntaxError(f"unexpected character '{ch}'")
        elif mode == Mode.array:
            slice = value[pos:]
            skip, token = array.parse(slice)
            pos += skip
            mode = Mode.end
        elif mode == Mode.false:
            slice = value[pos : pos + 5]
            if slice == "false":
                token = types.FalseToken(type=types.Type.false, value=False)
                pos += 5
                mode = Mode.end
            else:
                raise SyntaxError(f"expected 'false', actual '{slice}'")
        elif mode == Mode.null:
            slice = value[pos : pos + 4]
            if slice == "null":
                token = types.NullToken(type=types.Type.null, value=None)
                pos += 4
                mode = Mode.end
            else:
                raise SyntaxError(f"expected 'null', actual '{slice}'")
        elif mode == Mode.number:
            slice = value[pos:]
            skip, token = number.parse(
                slice, delimiters if delimiters is not None else r"\s"
            )
            pos += skip
            mode = Mode.end
        elif mode == Mode.object:
            slice = value[pos:]
            skip, token = object.parse(slice)
            pos += skip
            mode = Mode.end
        elif mode == Mode.string:
            slice = value[pos:]
            skip, token = string.parse(slice)
            pos += skip
            mode = Mode.end
        elif mode == Mode.true:
            slice = value[pos : pos + 4]
            if slice == "true":
                token = types.TrueToken(type=types.Type.true, value=True)
                pos += 4
                mode = Mode.end
            else:
                raise SyntaxError(f"expected 'true', actual '{slice}'")
        elif mode == Mode.end:
            pass
        else:
            raise SyntaxError(f"unexpected mode {mode}")

    if token is None:
        raise SyntaxError("value cannot be empty")

    return types.Result(skip=pos, token=token)
