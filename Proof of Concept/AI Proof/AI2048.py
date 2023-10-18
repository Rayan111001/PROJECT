from Grid import Grid
from AI import AI
import time

class Game:

    # Initializes the grid and variables for the game.
    def __init__(self) -> None:
        self.grid = Grid()
        self.ai = AI()
        self.gameOver = False
        self.depth = 4
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

    # Runs the game where the AI is playing.
    def run_AI_game(self) -> None:
        print("AI plays 2048.\n")
        moveTimes = []
        while (self.gameOver != True):
            start = time.time()
            print("\n")
            self.print_score()
            self.print_grid()
            print("\n")

            # If for whatever reason the best move results in no grid change, go through all moves until one makes a change.
            if (self.grid.move(self.ai.get_best_move(self.grid, self.depth)) == False):
                for i in self.moves:
                    if (self.grid.move(i) != False):
                        break
            #print(time.time() - start)
            self.is_game_over()
            moveTimes.append(time.time() - start)
            print("avg: ",sum(moveTimes)/len(moveTimes))
        print("\nGAME OVER.")
        self.print_score()
        self.print_highest_tile()

# Driver code
if __name__ == '__main__':
    
    # For playing the game normally.
    #game = Game('player')

    # For the AI plays version of the game.
    game = Game()
    game.run_AI_game()

    
