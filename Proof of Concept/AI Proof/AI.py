# Research on expectimax implementation done from:
# https://github.com/ovolve/2048-AI
# https://github.com/Lesaun/2048-expectimax-ai
# https://github.com/Wahab16/2048-Game-Using-Expectimax

# AI.py to be imported into the 'AI plays' version of the game.

class AI():

    def __init__(self) -> None:
        self.moves = ['up', 'right', 'down', 'left']

    def get_best_move(self, matrix, depth) -> str: # Returns the best move the AI can take.
        score = 0
        bestMove = None

        for i in self.moves:
            newMatrix = matrix.clone()

            if (newMatrix.move(i) == False): # If no move made return to top.
                continue

            newScore = self.expectimax(newMatrix, depth - 1, "computer")

            if (newScore > score):
                bestMove = i
                score = newScore

        return bestMove

    def expectimax(self, matrix, depth, agent) -> float:
            
        if (depth == 0): 
            return matrix.get_AI_score()

        elif(agent == "player"):
            score = 0
            for i in self.moves:
                newMatrix = matrix.clone()
                nextLevel = newMatrix.move(i) # Try each possible move.

                if (nextLevel == False): # If the move isn't possible, skip the move.
                    continue

                newScore = self.expectimax(newMatrix, depth - 1, "computer")

                if (newScore > score):
                    score = newScore

            return score

        elif (agent == "computer"):
            score = 0
            cells = matrix.get_empty_spots()
            totalCells = len(cells)

            for i in range(totalCells):
                newMatrix = matrix.clone()
                newMatrix.insert_tile(cells[i], 4) # Testing each empty cell with a value of 4.
                newScore = self.expectimax(newMatrix, depth - 1, "player")
                if (newScore == 0):
                    score += 0
                else:
                    score += (0.1 * newScore) # If the score is good, it's added but multiplied by 0.1 as that is the chance for a 4 to occur.

                newMatrix = matrix.clone()
                newMatrix.insert_tile(cells[i], 2) # Testing each empty cell with a value of 2.
                newScore = self.expectimax(newMatrix, depth - 1, "player")
                if (newScore == 0):
                    score += 0
                else:
                    score += (0.9 * newScore) # If the score is good, it's added but multiplied by 0.9 as that is the chance for a 2 to occur.
            
            if (totalCells != 0):
                score /= totalCells
            else:
                score = 0
            return score