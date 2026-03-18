#!/usr/bin/env python3

from arch_dots.core import check_python_version
from arch_dots.scanner import scanner


def main():
    print("--- Werlcome to Arch-Dots ---")

    if check_python_version():
        print("Starting configurations scanning...")
        scanner()

        


if __name__ == "__main__":
    main()
