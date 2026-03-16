#!/usr/bin/env python3

from arch_dots.core import check_python_version


def main():
    print("--- Bienvenido a Arch-Dots ---")

    # Llamamos a la función que está en core.py
    check_python_version()

    # Aquí seguiría el resto de tu programa
    print("Starting configurations scanning...")


if __name__ == "__main__":
    main()
