from game.Piece import *


# noinspection SpellCheckingInspection
class Board:
    grid = [[Rook(0, 0, Color.BLACK), Knight(0, 1, Color.BLACK), Bishop(0, 2, Color.BLACK), King(0, 3, Color.BLACK),
             Queen(0, 4, Color.BLACK), Bishop(0, 5, Color.BLACK), Knight(0, 6, Color.BLACK), Rook(0, 7, Color.BLACK)],
            [Pawn(1, 0, Color.BLACK), Pawn(1, 1, Color.BLACK), Pawn(1, 2, Color.BLACK), Pawn(1, 3, Color.BLACK),
             Pawn(1, 4, Color.BLACK), Pawn(1, 5, Color.BLACK), Pawn(1, 6, Color.BLACK), Pawn(1, 7, Color.BLACK)],
            [None, None, None, None, None, None, None, None],
            [None, None, King(1, 1, Color.WHITE), None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn(6, 0, Color.WHITE), Pawn(6, 1, Color.WHITE), Pawn(6, 2, Color.WHITE), Pawn(6, 3, Color.WHITE),
             Pawn(6, 4, Color.WHITE), Pawn(6, 5, Color.WHITE), Pawn(6, 6, Color.WHITE), Pawn(6, 7, Color.WHITE)],
            [Rook(7, 0, Color.WHITE), Knight(7, 1, Color.WHITE), Bishop(7, 2, Color.WHITE), King(7, 3, Color.WHITE),
             Queen(7, 4, Color.WHITE), Bishop(7, 5, Color.WHITE), Knight(7, 6, Color.WHITE), Rook(7, 7, Color.WHITE)]]

    def draw(self):
        pass

    def refresh(self):
        pass

    def check_moves(self, pos_x: int, pos_y: int):
        pass

    def minimax(self):
        pass


if __name__ == '__main__':
    board = Board()
    a = board.grid[3][2].move()
    print(len(a))
