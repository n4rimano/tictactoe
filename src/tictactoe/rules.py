# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

"""Pure game rules, independent of presentation and player types."""

from .board import Board, WEAPONS, available_cells

WINNING_LINES = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)


def winner(board: Board) -> str | None:
    for line in WINNING_LINES:
        cells = [board[row][col] for row, col in line]
        if cells[0] in WEAPONS and cells.count(cells[0]) == 3:
            return cells[0]
    return None


def is_draw(board: Board) -> bool:
    return winner(board) is None and not available_cells(board)
