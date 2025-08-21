import subprocess
import sys


def main():
    sys.exit(subprocess.call(["black", "."]))
