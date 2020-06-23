class Piece:
    def __init__(self):
        self.id = None
        self.kind = None
        self.color = None
        self.posx = None
        self.posy = None

    def move (self, x,y):
        pass

    def attack(self, piece):
        pass

class Pawn(Piece):
    def __init__(self):
        self.id = 1

class Tower(Piece):
    def __init__(self):
        self.id = 2

class Horse(Piece):
    def __init__(self):
        self.id = 3

class Bishop(Piece):
    def __init__(self):
        self.id = 4

class King(Piece):
    def __init__(self):
        self.id = 5

class Queen(Piece):
    def __init__(self):
        self.id = 6