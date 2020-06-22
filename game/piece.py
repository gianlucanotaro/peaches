class piece:
    def __init__(self):
        self.kind = None
        self.color = None
        self.posx = None
        self.posy = None

    def move (self, x,y):
        pass

    def attack(self, piece):
        pass

class pawn(piece):
    pass

class tower(piece):
    pass

class horse(piece):
    pass

class bishop(piece):
    pass

class king(piece):
    pass

class queen(piece):
    pass
