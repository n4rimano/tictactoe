def find_best_move(board, player, opponent):
    # 1. Can we win?
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if check_winner(board, player):
                board[i] = " "
                return i
            board[i] = " "

    # 2. Can we block opponent from winning?
    for i in range(9):
        if board[i] == " ":
            board[i] = opponent
            if check_winner(board, opponent):
                board[i] = " "
                return i
            board[i] = " "

    # 3. Take center
    if board[4] == " ":
        return 4

    # 4. Take a corner
    for i in [0, 2, 6, 8]:
        if board[i] == " ":
            return i

    # 5. Take a side
    for i in [1, 3, 5, 7]:
        if board[i] == " ":
            return i

    return -1  # Shouldn't happen unless board is full

def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    return any(all(board[i] == player for i in line) for line in wins)
