class Piece:
    def __init__(self):
        self.points = None
        self.kind = None
        self.color = None
        self.posx = None
        self.posy = None

    def move(self, x, y):
        pass

    def attack(self, piece):
        pass
    

class Pawn(Piece):
    def __init__(self):
        Piece.__init__(self)
        self.points = 1


class Rook(Piece):
    def __init__(self):
        Piece.__init__(self)
        self.points = 2


class Knight(Piece):
    def __init__(self):
        Piece.__init__(self)
        self.points = 3


class Bishop(Piece):
    def __init__(self):
        Piece.__init__(self)
        self.points = 4


class King(Piece):
    def __init__(self):
        Piece.__init__(self)
        self.points = 5


class Queen(Piece):
    def __init__(self):
        Piece.__init__(self)
        self.points = 6


class Empty(Piece):
    def __init__(self):
        Piece.__init__(self)
        self.points = 0
