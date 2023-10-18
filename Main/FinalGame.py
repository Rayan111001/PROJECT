# Final combined code

import tkinter as tk
from AI2048 import Game

class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("AI 2048")
        self.geometry("800x900")

        #Create a frame and assign it to a container
        container = tk.Frame(self, height=400, width=600)
        #The region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        #Configuring the location of the container in the grid
        container.grid_rowconfigure(0, weight=1) #non zero weight allows for container to be scaled when window is larger than widgets
        container.grid_columnconfigure(0, weight=1)

        #Dictionary of frames
        self.frames = {}
        #Components of dictionary is the different frames that exist
        for F in (MainPage, PlayPage, GameUI):  #List of different pages
            frame = F(container, self)

            #This window class acts as root window for all the frames
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #Method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        #Raises current frame to the top
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Menu")
        label.pack(padx=10, pady=10)

        #Switch window button calls show_frame method as lambda function
        switch_window_playPage_btn = tk.Button(self, text="Play Game", command=lambda: controller.show_frame(PlayPage), activebackground="red", bg= "#e88504", width=40)
        switch_window_playPage_btn.pack(pady=100)
        switch_window_aiplayPage_btn = tk.Button(self, text="AI Play", command=lambda: controller.show_frame(GameUI), activebackground="red", bg= "#e88504", width=40)
        switch_window_aiplayPage_btn.pack()
        quit_btn = tk.Button(self, text="Quit", command=lambda: exit(), activebackground="red", bg= "#e88504", width=40)
        quit_btn.pack(pady=100)

class GameUI(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.game = Game()

        self.SIZE = 500
        self.GRID_PADDING = 10
        self.BACKGROUND_COLOUR_GAME = "#92877d"
        self.BACKGROUND_COLOUR_CELL_EMPTY = "#bebebe"
        self.BACKGROUND_COLOUR_DICT = {  2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                                    32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                                    512:"#edc850", 1024:"#edc53f", 2048:"#edc22e"}
        self.CELL_COLOUR_DICT = {2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                            32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                            512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2"}
        self.FONT = ("Verdana", 40, "bold")
        self.optimalToggle = False

        # Switch window button calls show_frame method as lambda function
        self.switch_window_playPage_btn = tk.Button(self, text="Back to menu", command=lambda: controller.show_frame(MainPage),activebackground="red", bg= "#e88504")
        self.switch_window_playPage_btn.pack(side="bottom", fill=tk.X)

        # Runs the game, if clicked again resets.
        self.run_AI_btn = tk.Button(self, text="Run", command=lambda: self.start_game(),activebackground="red", bg= "#e88504")
        self.run_AI_btn.pack(side="top", fill=tk.X)

        # Speed of AI buttons.
        speedFrame = tk.Frame(self)
        speedFrame.pack(side="top")

        self.normal_btn = tk.Button(self, text="Normal", command=lambda: self.change_depth(5), activebackground="red", bg= "#e88504", padx=20)
        self.normal_btn.pack(in_=speedFrame, side="left")

        self.fast_btn = tk.Button(self, text="Fast", command=lambda: self.change_depth(4) ,activebackground="red", bg= "#e88504", padx=30)
        self.fast_btn.pack(in_=speedFrame, side="left")

        self.optimal_btn = tk.Button(self, text="Optimal", command=lambda: self.change_depth("optimal") ,activebackground="red", bg= "#e88504", padx=30)
        self.optimal_btn.pack(in_=speedFrame, side="left")

        speedInfoLabel = tk.Label(self, text="Speed changes depth. (Normal = 5, Fast = 4, Optimal = Auto)", font=("Verdana",10))
        speedInfoLabel.pack(side="top")

        # Real time score.
        self.scoreNameLabel = tk.Label(self, text="Score:", font=("Verdana", 15))
        self.scoreNameLabel.pack()
        self.scoreLabel = tk.Label(self, text="0", font = ("Verdana", 15))
        self.scoreLabel.pack()

        # Real time highest tile.
        self.highestTileNameLabel = tk.Label(self, text="Highest Tile:", font=("Verdana", 15))
        self.highestTileNameLabel.pack()
        self.highestTileLabel = tk.Label(self, text="0", font=("Verdana", 15))
        self.highestTileLabel.pack()

        self.background = tk.Frame(self, bg=self.BACKGROUND_COLOUR_GAME, width=self.SIZE, height=self.SIZE)

        # Game over label, not placed until the AI loses.
        self.gameOverLabel = tk.Label(self, text="GAME OVER", font=("Verdana", 40), fg="#302A2A", bg=self.BACKGROUND_COLOUR_GAME)
        
        self.gridCells = []
        self.init_grid()

    def change_depth(self, depth):
        if (depth == 'optimal'):
            self.optimalToggle = True
        else:
            self.optimalToggle = False
            self.game.depth = depth

    def start_game(self):
        self.gameOverLabel.place_forget()
        self.game = Game()
        self.game.depth = 5
        self.update_grid_cells()
        self.run_game()

    def run_game(self):
        while (True):
            if (self.optimalToggle):
                if (len(self.game.grid.get_empty_spots()) < 7): 
                    self.game.depth = 5
                else:
                    self.game.depth = 4

            if (self.game.grid.move(self.game.ai.get_best_move(self.game.grid, self.game.depth)) == False):
                for i in self.game.moves:
                    if (self.game.grid.move(i) != False):
                        break
            self.update_grid_cells()

            if (self.game.is_game_over()):

                # Code for writing results to the data file.
                # f = open("data.txt", "a")
                # row_item = [str(self.game.return_score()), str(self.game.return_highest_tile())]
                # data = "{}{:>20}".format(row_item[0], row_item[1])
                # f.write("\n"+data)
                # f.close()
                
                self.game_over_screen()
                break
            
            self.update()

    def game_over_screen(self):
        self.gameOverLabel.place(in_=self.background, relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.update()

    def init_grid(self):
        self.background.pack()

        for i in range(4):
            grid_row = []
            for j in range(4):

                cell = tk.Frame(self.background, bg=self.BACKGROUND_COLOUR_CELL_EMPTY, width=self.SIZE/4, height=self.SIZE/4)
                cell.grid(row=i, column=j, padx=self.GRID_PADDING, pady=self.GRID_PADDING)
                t = tk.Label(master=cell, text="", bg=self.BACKGROUND_COLOUR_CELL_EMPTY, justify=tk.CENTER, font=self.FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.gridCells.append(grid_row)

    def update_grid_cells(self):
        for i in range(4):
            for j in range(4):
                new_number = int(self.game.grid.matrix[i][j])
                if new_number == 0:
                    self.gridCells[i][j].configure(text="", bg=self.BACKGROUND_COLOUR_CELL_EMPTY)
                else:
                    n = new_number
                    if new_number > 2048:
                        c = 2048
                    else:
                        c = new_number

                    self.gridCells[i][j].configure(text=str(n), bg=self.BACKGROUND_COLOUR_DICT[c], fg=self.CELL_COLOUR_DICT[c])
        self.update_score()
        self.update_highest_tile()
        self.update_idletasks()
    
    def update_score(self):
        self.scoreLabel.configure(text=self.game.return_score())

    def update_highest_tile(self):
        self.highestTileLabel.configure(text=self.game.return_highest_tile())

class PlayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.game = Game()

        self.SIZE = 500
        self.GRID_PADDING = 10
        self.BACKGROUND_COLOUR_GAME = "#92877d"
        self.BACKGROUND_COLOUR_CELL_EMPTY = "#bebebe"
        self.BACKGROUND_COLOUR_DICT = {  2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                                    32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                                    512:"#edc850", 1024:"#edc53f", 2048:"#edc22e"}
        self.CELL_COLOUR_DICT = {2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                            32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                            512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2"}
        self.FONT = ("Verdana", 40, "bold")

        # Switch window button calls show_frame method as lambda function
        self.switch_window_playPage_btn = tk.Button(self, text="Back to menu", command=lambda: controller.show_frame(MainPage),activebackground="red", bg= "#e88504")
        self.switch_window_playPage_btn.pack(side="bottom", fill=tk.X)

        # Runs the game, if clicked again resets.
        self.run_AI_btn = tk.Button(self, text="Play", command=lambda: self.start_game(),activebackground="red", bg= "#e88504")
        self.run_AI_btn.pack(side="top", fill=tk.X)

        InfoLabel = tk.Label(self, text="Use WASD or arrow keys to move!", font=("Verdana",10))
        InfoLabel.pack(side="top")

        # Real time score.
        self.scoreNameLabel = tk.Label(self, text="Score:", font=("Verdana", 15))
        self.scoreNameLabel.pack()
        self.scoreLabel = tk.Label(self, text="0", font = ("Verdana", 15))
        self.scoreLabel.pack()

        # Real time highest tile.
        self.highestTileNameLabel = tk.Label(self, text="Highest Tile:", font=("Verdana", 15))
        self.highestTileNameLabel.pack()
        self.highestTileLabel = tk.Label(self, text="0", font=("Verdana", 15))
        self.highestTileLabel.pack()

        self.background = tk.Frame(self, bg=self.BACKGROUND_COLOUR_GAME, width=self.SIZE, height=self.SIZE)

        # Game over label, not placed until the AI loses.
        self.gameOverLabel = tk.Label(self, text="GAME OVER", font=("Verdana", 40), fg="#302A2A", bg=self.BACKGROUND_COLOUR_GAME)

        # Waits for key presses.
        self.scoreLabel.bind_all("<Key>", self.move_game)
        
        self.gridCells = []
        self.init_grid()

    def move_game(self, event):
        if (event.keysym == "w" or event.keysym == "Up"):
            self.game.grid.move("up")
        if (event.keysym == "a" or event.keysym == "Left"):
            self.game.grid.move("left")
        if (event.keysym == "s" or event.keysym == "Down"):
            self.game.grid.move("down")
        if (event.keysym == "d" or event.keysym == "Right"):
            self.game.grid.move("right")

    def start_game(self):
        self.gameOverLabel.place_forget()
        self.game = Game()
        self.update_grid_cells()
        self.run_game()

    def run_game(self):
        while (True):
            self.update_grid_cells()

            if (self.game.is_game_over()):
                self.game_over_screen()
                break
            
            self.update()

    def game_over_screen(self):
        self.gameOverLabel.place(in_=self.background, relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.update()

    def init_grid(self):
        self.background.pack()

        for i in range(4):
            grid_row = []
            for j in range(4):

                cell = tk.Frame(self.background, bg=self.BACKGROUND_COLOUR_CELL_EMPTY, width=self.SIZE/4, height=self.SIZE/4)
                cell.grid(row=i, column=j, padx=self.GRID_PADDING, pady=self.GRID_PADDING)
                t = tk.Label(master=cell, text="", bg=self.BACKGROUND_COLOUR_CELL_EMPTY, justify=tk.CENTER, font=self.FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.gridCells.append(grid_row)

    def update_grid_cells(self):
        for i in range(4):
            for j in range(4):
                new_number = int(self.game.grid.matrix[i][j])
                if new_number == 0:
                    self.gridCells[i][j].configure(text="", bg=self.BACKGROUND_COLOUR_CELL_EMPTY)
                else:
                    n = new_number
                    if new_number > 2048:
                        c = 2048
                    else:
                        c = new_number

                    self.gridCells[i][j].configure(text=str(n), bg=self.BACKGROUND_COLOUR_DICT[c], fg=self.CELL_COLOUR_DICT[c])
        self.update_score()
        self.update_highest_tile()
        self.update_idletasks()
    
    def update_score(self):
        self.scoreLabel.configure(text=self.game.return_score())

    def update_highest_tile(self):
        self.highestTileLabel.configure(text=self.game.return_highest_tile())

if __name__ == "__main__":
    testObj = Windows()
    testObj.mainloop()
