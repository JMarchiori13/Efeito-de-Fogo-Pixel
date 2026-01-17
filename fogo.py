import tkinter as tk
import random

W, H = 80, 50
PIXEL = 10
FPS = 10

PALETA = [
    "#000000", "#200000", "#400000", "#600000",
   "#800000", "#a00000", "#c00000",
    "#ff2000", "#ff7000", "#ffaa00",
    "#ffff00", "#ffffaa", "#ffffff"
]

MAX = len(PALETA) - 1

fire = [[0] * W for _ in range(H)]
for x in range(W):
    fire[H - 1][x] = MAX

root = tk.Tk()
root.title("Fogo")

canvas = tk.Canvas(
    root,
    width=W * PIXEL,
    height=H * PIXEL,
    highlightthickness=0
)
canvas.pack()

pixels = [
    [
        canvas.create_rectangle(
            x * PIXEL,
            y * PIXEL,
            (x + 1) * PIXEL,
            (y + 1) * PIXEL,
            fill=PALETA[0],
            outline=""
        )
        for x in range(W)
    ]
    for y in range(H)
]

def espalhar():
    for y in range(1, H):
        for x in range(W):
            val = fire[y][x] - random.randint(0, 2)
            fire[y - 1][(x + random.randint(-1, 1)) % W] = max(0, val)

def render():
    for y in range(H):
        for x in range(W):
            canvas.itemconfig(
                pixels[y][x],
                fill=PALETA[fire[y][x]]
            )
    espalhar()
    root.after(1000 // FPS, render)

render()
root.mainloop()
