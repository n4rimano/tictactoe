# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

# Standard library
from random import randrange

# Local modules
from tictactoe import prompt


def initialize() -> tuple[int, int, int]:
    first_player = randrange(0, 2)
    if first_player == 0:
        user_weapon = prompt.weapon()
    else:
        user_weapon = randrange(0, 2)
    pc_weapon = 1 - user_weapon
    return first_player, user_weapon, pc_weapon
