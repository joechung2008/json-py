import subprocess
import sys


def main():
    # Handle script name as first argument for Poetry scripts
    args = sys.argv[1:]
    script_name = sys.argv[0]
    # If called as 'poetry run coverage', 'coverage-report', 'coverage-html', or 'ci'
    if script_name.endswith("coverage"):
        subprocess.run(["coverage", "run", "-m", "unittest", "discover", "-s", "tests"])
    else:
        # Fallback for direct invocation
        if not args:
            subprocess.run(
                ["coverage", "run", "-m", "unittest", "discover", "-s", "tests"]
            )
        elif args[0] == "report":
            subprocess.run(["coverage", "report"])
        elif args[0] == "html":
            subprocess.run(["coverage", "html"])
        elif args[0] == "ci":
            if len(args) < 2:
                print("Usage: poetry run ci <filename>")
                sys.exit(1)
            filename = args[1]
            subprocess.run(
                ["coverage", "run", "-m", "unittest", "discover", "-s", "tests"]
            )
            subprocess.run(["coverage", "xml", "-o", filename])
        else:
            print(f"Unknown command: {' '.join(args)}")
            sys.exit(1)


if __name__ == "__main__":
    main()
