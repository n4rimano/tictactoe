# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

"""Execute one move by the user or computer."""

from . import ai, prompt
from .board import Board, WEAPONS, mark


def move(board: Board, next_player: int, user_weapon: int, pc_weapon: int) -> None:
    if next_player == 0:
        cell = prompt.move(board)
        weapon = WEAPONS[user_weapon]
    elif next_player == 1:
        weapon = WEAPONS[pc_weapon]
        cell = ai.find_best_move(board, weapon, WEAPONS[user_weapon])
        if cell is None:
            return
    else:
        raise ValueError("Player must be 0 (user) or 1 (computer)")
    mark(board, cell, weapon)
