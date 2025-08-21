import os
import sys

from prettyprinter import pformat
from src.lib.json import parse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def main():
    input_data = sys.stdin.read()
    result = parse(input_data)
    print(pformat(result))


if __name__ == "__main__":
    main()
