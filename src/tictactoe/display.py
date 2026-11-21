# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

"""Terminal-only presentation of a board."""

from . import ansi, terminal
from .board import Board


def colored_weapon(weapon: str) -> str:
    colors = {"o": ansi.YELLOW, "x": ansi.RED}
    return f"{colors[weapon]}{weapon}{ansi.RESET}" if weapon in colors else weapon


def generate_box(board: Board) -> str:
    rows = [" │ ".join(colored_weapon(str(cell)) for cell in row) for row in board]
    return (
        "┌───┬───┬───┐\n"
        f"│ {rows[0]} │\n"
        "├───┼───┼───┤\n"
        f"│ {rows[1]} │\n"
        "├───┼───┼───┤\n"
        f"│ {rows[2]} │\n"
        "└───┴───┴───┘"
    )


def show_board(board: Board) -> None:
    print(generate_box(board))


def clear_box() -> None:
    # A rendered board occupies seven lines (no leading/trailing blank lines).
    for _ in range(7):
        terminal.clear_line()
