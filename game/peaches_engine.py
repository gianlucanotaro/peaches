class Move:
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, start_sequence, end_sequence, board):
        self.start_row = start_sequence[0]
        self.start_col = start_sequence[1]
        self.end_row = end_sequence[0]
        self.end_col = end_sequence[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        self.move_id = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col

    def __str__(self):
        return str(self.cols_to_files[self.start_col]) + str(self.rows_to_ranks[self.start_row]) + \
               str(self.cols_to_files[self.end_col]) + str(self.rows_to_ranks[self.end_row])

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_id == other.move_id
        return False

    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

    def get_rank_file(self, r: int, c: int):
        return self.cols_to_files[c] + self.rows_to_ranks[r]


class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp" for i in range(8)],
            ["--" for i in range(8)],
            ["--" for i in range(8)],
            ["--" for i in range(8)],
            ["--" for i in range(8)],
            ["wp" for i in range(8)],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.move_functions = {'p': self.get_pawn_moves, 'R': self.get_rook_moves, 'N': self.get_knight_moves,
                               'B': self.get_bishop_moves, 'K': self.get_king_moves, 'Q': self.get_queen_moves}

        # True = White
        # False = Black
        self.turnPlayer = True

        self.move_log = []

        self.whiteKingLoc = (7, 4)
        self.blackKingLoc = (0, 4)

    def make_move(self, move: Move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.turnPlayer = not self.turnPlayer
        if move.piece_moved == 'wK':
            self.whiteKingLoc = (move.end_row, move.end_col)
        if move.piece_moved == 'bK':
            self.blackKingLoc = (move.end_row, move.end_col)

    def undo_move(self):
        if len(self.move_log) != 0:
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.turnPlayer = not self.turnPlayer
            if move.piece_moved == 'wK':
                self.whiteKingLoc = (move.start_row, move.start_col)
            if move.piece_moved == 'bK':
                self.blackKingLoc = (move.end_row, move.end_col)

    def get_valid_moves(self):
        return self.get_possible_moves()

    def get_possible_moves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.turnPlayer) or (turn == 'b' and not self.turnPlayer):
                    piece = self.board[r][c][1]
                    self.move_functions[piece](r, c, moves)
        return moves

    def get_pawn_moves(self, r: int, c: int, moves: [Move]):
        if self.turnPlayer:  # White player turn
            if self.board[r - 1][c] == '--':
                moves.append(Move((r, c), (r - 1, c), self.board))
                if r == 6 and self.board[r - 2][c] == '--':
                    moves.append(Move((r, c), (r - 2, c), self.board))
            if c - 1 >= 0:  # Captures to the left
                if self.board[r - 1][c - 1][0] == 'b':
                    moves.append(Move((r, c), (r - 1, c - 1), self.board))
            if c + 1 <= 7:  # Captures to the right
                if self.board[r - 1][c + 1][0] == 'b':
                    moves.append(Move((r, c), (r - 1, c + 1), self.board))

        else:  # Black movement
            if self.board[r + 1][c] == '--':
                moves.append(Move((r, c), (r + 1, c), self.board))
                if r == 1 and self.board[r + 2][c] == '--':
                    moves.append(Move((r, c), (r + 2, c), self.board))
            if c - 1 >= 0:  # Captures to the left
                if self.board[r + 1][c - 1][0] == 'w':
                    moves.append(Move((r, c), (r + 1, c - 1), self.board))
            if c + 1 <= 7:  # Captures to the right
                if self.board[r - 1][c + 1][0] == 'w':
                    moves.append(Move((r, c), (r + 1, c + 1), self.board))

    def get_rook_moves(self, r: int, c: int, moves: [Move]):
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        enemy_color = "b" if self.turnPlayer else "w"
        for d in directions:
            for i in range(1, 8):
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == '--':
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                        break
                    else:
                        break
                else:
                    break

    def get_bishop_moves(self, r: int, c: int, moves: [Move]):
        directions = ((1, 1), (1, -1), (-1, 1), (-1, -1))
        enemy_color = "b" if self.turnPlayer else "w"
        for d in directions:
            for i in range(1, 8):
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == '--':
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                        break
                    else:
                        break
                else:
                    break

    def get_knight_moves(self, r: int, c: int, moves: [Move]):
        directions = ((2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1), (1, 2), (-1, 2))
        enemy_color = "b" if self.turnPlayer else "w"
        for d in directions:
            end_row = r + d[0]
            end_col = c + d[1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece == '--':
                    moves.append(Move((r, c), (end_row, end_col), self.board))
                elif end_piece[0] == enemy_color:
                    moves.append(Move((r, c), (end_row, end_col), self.board))
            else:
                break

    def get_king_moves(self, r: int, c: int, moves: [Move]):
        directions = ((1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1))
        enemy_color = "b" if self.turnPlayer else "w"
        for d in directions:
            for i in range(1, 8):
                end_row = r + d[0] * i
                end_col = c + d[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == '--':
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:
                        moves.append(Move((r, c), (end_row, end_col), self.board))
                        break
                    else:
                        break
                else:
                    break

    def get_queen_moves(self, r: int, c: int, moves: [Move]):
        directions = ((1, 1), (-1, 1), (-1, -1), (1, -1), (1, 0), (0, 1), (-1, 0), (0, -1))
        enemy_color = "b" if self.turnPlayer else "w"
        for d in directions:
            end_row = r + d[0]
            end_col = c + d[1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece == '--':
                    moves.append(Move((r, c), (end_row, end_col), self.board))
                elif end_piece[0] == enemy_color:
                    moves.append(Move((r, c), (end_row, end_col), self.board))
            else:
                break
