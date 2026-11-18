# main.py

from terminators import clear_line, clear_screen
from start import start
from move import move
from shared import weapons, board
from shared import generate_box, clear_box, check_winner, check_draw

def main():
    clear_screen()
    init_player, user_weapon, pc_weapon = start()
    clear_line()

    if init_player == 0:
        print(f"User picked {weapons[user_weapon]}\n"
              f"PC assigned {weapons[pc_weapon]}")
        print(generate_box(board))
        move(init_player, user_weapon, pc_weapon)
        clear_box()
        print(generate_box(board))

        next_player = (init_player + 1) % 2
        while True:
            move(next_player, user_weapon, pc_weapon)
            winner = check_winner(board, user_weapon, pc_weapon)
            if winner[0]:
                clear_box()
                print(generate_box(board))
                print(f"Winner: {winner[1]}\n")
                return
            if check_draw(board, user_weapon, pc_weapon):
                clear_box()
                print(generate_box(board))
                print("Draw\n")
                return
            clear_box()
            print(generate_box(board))
            next_player = (next_player + 1) % 2

    else: 
        print(f"PC picked {weapons[pc_weapon]}\n"
              f"User assigned {weapons[user_weapon]}")
        move(init_player, user_weapon, pc_weapon)
        print(generate_box(board))

        next_player = (init_player + 1) % 2
        while True:
            move(next_player, user_weapon, pc_weapon)
            winner = check_winner(board, user_weapon, pc_weapon)
            if winner[0]:
                clear_box()
                print(generate_box(board))
                print(f"Winner: {winner[1]}\n")
                return
            if check_draw(board, user_weapon, pc_weapon):
                clear_box()
                print(generate_box(board))
                print("Draw\n")
                return
            clear_box()
            print(generate_box(board))
            next_player = (next_player + 1) % 2


if __name__ == '__main__':
    main()
