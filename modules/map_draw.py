import tkinter
from modules import map_colors as mc


def update_map(canvas: tkinter.Canvas):
    canvas.config(background=mc.background)
