import sys
import os
import runpy
from .tracer import start_trace, stop_trace, show_results

def main():
    if len(sys.argv) < 2:
        print("Usage: oracletrace <file.py>")
        return 1

    target = sys.argv[1]

    if not isinstance(target, str) or not os.path.exists(target):
        print(f"Target not found: {target}")
        return 1

    target = os.path.abspath(target)
    root = os.getcwd()
    target_dir = os.path.dirname(target)
    sys.path.insert(0, target_dir)


    start_trace(root)
    runpy.run_path(target, run_name="__main__")
    stop_trace()
    show_results()

    return 0

if __name__ == "__main__":
    sys.exit(main())
