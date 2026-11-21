# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

"""Terminal control helpers."""

import os
import sys


def clear_screen() -> None:
    # Do not issue shell commands (or ANSI cursor operations) for redirected output.
    if not sys.stdout.isatty():
        return
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def clear_line() -> None:
    if not sys.stdout.isatty():
        return
    sys.stdout.write("\033[1A\033[2K\r")
    sys.stdout.flush()


def exit_gracefully() -> None:
    raise SystemExit(0)
