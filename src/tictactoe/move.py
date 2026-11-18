# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

# Standard library
from random import choice

# Local modules
from .shared import weapons, board, get_available_cells
from .prompt import prompt_move

def apply_move(move: int, weapon: str) -> None:  # Internal func
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if move == cell:
                board[i][j] = weapon

def move(next_move: int, user_weapon: int, pc_weapon: int) -> None:
    available_cells = get_available_cells(board)

    if next_move == 0:
        user_move = prompt_move()
        if user_move in available_cells:
            apply_move(user_move, weapons[user_weapon])
    else:
        if available_cells:
            pc_move = choice(available_cells)
            apply_move(pc_move, weapons[pc_weapon])
