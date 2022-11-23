"""
@author: Jose Lopez Garcia, David Ramirez Monroy
"""

from .point import Point

class Line:
    def __init__(self, color: str, value: 'int'):
        self.value: int = value
        self.color: str = color
        self.points: list[Point] = []
        
    def is_finished(self) -> bool:
        if self.points[0].value != self.points[-1].value and self.points[0].pos == self.points[-1].pos:
            return False
        else:
            return True
    
    def __str__(self) -> str:
        return f'value: {self.value}, color: {self.color}'