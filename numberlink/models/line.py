"""
@author: Jose Lopez Garcia, David Ramirez Monroy
"""

from .point import Point

class Line:
    def __init__(self, color: str = '', value: 'int' = 0):
        self.value: int = value
        self.color: str = color
        self.points: list[Point] = []
    
    def __str__(self) -> str:
        return f'value: {self.value}, color: {self.color}, points: {self.points}'