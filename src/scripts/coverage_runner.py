import subprocess
import sys


def main():
    sys.exit(subprocess.call(["coverage", "run", "-m", "unittest", "discover"]))


def report():
    sys.exit(subprocess.call(["coverage", "report"]))


def html():
    subprocess.call(["coverage", "html"])
    subprocess.call(["start", "htmlcov/index.html"], shell=True)
    sys.exit(0)
