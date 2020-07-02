from game.piece import *


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

    def draw(self):
        pass

    def refresh(self):
        pass

    def check_moves(self, x, y):
        possible_moves = self.grid[x][y].move()
        dellist = []
        for i in possible_moves:
            if self.grid[i[0]][i[1]].color == self.grid[x][y].color:
                dellist.append(i)
        return [move for move in possible_moves if move not in dellist]

    def minimax(self):
        pass

    def printBoard(self):
        for sub in board.grid:
            print("")
            for i in sub:
                if i is not Empty:
                    print(i.points, end=' ')
                else:
                    print("0", end=' ')


if __name__ == '__main__':
    board = Board()
    print(board.check_moves(0, 1))
