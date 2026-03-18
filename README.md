# 🛠️ arch-dots

> [!CAUTION]
> **Warning:** This project is in early development (Alpha). It performs file move operations (`shutil.move`) and creates symbolic links. **Use it with caution** and ensure you have a backup of your configurations before proceeding.

An automated dotfiles manager written in Python, specifically designed for Arch Linux users.

**arch-dots** simplifies the transition to a centralized dotfiles repository. It scans your `~/.config` directory, identifies unsynced applications, and leverages **GNU Stow** to move them into a central repository while automatically creating the necessary symbolic links.

---

## ✨ Features

* **Intelligent Scanning:** Automatically distinguishes between real directories and existing symbolic links.
* **GNU Stow Integration:** Maintains a directory structure strictly compatible with the Linux $HOME$ standard.
* **Self-Managing Dependencies:** Automatically detects and installs `git` and `stow` using `pacman` if they are missing.
* **Interactive CLI:** User-friendly selection of applications via numeric input in the terminal.
* **Customizable Exclusion:** Built-in support for ignoring "junk" folders (browsers, cache, etc.) via a blacklist.
* **Automatic Git Initialization:** Sets up your `~/dotfiles` as a Git repository from the first run.

---

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/RareChimera87/arch-dots.git](https://github.com/RareChimera87/arch-dots.git)
    cd arch-dots
    ```

2.  **Set up a virtual environment (Optional but recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

---

## 💻 Usage

Simply run the main script:

```bash
python main.py
