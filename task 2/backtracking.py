import tkinter as tk
import numpy as np
from random_mazes import random_maze


maze = np.array(random_maze)
rows, cols = maze.shape
cell_size = 100
root = tk.Tk()
root.title("Random maze with backtracking")
canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size)
canvas.pack()


def draw_maze():
    for r in range(rows):
        for c in range(cols):
            color = "black" if maze[r][c] == 1 else "white"
            canvas.create_rectangle(c * cell_size, r * cell_size, (c + 1) * cell_size, (r + 1) * cell_size, fill=color)


def is_safe(x, y):
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0


def solve_maze(x, y):
    if x == rows - 1 and y == cols - 1:
        canvas.create_rectangle(y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size, fill="green")
        return True

    if not is_safe(x, y):
        return False

    canvas.create_rectangle(y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size, fill="blue")
    canvas.update()

    for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_x, next_y = x + direction[0], y + direction[1]
        if solve_maze(next_x, next_y):
            return True
    canvas.create_rectangle(y * cell_size, x * cell_size, (y + 1) * cell_size, (x + 1) * cell_size, fill="red")
    canvas.update()
    return False


draw_maze()
solve_maze(0, 0)
root.mainloop()
