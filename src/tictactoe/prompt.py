# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

"""Interactive user input and validation."""

from . import ansi, terminal
from .board import Board, WEAPONS, available_cells
from .display import colored_weapon


def _read(prompt_text: str) -> str:
    try:
        response = input(prompt_text).strip().lower()
    except (KeyboardInterrupt, EOFError):
        terminal.clear_screen()
        terminal.exit_gracefully()
    terminal.clear_line()
    if response == "q":
        terminal.clear_screen()
        terminal.exit_gracefully()
    return response


def weapon() -> int:
    while True:
        choice = _read(
            f"Pick your weapon {colored_weapon(WEAPONS[1])}/{colored_weapon(WEAPONS[0])} or "
            f"{ansi.MAGENTA}{ansi.BOLD}q{ansi.RESET} to quit: "
        )
        if choice in WEAPONS:
            return WEAPONS.index(choice)


def move(board: Board) -> int:
    while True:
        choice = _read(
            f"Your move (1-9) or {ansi.MAGENTA}{ansi.BOLD}q{ansi.RESET} to quit: "
        )
        if choice.isascii() and choice.isdecimal():
            cell = int(choice)
            if cell in available_cells(board):
                return cell
