import subprocess
import sys


def main():
    sys.exit(subprocess.call([sys.executable, "-m", "unittest", "discover", "-v"]))
