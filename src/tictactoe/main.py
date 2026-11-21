# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

"""Game entry point and turn coordination."""

from . import display, execute, initialize, terminal
from .board import WEAPONS, new_board
from .display import colored_weapon
from .rules import is_draw, winner


def main() -> None:
    board = new_board()
    terminal.clear_screen()
    first_player, user_weapon, pc_weapon = initialize.game()
    # prompt.weapon() already clears its own input line when used.

    if first_player == 0:
        print(f"User picked {colored_weapon(WEAPONS[user_weapon])}")
        print(f"PC assigned {colored_weapon(WEAPONS[pc_weapon])}")
    else:
        print(f"PC picked {colored_weapon(WEAPONS[pc_weapon])}")
        print(f"User assigned {colored_weapon(WEAPONS[user_weapon])}")

    next_player = first_player
    display.show_board(board)
    while True:
        execute.move(board, next_player, user_weapon, pc_weapon)
        # Input handling removes the prompt line; only the seven board lines
        # remain above the cursor, so replace them instead of appending.
        display.clear_box()
        display.show_board(board)
        winning_weapon = winner(board)
        if winning_weapon is not None:
            winning_player = "User" if winning_weapon == WEAPONS[user_weapon] else "PC"
            print(f"Winner: {winning_player} ({colored_weapon(winning_weapon)})\n")
            return
        if is_draw(board):
            print("Draw\n")
            return
        next_player = 1 - next_player


if __name__ == "__main__":
    main()
