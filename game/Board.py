from game.Piece import *


class Board:
    grid = [[Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook],
            [Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn],
            [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]]

    def draw(self):
        pass

    def refresh(self):
        pass

    def check_move(self):
        pass

    def minimax(self):
        pass


if __name__ == '__main__':
    board = Board()
