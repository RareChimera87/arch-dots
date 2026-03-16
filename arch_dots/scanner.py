from pathlib import Path


def get_config_files():
    config_path = Path.home() / ".config"
    candidates = []
    ignore_list = ["google-chrome", "PulseEffects", "gtk-3.0"]

    if not config_path.exists():
        print(f"Error: config folder not found in {config_path}")
        return []

    for item in config_path.iterdir():
        if item.name not in ignore_list and item.is_dir():
            f = {"name": item.name, "is_symlink": item.is_symlink()}
            candidates.append(f)

    return candidates
