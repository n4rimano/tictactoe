# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

"""Board creation and mutation; no terminal or input dependencies."""

WEAPONS = ("o", "x")

type Board = list[list[int | str]]

# Outer loop creates a list containing 3 inner lists.
# Inner loop fills each inner list with 3 elements.
# Formula numbers the elements from 1 to 9.
def new_board() -> Board:
    return [[(row * 3 + 1) + col for col in range(3)] for row in range(3)]

#def new_board() -> Board:
#    return [
#        [
#            (row * 3 + 1) + col
#            for col in range(3)
#        ]
#        for row in range(3)
#    ]

#def new_boar() -> Board:
#    return [
#        [
#            (row * 3) + col
#            for col in range(1, 4)
#        ]
#        for row in range(3)
#    ]

def available_cells(board: Board) -> list[int]:
    return [cell for row in board for cell in row if isinstance(cell, int)]

#def available_cells(board: Board) -> list[int]:
#    return [
#        cell
#        for row in board
#        for cell in row
#        if isinstance(cell, int)
#    ]

def mark(board: Board, cell: int, weapon: str) -> None:
    if weapon not in WEAPONS:
        raise ValueError("Unknown weapon")
    if cell not in available_cells(board):
        raise ValueError(f"Cell {cell} is not available")
    row, col = divmod(cell - 1, 3)
    board[row][col] = weapon
