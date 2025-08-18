import collections
import enum

Result = collections.namedtuple("Result", ["skip", "token"])


class Type(enum.Enum):
    unknown = 0
    array = 1
    false = 2
    null = 3
    number = 4
    object = 5
    pair = 6
    string = 7
    true = 8


ArrayToken = collections.namedtuple("ArrayToken", "type, value")
FalseToken = collections.namedtuple("FalseToken", "type, value")
NumberToken = collections.namedtuple("NumberToken", "type, value, valueAsString")
NullToken = collections.namedtuple("NullToken", "type, value")
ObjectToken = collections.namedtuple("ObjectToken", "type, members")
PairToken = collections.namedtuple("PairToken", "type, key, value")
StringToken = collections.namedtuple("StringToken", "type, value")
TrueToken = collections.namedtuple("TrueToken", "type, value")
