# Template for GUI from https://github.com/Lesaun/2048-expectimax-ai/blob/master/main_gui.py

from tkinter import *
from AI2048 import Game

SIZE = 500
GRID_PADDING = 10
BACKGROUND_COLOUR_GAME = "#92877d"
BACKGROUND_COLOUR_CELL_EMPTY = "#bebebe"
BACKGROUND_COLOUR_DICT = {  2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e"}
CELL_COLOUR_DICT = {2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                    32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                    512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2"}
FONT = ("Verdana", 40, "bold")

class GameUI(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.game = Game()
        self.grid()
        self.master.title("2048 AI")
        self.gridCells = []

        self.init_grid()
        self.update_grid_cells()

        self.run_game()
        self.mainloop()

    def run_game(self):
        while True:
            if (len(self.game.grid.get_empty_spots()) < 5): 
                self.game.depth = 5
            else:
                self.game.depth = 4
            if (self.game.grid.move(self.game.ai.get_best_move(self.game.grid, self.game.depth)) == False):
                for i in self.game.moves:
                    if (self.game.grid.move(i) != False):
                        break
            self.update_grid_cells()

            if (len(self.game.grid.get_empty_spots()) == 0):
                self.game_over_screen()
                break

            self.update()

    def game_over_screen(self):
        for i in range(4):
            for n in range(4):
                self.gridCells[i][n].configure(text="", bg=BACKGROUND_COLOUR_CELL_EMPTY)

        self.gridCells[1][1].configure(text="TOP",bg=BACKGROUND_COLOUR_CELL_EMPTY)
        self.gridCells[1][2].configure(text="4",bg=BACKGROUND_COLOUR_CELL_EMPTY)
        top_4 = [item for sublist in self.game.grid.matrix for item in sublist]
        top_4 = sorted(top_4)
        self.gridCells[2][0].configure(text=str(top_4[-1]), bg=BACKGROUND_COLOUR_DICT[top_4[-1]], fg=CELL_COLOUR_DICT[top_4[-1]])
        self.gridCells[2][1].configure(text=str(top_4[-2]), bg=BACKGROUND_COLOUR_DICT[top_4[-2]], fg=CELL_COLOUR_DICT[top_4[-2]])
        self.gridCells[2][2].configure(text=str(top_4[-3]), bg=BACKGROUND_COLOUR_DICT[top_4[-3]], fg=CELL_COLOUR_DICT[top_4[-3]])
        self.gridCells[2][3].configure(text=str(top_4[-4]), bg=BACKGROUND_COLOUR_DICT[top_4[-4]], fg=CELL_COLOUR_DICT[top_4[-4]])

        self.update()

    def init_grid(self):
        background = Frame(self, bg=BACKGROUND_COLOUR_GAME, width=SIZE, height=SIZE)
        background.grid()

        for i in range(4):
            grid_row = []
            for j in range(4):

                cell = Frame(background, bg=BACKGROUND_COLOUR_CELL_EMPTY, width=SIZE/4, height=SIZE/4)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOUR_CELL_EMPTY, justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.gridCells.append(grid_row)

    def update_grid_cells(self):
        for i in range(4):
            for j in range(4):
                new_number = int(self.game.grid.matrix[i][j])
                if new_number == 0:
                    self.gridCells[i][j].configure(text="", bg=BACKGROUND_COLOUR_CELL_EMPTY)
                else:
                    n = new_number
                    if new_number > 2048:
                        c = 2048
                    else:
                        c = new_number

                    self.gridCells[i][j].configure(text=str(n), bg=BACKGROUND_COLOUR_DICT[c], fg=CELL_COLOUR_DICT[c])
        self.update_idletasks()

gameUI = GameUI()
