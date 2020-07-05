from enum import Enum


def clean_list(list: list) -> list:
    r = range(0, 8)
    dellist = []
    for i in list:
        if i[0] not in r or i[1] not in r:
            dellist.append(i)
            print(i)
    print("Following will be removed: ",[move for move in list if move not in dellist])
    return [move for move in list if move not in dellist]


class Color(Enum):
    BLACK = 1
    WHITE = 2
    NONE = 3


class Piece:
    def __init__(self, x: int, y: int):
        self.points = 1
        self.posX = x
        self.posY = y
        self.color = Color.NONE

    def possible_move(self):
        pass


class Pawn(Piece):
    def __init__(self, x: int, y: int, c: Color):
        self.points = 1
        self.posX = x
        self.posY = y
        self.color = c

    def possible_move(self):

        if self.color == Color.BLACK:
            return clean_list([[self.posX+1, self.posY],
                               [self.posX+2, self.posY],
                               [self.posX + 1, self.posY + 1],
                               [self.posX + 1, self.posY - 1]])
        if self.color == Color.WHITE:
            return clean_list([[self.posX-1, self.posY],
                               [self.posX-2, self.posY],
                               [self.posX - 1, self.posY - 1],
                               [self.posX - 1, self.posY + 1]])


class Rook(Piece):
    def __init__(self, x: int, y: int, c: Color):
        self.points = 5
        self.posX = x
        self.posY = y
        self.color = c

    def possible_move(self):
        moves = []
        for i in range(7):
            moves.append([i, self.posY])
            moves.append([self.posX, i])
        moves.remove([self.posX, self.posY])
        return clean_list(moves)


class Knight(Piece):
    def __init__(self, x: int, y: int, c: Color):
        self.posX = x
        self.posY = y
        self.color = c
        self.points = 3

    def possible_move(self):
        moves = [[self.posX - 2, self.posY - 1], [self.posX - 2, self.posY + 1], [self.posX - 1, self.posY - 2],
                 [self.posX - 1, self.posY + 2], [self.posX + 1, self.posY - 2], [self.posX + 1, self.posY + 2],
                 [self.posX + 2, self.posY - 1], [self.posX + 2, self.posY + 1]]
        return clean_list(moves)


class Bishop(Piece):
    def __init__(self, x: int, y: int, c: Color):
        self.posX = x
        self.posY = y
        self.color = c
        self.points = 3

    def possible_move(self):
        moves = []
        r = range(0, 8)
        for i in range(0, 8):
            if self.posX + i in r and self.posY + i in r:
                moves.append([self.posX + i, self.posY + i])
            if self.posX + i in r and self.posY - i in r:
                moves.append([self.posX + i, self.posY - i])
            if self.posX - i in r and self.posY - i in r:
                moves.append([self.posX - i, self.posY - i])
            if self.posX - i in r and self.posY + i in r:
                moves.append([self.posX - i, self.posY + i])
        moves.remove([self.posX, self.posY])
        return clean_list(moves)


class King(Piece):
    def __init__(self, x: int, y: int, c: Color):
        self.posX = x
        self.posY = y
        self.color = c
        self.points = 'K'

    def possible_move(self):
        moves = []
        r = range(0, 8)
        for i in range(0, 8):
            if self.posX + i in r and self.posY + i in r:
                moves.append([self.posX + i, self.posY + i])
            if self.posX + i in r and self.posY - i in r:
                moves.append([self.posX + i, self.posY - i])
            if self.posX - i in r and self.posY - i in r:
                moves.append([self.posX - i, self.posY - i])
            if self.posX - i in r and self.posY + i in r:
                moves.append([self.posX - i, self.posY + i])
        for i in range(7):
            moves.append([i, self.posY])
            moves.append([self.posX, i])
        moves.remove([self.posX, self.posY])
        return clean_list(moves)


class Queen(Piece):
    def __init__(self, x: int, y: int, c: Color):
        self.posX = x
        self.posY = y
        self.color = c
        self.points = 9

    def possible_move(self):
        moves = [[self.posX + 1, self.posY],
                 [self.posX + 1, self.posY + 1],
                 [self.posX + 1, self.posY - 1],
                 [self.posX - 1, self.posY],
                 [self.posX - 1, self.posY + 1],
                 [self.posX - 1, self.posY - 1],
                 [self.posX, self.posY + 1],
                 [self.posX, self.posY - 1]]
        return clean_list(moves)


class Empty(Piece):
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.color = Color.NONE
        self.points = 0
