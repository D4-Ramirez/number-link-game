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
        self.curr_line = None

    def create_widgets(self, game_system: Game) -> None:
        for i in range(1, game_system.board.rows + 1):
            for j in range(1, game_system.board.cols + 1):
                point = game_system.board.matrix[i][j]
                button = Button(self.parent,
                                text=point.value,
                                height=3,
                                width=8,
                                bg=point.color,
                                command=lambda point=point, game_system=game_system: self.pressed(
                                    point, game_system)
                                )
                button.grid(row=i, column=j)
        reset_button = Button(self.parent,
                            text='Reset',
                            font=('tahoma',  15),
                            bg='grey',
                            command=self.reset)
        reset_button.grid(row=game_system.board.rows + 2, column=(game_system.board.cols // 2) +
                          1 if (game_system.board.cols % 2) != 0 else (game_system.board.cols // 2))

    def pressed(self, point: Point, game_system: Game) -> None:
        if not self.validate_if_button_pressed(point, game_system):
            if point.color != '#FFFFFF' and point.value > 0:
                if self.curr_line != None:
                    if self.curr_line.color == point.color and self.curr_line.value == point.value:
                        self.curr_line.points.append(point)
                        game_system.completed_lines.append(self.curr_line)
                        print(f'Line {self.curr_line.value} completed')
                        self.curr_line = None
                else:
                    self.curr_line = Line(point.color, point.value)
                    self.curr_line.points.append(point)                    
            else:
                if self.curr_line.color:
                    button_to_paint = self.parent.grid_slaves(point.col, point.row)[0]
                    if self.validate_pressed_button(point):
                        self.update_button(button_to_paint, point)
                        self.curr_line.points.append(point)

    def validate_pressed_button(self, point: Point) -> bool:
        if point.color == '#FFFFFF':
            if point.col + 1 is self.curr_line.points[-1].col and point.row is self.curr_line.points[-1].row:
                return True
            elif point.col - 1 is self.curr_line.points[-1].col and point.row is self.curr_line.points[-1].row:
                return True
            elif point.row + 1 is self.curr_line.points[-1].row and point.col is self.curr_line.points[-1].col:
                return True
            elif point.row - 1 is self.curr_line.points[-1].row and point.col is self.curr_line.points[-1].col:
                return True
            else:
                return False
    
    def validate_if_button_pressed(self, point: Point, game_system: Game) -> bool:
        for line in game_system.completed_lines:
            if point in line.points:
                return True
            else:
                return False
    
    def update_button(self, button: Button, point: Point) -> None:
        button.configure(bg=self.curr_line.color)
        point.update_color(self.curr_line.color)

    def reset(self):
        pass
