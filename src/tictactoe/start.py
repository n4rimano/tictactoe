# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

# Standard library
from random import randrange

# Local modules
from .prompt import prompt_weapon


def start() -> tuple[int, int, int]:
    init_player = randrange(0, 2)
    
    if init_player == 0:
        user_weapon = prompt_weapon()
    else:
        user_weapon = 1 - randrange(0, 2)
    
    pc_weapon = 1 - user_weapon
    return init_player, user_weapon, pc_weapon
