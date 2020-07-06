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
                    if piece == 'p':
                        self.get_pawn_moves(r, c, moves)
                    if piece == 'R':
                        self.get_rook_moves(r, c, moves)
                    if piece == 'N':
                        self.get_knight_moves(r, c, moves)
                    if piece == 'B':
                        self.get_bishop_moves(r, c, moves)
                    if piece == 'K':
                        self.get_king_moves(r, c, moves)
                    if piece == 'Q':
                        self.get_queen_moves(r, c, moves)

    def get_pawn_moves(self, r: int, c: int, moves: [Move]):
        pass

    def get_rook_moves(self, r: int, c: int, moves: [Move]):
        pass

    def get_bishop_moves(self, r: int, c: int, moves: [Move]):
        pass

    def get_knight_moves(self, r: int, c: int, moves: [Move]):
        pass

    def get_king_moves(self, r: int, c: int, moves: [Move]):
        pass

    def get_queen_moves(self, r: int, c: int, moves: [Move]):
        pass
