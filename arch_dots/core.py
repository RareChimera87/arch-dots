import subprocess
from pathlib import Path
import sys


def check_python_version():

    minimal_version = (3, 10)

    if sys.version_info < minimal_version:
        print(
            f"Error: arch-dots requires Python {minimal_version[0]}.{minimal_version[1]} or highuer."
        )
        print(f"Current version: {sys.version_info.major}.{sys.version_info.minor}")
        return False
    else:
        print(f"Python {sys.version_info.major}.{sys.version_info.minor} detected.")
        return True


def check_dependencies():
    try:
        subprocess.run(
            ["sudo", "pacman", "-Syu"], capture_output=True, text=True, check=True
        )

        subprocess.run(
            ["stow", "--version"], capture_output=True, text=True, check=True
        )

        subprocess.run(["git", "--version"], capture_output=True, text=True, check=True)
        print("Stow and Git are up.")

    except subprocess.CalledProcessError:
        try:
            print("Missing something. Starting install...")
            subprocess.run(
                ["sudo", "pacman", "-S", "--noconfirm", "--needed", "stow", "git"],
                check=True,
            )
            print("Stow and Git are up.")
        except subprocess.CalledProcessError:
            print("There was a proble. Check your permission or your network")
    except FileNotFoundError:
        print("You sure this is arch?")


def read_apps(config_file="apps.list"):
    apps = []
    path = Path(config_file)

    if not path.exists():
        print(f"{config_file} not found. Creating an empty one")
        path.touch()
        return apps

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                apps.append(line)

    return apps
