# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

"""Choose starting player and assign weapons."""

import random
from . import prompt


def game() -> tuple[int, int, int]:
    """Return (first_player, user_weapon_index, pc_weapon_index).

    Player 0 is the user; player 1 is the computer.
    """
    first_player = random.randrange(2)
    user_weapon = prompt.weapon() if first_player == 0 else random.randrange(2)
    return first_player, user_weapon, 1 - user_weapon
