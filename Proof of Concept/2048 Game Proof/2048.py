from Grid import Grid

class Game:

    # Initializes the grid and variables for the game.
    def __init__(self) -> None:
        self.grid = Grid()
        self.gameOver = False
        self.moves = ['up', 'right', 'down', 'left']
        self.grid.add_first_tile()

    # Prints the current grid layout.
    def print_grid(self) -> None:
        for i in range(4):
            print(self.grid.matrix[i])

    # Prints the current score.
    def print_score(self) -> None:
        print("Score: ", self.grid.get_score())
    
    # Prints the highest tile achieved currently.
    def print_highest_tile(self) -> None:
        print("Highest tile: ", self.grid.get_highest_tile())

    # Returns a boolean for whether the game is over or not.
    def is_game_over(self) -> bool:
        if (self.grid.get_current_state() == 'LOST'):
            self.gameOver = True

    # Runs the game for if a player is playing.
    def run_player_game(self) -> None:
        print("Player plays 2048.\n")
        print("""Controls:
        w: up
        a: left
        s: down
        d: right""")

        while (self.gameOver != True):
            print("\n")
            self.print_score()
            self.print_grid()
            print("\n")
            playerInput = input("Enter a move: ")
            if (playerInput == 'w'):
                self.grid.move('up')
            elif (playerInput == 'a'):
                self.grid.move('left')
            elif (playerInput == 's'):
                self.grid.move('down')
            elif (playerInput == 'd'):
                self.grid.move('right')
            else:
                print("Invalid key press.")
            self.is_game_over()
        print("\nGAME OVER.")
        self.print_score()
        self.print_highest_tile()

# Driver code
if __name__ == '__main__':
    game = Game()
    game.run_player_game()

    
