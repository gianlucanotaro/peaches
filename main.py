from tkinter import *

from game import peaches_engine as pe

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


def load_images():
    pass


if __name__ == "__main__":
    root = Tk()
    pe
    root.resizable(False, False)
    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    draw_board()
    canvas.pack()
    root.mainloop()
