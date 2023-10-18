# Logic for the game running.
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

    # Returns the current score.
    def return_score(self) -> int:
        return self.grid.get_score()
    
    # Prints the highest tile achieved currently.
    def print_highest_tile(self) -> None:
        print("Highest tile: ", self.grid.get_highest_tile())

    # Returns the highest tile achieved currently.
    def return_highest_tile(self) -> int:
        return self.grid.get_highest_tile()

    # Returns a boolean for whether the game is over or not.
    def is_game_over(self) -> bool:
        if (self.grid.get_current_state() == 'LOST'):
            return True
        return False
            #self.gameOver = True

    # Used for testing the AI in the console.
    def run_AI_game(self) -> None:
        print("AI plays 2048.\n")
        moveTimes = []
        while (self.is_game_over() != True):
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
            moveTimes.append(time.time() - start)
            print("avg: ",sum(moveTimes)/len(moveTimes))

        print("\nGAME OVER.")
        f = open("data.txt", "a")
        row_item = [str(self.return_score()), str(self.return_highest_tile())]
        data = "{}{:>20}".format(row_item[0], row_item[1])
        f.write("\n"+data)
        f.close()
        self.print_score()
        self.print_highest_tile()

if __name__ == '__main__':
    # For the AI plays version of the game.
    for i in range(10):
        game = Game()
        game.run_AI_game()

    
