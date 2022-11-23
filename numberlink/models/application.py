"""
@author: Jose Lopez Garcia, David Ramirez Monroy
"""

from tkinter import Tk, Button
from .game import Game
from .point import Point
from .line import Line

class Application:
    def __init__(self, parent: Tk):
        self.parent = parent
        self.curr_color = ''
        self.curr_line = []

    def create_widgets(self, game_system: Game) -> None:
        for i in range(1, game_system.board.rows + 1):
            for j in range(1, game_system.board.cols + 1):
                point = game_system.board.matrix[i][j]
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
        reset_button.grid(row=game_system.board.rows + 2, column=(game_system.board.cols // 2) +
                          1 if (game_system.board.cols % 2) != 0 else (game_system.board.cols // 2))

    def pressed(self, point: Point) -> None:
        if point.color != '#FFFFFF':
                self.curr_color = point.color
                self.curr_line.append(point)             
        else:
            if self.curr_color != '':
                button_to_paint = self.parent.grid_slaves(point.col, point.row)[0]
                if self.validate_pressed_button(point):
                    self.update_button(button_to_paint, point)
                    self.curr_line.append(point)

    def validate_pressed_button(self, point: Point) -> bool:
        if point.color == '#FFFFFF':
            if point.col + 1 is self.curr_line[-1].col and point.row is self.curr_line[-1].row:
                return True
            elif point.col - 1 is self.curr_line[-1].col and point.row is self.curr_line[-1].row:
                return True
            elif point.row + 1 is self.curr_line[-1].row and point.col is self.curr_line[-1].col:
                return True
            elif point.row - 1 is self.curr_line[-1].row and point.col is self.curr_line[-1].col:
                return True
            else:
                return False
    
    def update_button(self, button: Button, point: Point) -> None:
        button.configure(bg=self.curr_color)
        point.update_color(self.curr_color)

    def reset(self):
        pass
