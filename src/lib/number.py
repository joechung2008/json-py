import enum
import re
from . import types


class Mode(enum.Enum):
    scanning = 0
    characteristic = 1
    characteristic_digit = 2
    decimal_point = 3
    mantissa = 4
    exponent = 5
    exponent_sign = 6
    exponent_first_digit = 7
    exponent_digits = 8
    end = 9


def parse(number, delimiters="[ \n\r\t]"):
    if type(number) is not str:
        raise TypeError("number expected string")

    mode = Mode.scanning
    pos = 0
    token = types.NumberToken(type=types.Type.number, value=None, valueAsString="")

    while pos < len(number) and mode != Mode.end:
        ch = number[pos]

        if mode == Mode.scanning:
            if re.match(r"[ \n\r\t]", ch):
                pos += 1
            elif ch == "-":
                pos += 1
                token = types.NumberToken(
                    type=types.Type.number,
                    value=None,
                    valueAsString=token.valueAsString + ch,
                )
                mode = Mode.characteristic
            else:
                mode = Mode.characteristic
        elif mode == Mode.characteristic:
            if ch == "0":
                pos += 1
                token = types.NumberToken(
                    type=types.Type.number,
                    value=None,
                    valueAsString=token.valueAsString + ch,
                )
                mode = Mode.decimal_point
            elif re.match("[1-9]", ch):
                pos += 1
                token = types.NumberToken(
                    type=types.Type.number,
                    value=None,
                    valueAsString=token.valueAsString + ch,
                )
                mode = Mode.characteristic_digit
            else:
                raise SyntaxError(f"expected digit, actual '{ch}'")
        elif mode == Mode.characteristic_digit:
            if re.match(r"\d", ch):
                pos += 1
                token = types.NumberToken(
                    type=types.Type.number,
                    value=None,
                    valueAsString=token.valueAsString + ch,
                )
            elif delimiters is not None and re.match(delimiters, ch):
                mode = Mode.end
            else:
                mode = Mode.decimal_point
        elif mode == Mode.decimal_point:
            if ch == ".":
                pos += 1
                token = types.NumberToken(
                    type=types.Type.number,
                    value=None,
                    valueAsString=token.valueAsString + ch,
                )
                mode = Mode.mantissa
            elif delimiters is not None and re.match(delimiters, ch):
                mode = Mode.end
            else:
                mode = Mode.exponent
        elif mode == Mode.mantissa:
            if re.match(r"\d", ch):
                pos += 1
                token = types.NumberToken(
                    type=types.Type.number,
                    value=None,
                    valueAsString=token.valueAsString + ch,
                )
            elif re.match("e", ch, re.I):
                mode = Mode.exponent
            elif delimiters is not None and re.match(delimiters, ch):
                mode = Mode.end
            else:
                raise SyntaxError(f"unexpected character '{ch}'")
        elif mode == Mode.exponent:
            if re.match("e", ch, re.I):
                pos += 1
                token = types.NumberToken(
                    type=types.Type.number,
                    value=None,
                    valueAsString=token.valueAsString + "e",
                )
                mode = Mode.exponent_sign
            else:
                raise SyntaxError(f"expected 'e' or 'E', actual '{ch}'")
        elif mode == Mode.exponent_sign:
            if ch == "+" or ch == "-":
                pos += 1
                token = types.NumberToken(
                    type=types.Type.number,
                    value=None,
                    valueAsString=token.valueAsString + ch,
                )
                mode = Mode.exponent_first_digit
            else:
                mode = Mode.exponent_first_digit
        elif mode == Mode.exponent_first_digit:
            if re.match(r"\d", ch):
                pos += 1
                token = types.NumberToken(
                    type=types.Type.number,
                    value=None,
                    valueAsString=token.valueAsString + ch,
                )
                mode = Mode.exponent_digits
            else:
                raise SyntaxError(f"expected digit, actual '{ch}'")
        elif mode == Mode.exponent_digits:
            if re.match(r"\d", ch):
                pos += 1
                token = types.NumberToken(
                    type=types.Type.number,
                    value=None,
                    valueAsString=token.valueAsString + ch,
                )
            elif delimiters is not None and re.match(delimiters, ch):
                mode = Mode.end
            else:
                raise SyntaxError(f"expected digit, actual '{ch}'")
        elif mode == Mode.end:
            pass
        else:
            raise SyntaxError(f"unexpected mode {mode}")

    if mode == Mode.characteristic or mode == Mode.exponent_first_digit:
        raise SyntaxError(f"incomplete expression, mode {mode}")
    else:
        token = types.NumberToken(
            type=types.Type.number,
            value=float(token.valueAsString),
            valueAsString=token.valueAsString,
        )

    return types.Result(skip=pos, token=token)
