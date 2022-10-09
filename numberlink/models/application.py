"""
@author: Jose Lopez Garcia, David Ramirez Monroy
"""

from tkinter import Tk, Button
from .game import Game


class Application:
    def __init__(self, parent: Tk):
        self.parent = parent
        self.curr_color = ''

    def create_widgets(self, system: Game):
        for i in range(1, system.board.rows + 1):
            for j in range(1, system.board.cols + 1):
                self.point = system.board.matrix[i][j]
                self.button = Button(self.parent,
                                     text=self.point.value,
                                     height=3,
                                     width=8,
                                     bg=self.point.color,
                                     command=self.pressed
                                     )
                self.button.grid(row=i, column=j)

    def pressed(self):
        print('pressed')