from tkinter import *

from PIL import Image, ImageTk

from game import peaches_engine

WIDTH = HEIGHT = 800
DIMENSION = 8
SQ_SIZE = HEIGHT / DIMENSION
IMAGES = {}


def draw_board():
    colors = ["#cfb997", "#556b2f"]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            x0, y0 = c * (HEIGHT / DIMENSION), r * (HEIGHT / DIMENSION)
            x1, y1 = x0 + (HEIGHT / DIMENSION), y0 + (HEIGHT / DIMENSION)
            canvas.create_rectangle(x0, y0, x1, y1, fill=colors[((r + c) % 2)])


def refresh_board(board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            x0, y0 = c * (HEIGHT / DIMENSION), r * (HEIGHT / DIMENSION)
            if board[r][c] != "--":
                img = Image.open("img/" + board[r][c] + ".png")
                ph = ImageTk.PhotoImage(img)
                canvas.create_image(x0, y0, image=ph)


def load_images():
    pieces = ['wp', 'wR', 'wN', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = ImageTk.PhotoImage(Image.open("img/" + piece + ".png"))


if __name__ == "__main__":
    g = peaches_engine.GameState()
    root = Tk()
    root.resizable(False, False)
    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    draw_board()
    refresh_board(g.board)
    canvas.pack()
    root.mainloop()
