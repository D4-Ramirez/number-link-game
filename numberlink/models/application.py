"""
@author: Jose Lopez Garcia, David Ramirez Monroy
"""

from tkinter import Tk, Button
from .game import Game
from .point import Point


class Application:
    def __init__(self, parent: Tk):
        self.parent = parent
        self.curr_color = ''
        self.curr_line = []

    def create_widgets(self, system: Game):
        for i in range(1, system.board.rows + 1):
            for j in range(1, system.board.cols + 1):
                point = system.board.matrix[i][j]
                button = Button(self.parent,
                                text=point.value,
                                height=3,
                                width=8,
                                bg=point.color,
                                command=lambda point=point: self.pressed(
                                    point)
                                )
                button.grid(row=i, column=j)
        reset_button = Button(self.parent,
                              text='Reset',
                              font=('tahoma',  15),
                              bg='grey',
                              command=self.reset)
        reset_button.grid(row=system.board.rows + 2, column=(system.board.cols // 2) +
                          1 if (system.board.cols % 2) != 0 else (system.board.cols // 2))

    def pressed(self, point: Point):
        if point.color != '#FFFFFF':
            self.curr_color = point.color
            print(f'Current color is {self.curr_color}')
        else:
            if self.curr_color != '':
                button_to_paint = self.parent.grid_slaves(
                    point.col, point.row)[0]
                button_to_paint.configure(bg=self.curr_color)

    def reset(self):
        print('Reset')
