# Tic-Tac-Toe

A simple terminal-based Tic-Tac-Toe game developed in **Python 3** as a learning project. The project also serves as an introduction to **uv** for managing Python projects and virtual environments.

## Features

- Human versus computer gameplay.

- Random selection of the starting player.

- X/O selection when the human starts; automatic assignment when the computer starts.

- Numbered board positions and validation of player moves.

- Coloured symbols and terminal screen updates using ANSI escape codes.

- Detection of wins across rows, columns, and diagonals.

- A computer opponent that currently chooses random available cells.

- Quit during an input prompt by entering q or pressing Ctrl+C.

## Requirements

- Python 3.13.3 or newer.
- A terminal with ANSI escape sequence support for the intended colours and screen updates.
- Optional: 'uv' to manage the Python environment and run the program.

No external Python libraries are required.

## Installation and Usage

Clone the repository and navigate to the project directory.

Install and synchronise the project environment using uv:

```bash
uv sync
```

Run the application from the project directory:

```bash
uv run tictactoe
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Demo
![Tic-tac-toe gameplay](assets/demo.gif)

## Flowchart

![Tic-Tac-Toe Application Flowchart](docs/tictactoeFlowChart.png)


## Modules
- `board.py`: fresh board, available cells, cell marking and weapon symbols.
- `rules.py`: winner and draw detection.
- `display.py`: ANSI colors and board layout.
- `ai.py`: tactical computer strategy.
- `prompt.py`: interactive input.
- `execute.py`: run one turn.
- `initialize.py`: select first player and weapons.
- `main.py`: single game loop.
- `terminal.py`, `ansi.py`: terminal utilities and colors.


## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. See the [LICENSE](LICENSE) file for details.
