import enum
import re
from . import types
from . import value


class Mode(enum.Enum):
    scanning = 0
    value = 1
    end = 2


def parse(expression):
    if type(expression) is not str:
        raise TypeError("expression expected string")

    mode = Mode.scanning
    pos = 0

    while pos < len(expression) and mode != Mode.end:
        ch = expression[pos]

        if mode == Mode.scanning:
            if re.match(r"\s", ch):
                pos += 1
            else:
                mode = Mode.value
        elif mode == Mode.value:
            slice = expression[pos:]
            skip, token = value.parse(slice)
            pos += skip
            mode = Mode.end
        elif mode == Mode.end:
            pass
        else:
            raise SyntaxError(f"unexpected mode {mode}")

    return types.Result(skip=pos, token=token)
