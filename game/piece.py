from enum import Enum


def cleanList(list: list) -> list:
    r = range(0, 8)
    for i in list:
        if i[0] not in r or i[1] not in r:
            list.remove(i)
            print(i)
    return list


class Color(Enum):
    BLACK = 1
    WHITE = 2


class Pawn:
    def __init__(self, x: int, y: int, c: Color):
        self.points = 1
        self.posX = x
        self.posY = y
        self.color = c

    def move(self):

        if self.color == Color.BLACK:
            return cleanList([[self.posX, self.posY + 1],
                              [self.posX, self.posY + 2],
                              [self.posX + 1, self.posY + 1],
                              [self.posX - 1, self.posY + 1]])
        if self.color == Color.WHITE:
            return cleanList([[self.posX, self.posY - 1],
                              [self.posX, self.posY - 2],
                              [self.posX + 1, self.posY - 1],
                              [self.posX - 1, self.posY - 1]])


class Rook:
    def __init__(self, x: int, y: int, c: Color):
        self.points = 5
        self.posX = x
        self.posY = y
        self.color = c

    def move(self):
        moves = []
        for i in range(7):
            moves.append([i, self.posY])
            moves.append([self.posX, i])
        moves.remove([self.posX, self.posY])
        return cleanList(moves)


class Knight:
    def __init__(self, x: int, y: int, c: Color):
        self.posX = x
        self.posY = y
        self.color = c
        self.points = 3

    def move(self):
        moves = [[self.posX - 2, self.posY - 1], [self.posX - 2, self.posY + 1], [self.posX - 1, self.posY - 2],
                 [self.posX - 1, self.posY + 2], [self.posX + 1, self.posY - 2], [self.posX + 1, self.posY + 2],
                 [self.posX + 2, self.posY - 1], [self.posX + 2, self.posY + 1]]
        return cleanList(moves)


class Bishop:
    def __init__(self, x: int, y: int, c: Color):
        self.posX = x
        self.posY = y
        self.color = c
        self.points = 3

    def move(self):
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
        return cleanList(moves)


class King:
    def __init__(self, x: int, y: int, c: Color):
        self.posX = x
        self.posY = y
        self.color = c
        self.points = 'K'

    def move(self):
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
        return cleanList(moves)


class Queen:
    def __init__(self, x: int, y: int, c: Color):
        self.posX = x
        self.posY = y
        self.color = c
        self.points = 9

    def move(self):
        moves = [[self.posX + 1, self.posY],
                 [self.posX + 1, self.posY + 1],
                 [self.posX + 1, self.posY - 1],
                 [self.posX - 1, self.posY],
                 [self.posX - 1, self.posY + 1],
                 [self.posX - 1, self.posY - 1],
                 [self.posX, self.posY + 1],
                 [self.posX, self.posY - 1]]
        return cleanList(moves)
