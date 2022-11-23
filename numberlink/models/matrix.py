"""
@author: Jose Lopez Garcia, David Ramirez Monroy
"""

from .point import Point


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = self.generate()

    def generate(self) -> list[list[Point]]:
        matrix = [[Point(x, y, 0, '#FFFFFF') for x in range(
            0, self.rows + 1)] for y in range(0, self.cols + 1)]
        return matrix

    def update_value(self, point: Point) -> None:
        self.matrix[point.row][point.col].value = point.value
        self.matrix[point.row][point.col].color = point.color
        
    def __str__(self) -> str:
        return f'rows: {self.rows}, cols: {self.cols}'
