"""
@author: Jose Lopez Garcia, David Ramirez Monroy
"""

import sys
from tkinter import Tk
from numberlink.models.application import Application
from numberlink.models.game import Game

def main():
    file_name = sys.argv[1]
    game_system = Game(file_name)
    
    parent = Tk()
    
    app = Application(parent)
    app.create_widgets(game_system)

    parent.mainloop()

if __name__ == '__main__':
    main()
