#!/usr/bin/env python3

from arch_dots.core import check_python_version, check_dependencies
from arch_dots.manager import run


def main():
    print("--- Werlcome to Arch-Dots ---")

    if check_python_version():
        print("Starting configurations scanning...")
        check_dependencies()
        run()

        


if __name__ == "__main__":
    main()
