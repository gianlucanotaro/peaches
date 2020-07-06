import random

from game.piece import *


class Move:
    # Map key to value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}


class Board:
    grid = [[Rook(0, 0, Color.BLACK), Knight(0, 1, Color.BLACK), Bishop(0, 2, Color.BLACK), King(0, 3, Color.BLACK),
             Queen(0, 4, Color.BLACK), Bishop(0, 5, Color.BLACK), Knight(0, 6, Color.BLACK), Rook(0, 7, Color.BLACK)],
            [Pawn(1, 0, Color.BLACK), Pawn(1, 1, Color.BLACK), Pawn(1, 2, Color.BLACK), Pawn(1, 3, Color.BLACK),
             Pawn(1, 4, Color.BLACK), Pawn(1, 5, Color.BLACK), Pawn(1, 6, Color.BLACK), Pawn(1, 7, Color.BLACK)],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
            [Pawn(6, 0, Color.WHITE), Pawn(6, 1, Color.WHITE), Pawn(6, 2, Color.WHITE), Pawn(6, 3, Color.WHITE),
             Pawn(6, 4, Color.WHITE), Pawn(6, 5, Color.WHITE), Pawn(6, 6, Color.WHITE), Pawn(6, 7, Color.WHITE)],
            [Rook(7, 0, Color.WHITE), Knight(7, 1, Color.WHITE), Bishop(7, 2, Color.WHITE), King(7, 3, Color.WHITE),
             Queen(7, 4, Color.WHITE), Bishop(7, 5, Color.WHITE), Knight(7, 6, Color.WHITE), Rook(7, 7, Color.WHITE)]]

    def check_moves(self, x, y):
        possible_moves = self.grid[x][y].possible_move()
        dellist = []
        for i in possible_moves:
            if self.grid[i[0]][i[1]].color == self.grid[x][y].color:
                dellist.append(i)
        return [move for move in possible_moves if move not in dellist]

    def printBoard(self):
        for sub in board.grid:
            print("")
            for i in sub:
                print(i.points, end=' ')
        print("")

    def move_piece(self, piece: Piece):
        x = piece.posX
        y = piece.posY
        a = self.check_moves(x, y)
        selection = random.choice(a)
        print("Piece will move: ", selection)
        piece.posX, piece.posY = selection
        board.grid[piece.posX][piece.posY] = piece
        board.grid[x][y] = Empty()

    def getChessNotation(self, move: Move):
        pass


if __name__ == '__main__':
    board = Board()
    board.printBoard()
    board.move_piece(board.grid[1][7])
    board.printBoard()
