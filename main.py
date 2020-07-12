from tkinter import *

from PIL import Image, ImageTk

from game import peaches_engine

WIDTH = HEIGHT = 800
DIMENSION = 8
SQ_SIZE = HEIGHT / DIMENSION



def draw_board():
    colors = ["#cfb997", "#556b2f"]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            x0, y0 = c * (HEIGHT / DIMENSION), r * (HEIGHT / DIMENSION)
            x1, y1 = x0 + (HEIGHT / DIMENSION), y0 + (HEIGHT / DIMENSION)
            canvas.create_rectangle(x0, y0, x1, y1, fill=colors[((r + c) % 2)])


def refresh_pieces(board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            x0, y0 = c * (HEIGHT / DIMENSION)+50, r * (HEIGHT / DIMENSION)+50
            canvas.create_text(x0, y0, text=board[r][c])


def callback(event):
    print("clicked at ", event.x, event.y)

if __name__ == "__main__":
    g = peaches_engine.GameState()
    root = Tk()
    root.resizable(False, False)
    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    draw_board()
    refresh_pieces(g.board)
    canvas.bind("<Button-1>", callback)
    canvas.pack()
    root.mainloop()
