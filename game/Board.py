from game.Piece import *


class Board:
    grid = [[Tower, Horse, Bishop, King, Queen, Bishop, Horse, Tower],
            [Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn, Pawn],
            [Tower, Horse, Bishop, King, Queen, Bishop, Horse, Tower]]

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
