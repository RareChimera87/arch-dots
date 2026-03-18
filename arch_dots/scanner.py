from pathlib import Path
import sys
class Color:
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'


def get_ignore_list():
    ignore_file = Path("arch_dots/.dotsignore")
    if not ignore_file.exists():
        return set()

    with open(ignore_file, "r") as f:
        return {line.strip() for line in f if line.strip() and not line.startswith("#")}


def get_config_files():
    config_path = Path.home() / ".config"
    candidates = []
    ignore_list = get_ignore_list()

    if not config_path.exists():
        print(f"Error: config folder not found in {config_path}")
        return []

    for item in config_path.iterdir():
        if item.name not in ignore_list and item.is_dir():
            f = {"name": item.name, "is_symlink": item.is_symlink()}
            candidates.append(f)

    return candidates

def selection(possible, linked):
    incorrect = True
    while incorrect:

        inp = input("\nPlease select number (ex. 1 3 5): ")
        clean = inp.split()
        selected = []
        for i in clean:
            if i.isdigit():
                num = int(i)
                if 0 <= num < len(possible):
                    if possible[num] not in linked:
                        selected.append(possible[num])
                        incorrect = False
                    else:
                        print(f"Number {num} is already linked. Skipping...")
                        incorrect = False
                        
                else:
                    print(f"Invalid option. Please retry")
                    incorrect = True
                    break
    return selected
                
    

def scanner():
    possible =[]
    linked = []
    
    apps = get_config_files()
    for i, app in enumerate(apps):
        nombre = app['name']
        possible.append(nombre)
        
        if app['is_symlink']:
            
            print(f"[{i}] {Color.GREEN}{Color.BOLD}{nombre}{Color.END} (Linked)")
            linked.append(nombre)
        else:
                
                print(f"[{i}] {Color.YELLOW}{nombre}{Color.END} (Pending)")
                
                #print(possible)
    
    selected = selection(possible, linked)
    if len(selected) > 0:
        print("Selectioned: ")
        for i in selected:
            #print(f"sssssssssssssssssssssss{i}")
            print(f"- {Color.GREEN}{i}{Color.END}")
        
        ans = input("Confirm [Y/n]: ")
        if ans == "Y" or ans == "Yes" or ans == "y" or ans == "yes":
            return selected


    print("Ok exiting...")
    sys.exit(0)
                
    