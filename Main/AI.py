# Logic for the AI playing the game
from multiprocessing import Pool

class AI():

    def __init__(self) -> None:
        self.moves = ['up', 'right', 'down', 'left']
        self.matrix = None
        self.depth = None
        self.cache = {}

    def get_best_move(self, matrix, depth) -> str: # Returns the best move the AI can take.
        score = 0
        bestMove = None
        self.matrix = matrix
        self.depth = depth

        if (self.depth <= 4):
            for i in self.moves:
                newMatrix = matrix.clone()

                if (newMatrix.move(i) == False): # If no move made return to top.
                    continue

                newScore = self.expectimax(newMatrix, depth - 1, "computer")

                if (newScore > score):
                    bestMove = i
                    score = newScore

            return bestMove

        else:
            with Pool(6) as pool:
                newScore = pool.map(self.startExpectimax, self.moves) # Multiprocesses each of the 4 moves.

            for i in range(len(newScore)): # Goes through the list of scores and their corresponding move.
                if (newScore[i][0] > score):
                    bestMove = newScore[i][1]
                    score = newScore[i][0]

            return bestMove
        
        ########################################

        # Caching code that I tried to use, it seemed that identical game states rarely happened so I left it out of the final code.

        # import json
        # state = json.dumps(matrix.matrix)

        # if state in self.cache: # If current state is in the cache use the move without searching tree.
        #     print("USED CACHE")
        #     return self.cache[state]

        # if (len(self.cache) > 1024): # If the cache is too large get rid of the oldest value.
        #     first = next(iter(self.cache))
        #     self.cache.pop(first)
        # self.cache[state] = bestMove

    def startExpectimax(self, moveDir):
        newMatrix = self.matrix.clone()
        if (newMatrix.move(moveDir) == False): # If no move made return to top.
                return 0, moveDir

        newScore = self.expectimax(newMatrix, self.depth - 1, "computer")
        
        return newScore, moveDir

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