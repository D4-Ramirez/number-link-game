"""
@author: Jose Lopez Garcia, David Ramirez Monroy
"""

import random


def random_color():
    def r(): return random.randint(0, 255)
    color = '#%02X%02X%02X' % (r(), r(), r())
    return color
