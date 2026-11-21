# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

"""Simple tactical opponent: win, block, center, corner, side."""

from .board import Board, available_cells, mark
from .rules import winner


def find_best_move(board: Board, player: str, opponent: str) -> int | None:
    """Return a 1-based available cell, or None if the board is full.

    Trials are made on copies so the original board cannot be mutated.
    """
    available = available_cells(board)
    if not available:
        return None

    for weapon in (player, opponent):
        for cell in available:
            trial = [row.copy() for row in board]
            mark(trial, cell, weapon)
            if winner(trial) == weapon:
                return cell

    for cell in (5, 1, 3, 7, 9, 2, 4, 6, 8):
        if cell in available:
            return cell
    return None
