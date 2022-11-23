"""
@author: Jose Lopez Garcia, David Ramirez Monroy
"""

from .matrix import Matrix
from .point import Point
from .line import Line
from ..utils.utils import random_color


class Game:
    def __init__(self, file):
        self.file = file
        self.lines: list[Line] = []
        self.board = self.generate_board()

    def generate_board(self) -> list[list[Point]]:
        memory = []
        with open(self.file) as file:
            lines = file.readlines()
            for line in lines:
                if '\n' in line:
                    line.replace('\n', '')
                if lines.index(line) == 0:
                    size = list(map(int, line.split(' ,')))
                    matrix = Matrix(size[0], size[1])
                else:
                    point = list(map(int, line.split(',')))
                    if point[0] <= size[0] and point[1] <= size[1]:
                        in_tuple = [
                            tup for tup in memory if tup[0] == point[2]]
                        if in_tuple:
                            matrix.update_value(
                                Point(point[0], point[1], point[2], in_tuple[0][1]))
                        else:
                            color = random_color()
                            memory.append((point[2], color))
                            matrix.update_value(
                                Point(point[0], point[1], point[2], color))
            return matrix
    
    def __str__(self) -> str:
        return f'file: {self.file}'
