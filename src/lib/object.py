import enum
import re
from . import pair
from . import types


class Mode(enum.Enum):
    scanning = 0
    pair = 1
    delimiter = 2
    end = 3


def parse(object):
    if type(object) is not str:
        raise TypeError("object expected string")

    mode = Mode.scanning
    pos = 0
    result = types.ObjectToken(type=types.Type.object, members=[])

    while pos < len(object) and mode != Mode.end:
        ch = object[pos]

        if mode == Mode.scanning:
            if re.match("[ \n\r\t]", ch):
                pos += 1
            elif ch == "{":
                pos += 1
                mode = Mode.pair
            else:
                raise SyntaxError(f"expected '{{', actual '{ch}'")
        elif mode == Mode.pair:
            if re.match("[ \n\r\t]", ch):
                pos += 1
            elif ch == "}":
                if len(result.members) > 0:
                    raise SyntaxError("unexpected ','")
                pos += 1
                mode = Mode.end
            else:
                slice = object[pos:]
                skip, token = pair.parse(slice, r"[\s,\}]")
                result = types.ObjectToken(
                    type=types.Type.object, members=result.members + [token]
                )
                pos += skip
                mode = Mode.delimiter
        elif mode == Mode.delimiter:
            if re.match("[ \n\r\t]", ch):
                pos += 1
            elif ch == ",":
                pos += 1
                mode = Mode.pair
            elif ch == "}":
                pos += 1
                mode = Mode.end
            else:
                raise SyntaxError(f"expected ',' or '}}', actual '{ch}'")
        elif mode == Mode.end:
            pass
        else:
            raise SyntaxError(f"unexpected mode {mode}")

    if mode != Mode.end:
        raise SyntaxError(f"incomplete object expression, mode {mode}")

    return types.Result(skip=pos, token=result)
