class TicTacToe:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.marks = {
            self.player1: "X",
            self.player2: "O"
        }
        self.winner = ""
        self.won = False
        self.player_turn = player1

    def get_board(self):
        return "\n".join("".join(f"[{cell}]" for cell in row) for row in self.board)

    def make_move(self, row, col, player):
        if self.board[row][col] != " ":
            return False
            
        mark = self.marks[player]
        self.board[row][col] = mark
        if self.check_winner(mark):
            self.winner = player
            self.won = True

        return True

    def check_winner(self, mark):
        board = self.board

        return any(
            # Check all rows
            all(cell == mark for cell in row) for row in board
        ) or any(
            # Check all columns
            all(board[r][c] == mark for r in range(3)) for c in range(3)
        ) or all(
            # Check left-to-right diagonal
            board[i][i] == mark for i in range (3)
        ) or all(
            # Check right-to-left diagonal
            board[i][2 - i] == mark for i in range(3)
        )

    def debug(self):
        print(self.get_board())
        print("---------")
        if self.won:
            print(f"The Winner is {self.winner}")
            print("---------")
