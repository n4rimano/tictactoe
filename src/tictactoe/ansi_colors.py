# Copyright (C) 2026 Nariman Seyfulayev
# SPDX-License-Identifier: GPL-3.0-only

# \033[<sequence>m
# \033 escape char
# [ introduces CSI(Control Sequence Introducer)
# <parameters> = one of ansi codes
# m tells the terminal: apply these visual styles 

# ANSI escape sequence builder
def ansi(code: int) -> str:
    return f"\033[{code}m"

# Reset code
RESET = ansi(0)

# Foreground colors
foreground_colors = {
    "black": ansi(30),
    "red": ansi(31),
    "green": ansi(32),
    "yellow": ansi(33),
    "blue": ansi(34),
    "magenta": ansi(35),
    "cyan": ansi(36),
    "white": ansi(37),
    "bright_black": ansi(90),
    "bright_red": ansi(91),
    "bright_green": ansi(92),
    "bright_yellow": ansi(93),
    "bright_blue": ansi(94),
    "bright_magenta": ansi(95),
    "bright_cyan": ansi(96),
    "bright_white": ansi(97),
}

# Background colors
background_colors = {
    "black": ansi(40),
    "red": ansi(41),
    "green": ansi(42),
    "yellow": ansi(43),
    "blue": ansi(44),
    "magenta": ansi(45),
    "cyan": ansi(46),
    "white": ansi(47),
    "bright_black": ansi(100),
    "bright_red": ansi(101),
    "bright_green": ansi(102),
    "bright_yellow": ansi(103),
    "bright_blue": ansi(104),
    "bright_magenta": ansi(105),
    "bright_cyan": ansi(106),
    "bright_white": ansi(107),
}

# Text styles
text_styles = {
    "reset": ansi(0),
    "bold": ansi(1),
    "dim": ansi(2),
    "italic": ansi(3),
    "underline": ansi(4),
    "blink": ansi(5),
    "reverse": ansi(7),
    "hidden": ansi(8),
}

# Demo function to print all styles and colors
def demo_all():
    print("=== Foreground Colors ===")
    for name, code in foreground_colors.items():
        print(f"{code}{name}{RESET}")

    print("\n=== Background Colors ===")
    for name, code in background_colors.items():
        print(f"{code}{name}{RESET}")

    print("\n=== Text Styles ===")
    for name, code in text_styles.items():
        # Combine each style with white text for visibility
        print(f"{code}{foreground_colors['white']}{name}{RESET}")

    print("\n=== Combination Example ===")
    print(f"{text_styles['bold']}{foreground_colors['bright_yellow']}{background_colors['blue']}Bold Yellow on Blue{RESET}")

# Run demo if executed directly
if __name__ == "__main__":
    demo_all()
