import sys
from pprint import pprint
import os
from lib.json import parse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def main():
    input_data = sys.stdin.read()
    result = parse(input_data)
    pprint(result)


if __name__ == "__main__":
    main()
