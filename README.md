# Python Projects Collection

A collection of small-to-medium Python projects (learning exercises, games, GUIs, data viz, and utilities). Each folder is a standalone project. This README summarizes what each does and how to run them locally.

## Getting Started

- **Python**: Use Python 3.11+ (3.13 is fine if supported by your environment).
- **Create venv**:
  ```bash
  python3 -m venv .venv && source .venv/bin/activate
  ```
- **Install common dependencies (if needed)**: Most projects rely on the standard library. Some may use `tkinter`, `pandas`, `numpy`. Install as needed:
  ```bash
  pip install -U pip
  pip install pandas numpy
  ```
- **Run**: Navigate into a project directory and execute its entry script (commonly `main.py`).
  ```bash
  cd "<project-folder>"
  python main.py
  ```

## Project Index

### Core Learning/Exercises
- **Day16/Day17/Day18/Day19/Day22/Day23/Day24/Day25/Day26/Day27/Day30**: Daily practice scripts following a Python bootcamp. Many use `turtle`, file I/O, or small algorithms.
  - Run example:
    ```bash
    cd Day25
    python main.py
    ```

- **learnpandas/**: Small scripts experimenting with `pandas`.
  ```bash
  cd learnpandas
  python main.py
  ```

- **Numpy/**: Numpy learning snippets (`learn1.py` … `learn5.py`).
  ```bash
  cd Numpy
  python main.py
  ```

### GUI and Games
- **Capstone_Flashcard31/**: A flashcard app (likely French vocabulary) using a CSV data file and Tkinter.
  - Data: `Capstone_Flashcard31/data/french_words.csv`
  - Run:
    ```bash
    cd Capstone_Flashcard31
    python main.py
    ```

- **Snake_game/**: Classic Snake game using `turtle`. Tracks score in `data.txt`.
  ```bash
  cd Snake_game
  python main.py
  ```

- **pomodaro gui/**: Pomodoro timer GUI (Tkinter) with a tomato icon.
  ```bash
  cd "pomodaro gui"
  python main.py
  ```

- **password manager/**: Simple GUI password manager (Tkinter). Reads/writes `data.json` and `data.txt`.
  ```bash
  cd "password manager"
  python main.py
  ```

- **US_state_project/**: U.S. States guessing game using `turtle` and CSV data.
  - Files: `50_states.csv`, `blank_states_img.gif`
  ```bash
  cd US_state_project
  python main.py
  ```

- **HirstPainting/**: Dot painting inspired by Damien Hirst using `turtle`.
  ```bash
  cd HirstPainting
  python main.py
  ```

- **oop-coffee-machine-start/oop-coffee-machine-start/**: OOP coffee machine simulation (console-based). Modules: `coffee_maker.py`, `menu.py`, `money_machine.py`.
  ```bash
  cd oop-coffee-machine-start/oop-coffee-machine-start
  python main.py
  ```

### Text/Data Utilities
- **Mail Merge Project Start/**: Generates personalized invitation letters from a starting template and a list of names.
  - Input:
    - Template: `Mail Merge Project Start/Input/Letters/starting_letter.txt`
    - Names: `Mail Merge Project Start/Input/Names/invited_names.txt`
  - Output: `Mail Merge Project Start/Output/ReadyToSend/`
  ```bash
  cd "Mail Merge Project Start"
  python main.py
  ```

- **NATO-alphabet-start/**: Convert words to the NATO phonetic alphabet using a CSV mapping.
  ```bash
  cd NATO-alphabet-start
  python main.py
  ```

- **Data vizulization/**: Simple plotting/visualization examples (likely `matplotlib`/`pandas`).
  ```bash
  cd "Data vizulization"
  python main.py
  ```

- **Day25/**: CSV/weather and squirrel dataset examples.
  - Data: `weather_data.csv`, `Squirrel_Data.csv`, `Squirrel_count.csv`
  ```bash
  cd Day25
  python main.py
  ```

### ML/Analysis
- **stock_price_predictor/**: Scripts for data collection and preprocessing for stock price prediction.
  - Files: `data_collection.py`, `data_preprocessing.py`
  ```bash
  cd stock_price_predictor
  python data_collection.py
  python data_preprocessing.py
  ```

### Miscellaneous
- **PythonProject/Practice.py**: General practice script.
- **Day27/**: `mile_to_km.py` and `Other_Tkinter_Widgets.py` demonstrate Tkinter widgets and a converter GUI.
- **Day18/**: `spirograph.py` and `random_diection.py` generate turtle graphics.
- **Day22/**: `paddle.py`, `ball.py`, `scoreboard.py` underpin a Pong-like game driven by `main.py`.

## Data/Assets
Some projects require local data/assets. Ensure paths stay relative to each project folder:
- `Capstone_Flashcard31/data/french_words.csv`
- `US_state_project/50_states.csv` and `blank_states_img.gif`
- `HirstPainting/Hirstspotpainting.jpg` (for reference)
- `Snake_game/data.txt` (created/updated on run)
- `password manager/data.json` and `logo.png`

## Notes
- GUI apps need a desktop environment (Tkinter comes with most Python installs).
- Turtle graphics open a window; close it to end the program if it doesn’t auto-terminate.
- If you hit missing-package errors, install the suggested packages for that project only (keep the global environment minimal).

## Contributing
This repo is a learning playground. Feel free to open PRs to improve docs, add instructions, or refine code structure.

## License
Provided as-is for educational purposes. Add a LICENSE file if you plan to distribute. 
