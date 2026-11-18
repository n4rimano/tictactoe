# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

# Local modules
from .terminators import clear_line, clear_screen, exit_gracefully
from .shared import weapons, board, RESET, get_available_cells, ansi


def prompt_weapon() -> int:
    while True:
        try:
            char = input(
            f"Pick your weapon {weapons[1]}/{weapons[0]} or {ansi(95)}{ansi(1)}q{RESET} to quit: ").lower()
            clear_line()
            if char == "q":
                clear_screen()
                exit_gracefully()
            if len(char) == 1 and char in weapons[0]:
                return 0
            elif len(char) == 1 and char in weapons[1]:
                return 1
        except KeyboardInterrupt:
            clear_screen()
            exit_gracefully()


def prompt_move() -> int:
    while True:
        try:
            # Quit on start or ignore bad input
            user_input = input(f"Your move or {ansi(95)}{ansi(1)}q{RESET} to quit: ").lower()
            clear_line()
            if user_input == "q":
                clear_screen()
                exit_gracefully()
            if not user_input.isdigit():  # isdigit checks for . or other non digit input
                continue

            # Correct input
            cell = int(user_input)
            if cell not in range(1, 10):
                continue
            if cell not in get_available_cells(board):
                continue
            return cell    
        except KeyboardInterrupt:
            clear_screen()
            exit_gracefully()
