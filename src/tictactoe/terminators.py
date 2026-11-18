# terminators.py

import os
import sys


def clear_screen():
    os.system("clear" if os.name == 'posix' else 'cls')

def clear_line():
    sys.stdout.flush()
    sys.stdout.write("\033[F")  # Move the cursor up one line
    sys.stdout.write("\033[K")  # Clear the entire line
    sys.stdout.flush()

def exit_gracefully():
    sys.exit(0)
