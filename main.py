from tkinter import *

from game import peaches_engine

WIDTH = HEIGHT = 800
DIMENSION = 8
SQ_SIZE = HEIGHT / DIMENSION

xstart = 0
ystart = 0


def draw_board(board):
    colors = ["#cfb997", "#556b2f"]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            x0, y0 = c * (HEIGHT / DIMENSION), r * (HEIGHT / DIMENSION)
            x1, y1 = x0 + (HEIGHT / DIMENSION), y0 + (HEIGHT / DIMENSION)
            canvas.create_rectangle(x0, y0, x1, y1, fill=colors[((r + c) % 2)])
    refresh_pieces(board)


def refresh_pieces(board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            x0, y0 = c * (HEIGHT / DIMENSION) + 50, r * (HEIGHT / DIMENSION) + 50
            canvas.create_text(x0, y0, text=board[r][c])


def get_piece_at_coordinate(x, y):
    print(g.get_pawn_moves(x // 100, y // 100, g.get_possible_moves()))


def on_start(event):
    global xstart
    global ystart
    xstart = event.x // 100
    ystart = event.y // 100


def on_drop(event):
    print(xstart, ystart, event.x // 100, event.y // 100)
    g.board[event.y // 100][event.x // 100] = g.board[ystart][xstart]
    g.board[ystart][xstart] = '--'
    g.print_board()
    draw_board(g.board)

if __name__ == "__main__":
    g = peaches_engine.GameState()
    root = Tk()
    root.resizable(False, False)
    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    draw_board(g.board)
    refresh_pieces(g.board)
    canvas.bind("<ButtonPress-1>", on_start)
    canvas.bind("<ButtonRelease-1>", on_drop)
    canvas.pack()
    root.mainloop()
