from arch_dots.scanner import scanner
from arch_dots.core import move_to_dotfiles, link_dotfiles, prepare_folders


def run():
    selected = scanner()
    for i in selected:
        prepare_folders(i)