import subprocess
from pathlib import Path
import sys
import shutil

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
    #    subprocess.run(
    #         ["sudo", "pacman", "-Syu"], capture_output=True, text=True, check=True
    #     )

        subprocess.run(
            ["stow", "--version"], capture_output=True, text=True, check=True
        )

        subprocess.run(["git", "--version"], capture_output=True, text=True, check=True)
        print("Stow and Git are up.")

    except:
        try:
            print("Missing something. Starting install...")
            subprocess.run(
                ["sudo", "pacman", "-S", "--noconfirm", "--needed", "stow", "git"],
                check=True,
            )
            print("Stow and Git are up.")
        except subprocess.CalledProcessError:
            print("There was a proble. Check your permission or your network")



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

def prepare_folders(app_name):
    DOTFILES_ROOT = Path("~/dotfiles").expanduser()
    if not DOTFILES_ROOT.exists():
        print(f"Creating: {DOTFILES_ROOT}")
        DOTFILES_ROOT.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "init", str(DOTFILES_ROOT)], capture_output=True)
        print(f"Empty repository initialized.")
    #DOTFILES_ROOT = Path("~/dotfiles").expanduser()
    
    basic_model = DOTFILES_ROOT / app_name / ".config"
    try:

        basic_model.mkdir(parents=True, exist_ok=True)
        print(f"Structure ready for: {app_name}")
        move_to_dotfiles(app_name, DOTFILES_ROOT)
    except Exception as e:
        print(f"Error crating folder: {e}")
        return None
    

def move_to_dotfiles(app_name, DOTFILES_ROOT):
    home_config = Path.home() / ".config" / app_name
    dotfiles_config_dir = Path.home() / "dotfiles" / app_name / ".config"
    

    if home_config.exists() and not home_config.is_symlink():
        shutil.move(str(home_config), str(dotfiles_config_dir))
        print(f" {app_name} moved")
        link_dotfiles(app_name, DOTFILES_ROOT)
    else:
        print(f"⚠️ {app_name} already a link or not exist")
        
def link_dotfiles(app_name, DOTFILES_ROOT):
    try:

        subprocess.run(
            ["stow", "-v", "-R", "-t", str(Path.home()), app_name],
            cwd=str(DOTFILES_ROOT),
            check=True
        )
        print(f"Check: Stow {app_name} ")
    except subprocess.CalledProcessError:
        print(f"Error using stow {app_name}.")