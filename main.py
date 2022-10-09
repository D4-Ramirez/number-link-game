"""
@author: Jose Lopez Garcia, David Ramirez Monroy
"""

from numlink.models.game import Game

import sys
import tkinter as tk

def checker(color):
    if color != '#FFFFFF':
        print(f'The color clicked is {color}')

def main():
    file_name = sys.argv[1]
    app = tk.Tk()
    left_frame = tk.Frame(app)
    left_frame.grid()

    game_system = Game(file_name)

    for i in range(1, game_system.board.rows + 1):
        for j in range(1, game_system.board.cols + 1):
            curr_point = game_system.board.matrix[i][j]
            curr_button = tk.Button(left_frame,
                                    text=curr_point.value,
                                    height=3,
                                    width=8,
                                    bg=curr_point.color,
                                    command=lambda color=curr_point.color:checker(color)
                                    )
            curr_button.grid(row=i, column=j)
    app.mainloop()


if __name__ == '__main__':
    main()
