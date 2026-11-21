# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

"""Board creation and mutation; no terminal or input dependencies."""

WEAPONS = ("o", "x")

type Board = list[list[int | str]]


def new_board() -> Board:
    return [[row * 3 + col + 1 for col in range(3)] for row in range(3)]


def available_cells(board: Board) -> list[int]:
    return [cell for row in board for cell in row if isinstance(cell, int)]


def mark(board: Board, cell: int, weapon: str) -> None:
    if weapon not in WEAPONS:
        raise ValueError("Unknown weapon")
    if cell not in available_cells(board):
        raise ValueError(f"Cell {cell} is not available")
    row, col = divmod(cell - 1, 3)
    board[row][col] = weapon
