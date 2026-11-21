import unittest
from unittest.mock import patch
from tictactoe import ai, execute, main, prompt
from tictactoe.board import new_board, available_cells, mark
from tictactoe.rules import winner, is_draw


class GameTests(unittest.TestCase):
    def test_new_board(self):
        a = new_board()
        b = new_board()
        mark(a, 1, "x")
        self.assertEqual(b[0][0], 1)
        self.assertEqual(available_cells(a), list(range(2, 10)))

    def test_mark_rejects_occupied(self):
        board = new_board()
        mark(board, 1, "x")
        with self.assertRaises(ValueError):
            mark(board, 1, "o")

    def test_winner_rows_columns_diagonals(self):
        for cells in ((1, 2, 3), (2, 5, 8), (3, 5, 7)):
            board = new_board()
            for cell in cells:
                mark(board, cell, "x")
            self.assertEqual(winner(board), "x")

    def test_draw(self):
        board = [["x", "o", "x"], ["x", "o", "o"], ["o", "x", "x"]]
        self.assertTrue(is_draw(board))
        self.assertIsNone(winner(board))

    def test_ai_wins_and_does_not_mutate(self):
        board = new_board()
        mark(board, 1, "x")
        mark(board, 2, "x")
        before = [row.copy() for row in board]
        self.assertEqual(ai.find_best_move(board, "x", "o"), 3)
        self.assertEqual(board, before)

    def test_ai_blocks(self):
        board = new_board()
        mark(board, 1, "o")
        mark(board, 2, "o")
        self.assertEqual(ai.find_best_move(board, "x", "o"), 3)

    def test_ai_full_board(self):
        self.assertIsNone(ai.find_best_move([["x"]*3 for _ in range(3)], "o", "x"))

    def test_user_move_validation(self):
        board = new_board()
        mark(board, 5, "x")
        with patch("tictactoe.prompt._read", side_effect=["hello", "5", "10", "3"]):
            self.assertEqual(prompt.move(board), 3)

    def test_execute_computer_move(self):
        board = new_board()
        execute.move(board, 1, 0, 1)
        self.assertEqual(board[1][1], "x")

    def test_main_completes_and_starts_fresh(self):
        # Force a deterministic computer-first game with all user choices legal.
        with patch("tictactoe.main.initialize.game", return_value=(1, 0, 1)), \
             patch("tictactoe.main.terminal.clear_screen"), \
             patch("tictactoe.main.terminal.clear_line"), \
             patch("tictactoe.execute.prompt.move", side_effect=lambda board: available_cells(board)[0]), \
             patch("builtins.print") as output:
            main.main()
            self.assertTrue(any("Winner:" in str(c) or "Draw" in str(c) for c in output.call_args_list))


if __name__ == "__main__":
    unittest.main()
