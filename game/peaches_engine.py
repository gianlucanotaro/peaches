class Move:
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def get_chess_notation(self):
        return self.get_rank_file(self.startRow, self.startCol) + self.get_rank_file(self.endRow, self.endCol)

    def get_rank_file(self, r: int, c: int):
        return self.colsToFiles[c] + self.rowsToRanks[r]


class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp" for i in range(8)],
            ["-" for i in range(8)],
            ["-" for i in range(8)],
            ["-" for i in range(8)],
            ["-" for i in range(8)],
            ["wp" for i in range(8)],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.move_functions = {'p': self.get_pawn_moves, 'R': self.get_rook_moves, 'N': self.get_knight_moves,
                               'B': self.get_bishop_moves, 'K': self.get_king_moves, 'Q': self.get_queen_moves}

        # True = White
        # False = Black
        self.turnPlayer = True

        self.move_log = []

    def make_move(self, move: Move):
        self.board[move.startRow][move.startCol] = "-"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.move_log.append(move)
        self.turnPlayer = not self.turnPlayer

    def undo_move(self):
        if len(self.move_log) != 0:
            move = self.move_log.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.turnPlayer = not self.turnPlayer

    def get_valid_moves(self):
        return self.get_possible_moves()

    def get_possible_moves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.turnPlayer) and (turn == 'b' and not self.turnPlayer):
                    piece = self.board[r][c][1]
                    self.move_functions[piece](r, c, moves)
        return moves

    def get_pawn_moves(self, r: int, c: int, moves: [Move]):
        if self.turnPlayer:  # White player turn
            if self.board[r - 1][c] == '-':
                moves.append(Move((r, c), r - 1, c), self.board)
                if r == 6 and self.board[r - 2][c] == '-':
                    moves.append(Move((r, c), (r - 1, c - 1), self.board))
            if c - 1 >= 0:  # Captures to the left
                if self.board[r - 1][c - 1][0] == 'b':
                    moves.append(Move((r, c), (r - 1, c - 1), self.board))
            if c + 1 <= 7:  # Captures to the right
                if self.board[r - 1][c + 1][0] == 'b':
                    moves.append(Move((r, c), (r - 1, c + 1), self.board))

        else:  # Black movement
            if self.board[r + 1][c] == '-':
                moves.append(Move((r, c), r + 1, c), self.board)
                if r == 1 and self.board[r + 2][c] == '-':
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))
            if c - 1 >= 0:  # Captures to the left
                if self.board[r + 1][c - 1][0] == 'w':
                    moves.append(Move((r, c), (r + 1, c - 1), self.board))
            if c + 1 <= 7:  # Captures to the right
                if self.board[r - 1][c + 1][0] == 'w':
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))

    def get_rook_moves(self, r: int, c: int, moves: [Move]):
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        enemyColor = "b" if self.turnPlayer else "w"
        for d in directions:
            for i in range(1, 8):
                endRow = r + d(0) * i
                endCol = c + d(0) * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '-':
                        moves.append(Move(r, c), (endRow, endCol), self.board)
                    elif endPiece[0] == enemyColor:
                        moves.append(Move(r, c)(endRow, endCol), self.board)
                        break
                    else:
                        break
                else:
                    break

    def get_bishop_moves(self, r: int, c: int, moves: [Move]):
        directions = ((1, 1), (1, -1), (-1, 1), (-1, -1))
        enemyColor = "b" if self.turnPlayer else "w"
        for d in directions:
            for i in range(1, 8):
                endRow = r + d(0) * i
                endCol = c + d(0) * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '-':
                        moves.append(Move(r, c), (endRow, endCol), self.board)
                    elif endPiece[0] == enemyColor:
                        moves.append(Move(r, c)(endRow, endCol), self.board)
                        break
                    else:
                        break
                else:
                    break

    def get_knight_moves(self, r: int, c: int, moves: [Move]):
        directions = ((2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1), (1, 2), (-1, 2))
        enemyColor = "b" if self.turnPlayer else "w"
        for d in directions:
            for i in range(1, 8):
                endRow = r + d(0) * i
                endCol = c + d(0) * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '-':
                        moves.append(Move(r, c), (endRow, endCol), self.board)
                    elif endPiece[0] == enemyColor:
                        moves.append(Move(r, c)(endRow, endCol), self.board)
                        break
                    else:
                        break
                else:
                    break

    def get_king_moves(self, r: int, c: int, moves: [Move]):
        directions = ((1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1))
        enemyColor = "b" if self.turnPlayer else "w"
        for d in directions:
            for i in range(1, 8):
                endRow = r + d(0) * i
                endCol = c + d(0) * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == '-':
                        moves.append(Move(r, c), (endRow, endCol), self.board)
                    elif endPiece[0] == enemyColor:
                        moves.append(Move(r, c)(endRow, endCol), self.board)
                        break
                    else:
                        break
                else:
                    break

    def get_queen_moves(self, r: int, c: int, moves: [Move]):
        directions = ((1, 1), (-1, 1), (-1, -1), (1, -1), (1, 0), (0, 1), (-1, 0), (0, -1))
        pass

    def print_board(self):
        for sub in self.board:
            print(sub)


if __name__ == '__main__':
    game = GameState()
    game.make_move(Move((1, 1), (2, 5), game.board))
    game.print_board()
