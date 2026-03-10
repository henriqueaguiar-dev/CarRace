Car Race
========

### About

Car Race is a 2D racing game developed with Pygame. The game has 2 levels and each level ends with a timeout event.
Single-player distance is saved in a SQLite3 database.

### Controls

Player 1: Arrow keys (accelerate/brake/steer)

### Setup (macOS)

Recommended (Python 3.12 with wheels):
1. `brew install python@3.12`
2. `/opt/homebrew/opt/python@3.12/bin/python3.12 -m venv .venv`
3. `source .venv/bin/activate`
4. `python -m pip install -U pip`
5. `python -m pip install -r requirements.txt`

If you are on Python 3.14, pip will try to build Pygame from source. You will need SDL headers:
1. `brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf pkg-config`
2. `python -m pip install -r requirements.txt`

No virtualenv (system Python):
1. `python3 -m pip install --user --break-system-packages -r requirements.txt`

### Run

`python main.py`
