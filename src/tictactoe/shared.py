# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

# Local modules
from .terminators import clear_line
from .ansi_colors import ansi, RESET

#==========Varialbes==========#

weapons = (
           f"{ansi(93)}{ansi(1)}o{RESET}",
           f"{ansi(91)}{ansi(1)}x{RESET}"
           )

board = tuple([[(i * 3 + 1 + j) for j in range(3)] for i in range(3)])


#==========Functions==========#

def get_move_count(board) -> int:
    return sum(1 for row in board for cell in row if cell in weapons)

def get_available_cells(board) -> list[int]:
    return [cell for row in board for cell in row if isinstance(cell, int)]

def check_winner(board, user_weapon, pc_weapon) -> tuple[bool, str] or tuple[bool, None]:
    winner_conditions = (
((0, 0), (0, 1), (0, 2)),
((1, 0), (1, 1), (1, 2)),
((2, 0), (2, 1), (2, 2)),

((0, 0), (1, 0), (2, 0)),
((0, 1), (1, 1), (2, 1)),
((0, 2), (1, 2), (2, 2)),

((0, 0), (1, 1), (2, 2)),
((0, 2), (1, 1), (2, 0))
)
    for line in winner_conditions:
        if all(board[r][c] == weapons[user_weapon] for r, c in line):
            return True, weapons[user_weapon]
        elif all(board[r][c] == weapons[pc_weapon] for r, c in line):
            return True, weapons[pc_weapon]
    return False, None

def check_draw(board, user_weapon, pc_weapon) -> bool:
    return get_move_count(board) == 9 and not check_winner(board, user_weapon, pc_weapon)[0]

def generate_box(board) -> str:
    return f"""
┌───┬───┬───┐
│ {board[0][0]} │ {board[0][1]} │ {board[0][2]} │
├───┼───┼───┤
│ {board[1][0]} │ {board[1][1]} │ {board[1][2]} │
├───┼───┼───┤
│ {board[2][0]} │ {board[2][1]} │ {board[2][2]} │
└───┴───┴───┘
"""

def clear_box() -> None:
    for _ in range(9):
        clear_line()
