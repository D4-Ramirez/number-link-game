"""
@author: Jose Lopez Garcia, David Ramirez Monroy
"""


class Point:
    def __init__(self, row, col, value, color):
        self.row = row
        self.col = col
        self.value = value
        self.color = color
        self.pos = (self.row, self.col)
        
    def update_color(self, new_color) -> None:
        self.color = new_color

    def __str__(self) -> str:
        return f'row: {self.row}, col: {self.col}, value: {self.value}, color: {self.color}'