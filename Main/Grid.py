# Logic for the grid functions.

import random
import numpy as np
import math

class Grid:

	def __init__(self) -> None:
		self.matrix = [] # Declaring an empty list.
		for i in range(4): # Giving the matrix the shape it should have.
			self.matrix.append([0] * 4)

		self.weights = [[2048, 1024, 512, 256], # Weighted matrix used for the AI scoring. (Snake)
		   				[16,   32,   64,  128],
		   				[8,    4,    2,    -2],
		   				[-32, -16,  -8,    -4]]

		
	# Adds a random 2 or 4 to start the game.
	def add_first_tile(self) -> None:
		self.add_random_tile()

	# Creates a clone of the matrix and returns the object.
	def clone(self) -> object:
		copy = Grid()
		copy.matrix = np.copy(self.matrix)
		return copy

	# Specific moving, used for AI. Returns whether the move resulted in a different grid.
	def move(self, direction) -> bool:
		changed = False
		if (direction == 'up'):
			changed = self.move_up()
		if (direction == 'right'):
			changed = self.move_right()
		if (direction == 'down'):
			changed = self.move_down()
		if (direction == 'left'):
			changed = self.move_left()

		if (changed == True): # Checks if move was able to be made.
			self.add_random_tile()
			return changed
		return changed

	def get_highest_tile(self) -> int:
		maxTile= 0
		for i in range(4):
			for n in range(4):
				if (self.matrix[i][n] > maxTile):
					maxTile = self.matrix[i][n]
		return maxTile
	
	def get_4highest_tiles(self) -> list:
		maxTiles = []
		flattenedMatrix = sorted(list(np.array(self.matrix).flatten()))
		for i in range(1, 5):
			maxTiles.append(flattenedMatrix[-i])
		return maxTiles

	# Returns the current score.
	def get_score(self) -> int:
		score = 0
		for i in range(4):
			for n in range(4):
				score += self.matrix[i][n]
		return score

	# Returns the AI score of the current grid.
	def get_AI_score(self) -> int: 
		score = 0
		penalty = 0
		matrixWeight = 2.5
		emptySqauresWeight = 1.3
		highestTileWeight = 2.2
		smoothnessWeight = 1.5

		# Monotonicity heuristic. Each cell is weighted to ensure the AI makes the best moves.
		for i in range(4):
			for n in range(4):
				score += (self.weights[i][n] * self.matrix[i][n]) * matrixWeight

		# More squares available means more score. More important as game goes on.
		score +=  len(self.get_empty_spots()) * math.log(self.get_score()) * emptySqauresWeight

		# Gives a boost to the score if the highest tile is in the correct spot, otherwise it penalises.
		if (self.get_highest_tile() == self.matrix[0][0]):
			score += self.get_highest_tile() * highestTileWeight
		else:
			penalty += self.get_highest_tile() * highestTileWeight

		# Smoothness heuristic. Penalises the score when the grid does not have matching tiles neighbouring each other.
		# Directions relative to tile. Right, Left, Up, Down.
		directions = [[1, 0], [-1 , 0], [0, 1], [0, -1]] 
		# For each tile.
		for y in range(4):
			for x in range(4):
				# If tile is not 0.
				if (self.matrix[y][x] != 0):
					# For each direction check whether it is in bounds.
					for i in range(4):
						position = [y + directions[i][1], x + directions[i][0]]
						if (self.is_in_bounds(position)):
							neighbour = self.matrix[position[0]][position[1]]
							# If neighbour is not 0.
							if (neighbour != 0):
								# If neighbours are equal add 0 to the penalty, if not add their difference to the penalty.
								penalty += abs(neighbour - self.matrix[y][x]) * smoothnessWeight

		return score - penalty
	
		########################################################

		# Heuristics I tried but ended up leaving out since they did not seem to help. They may have end up helping with more weight testing however.

		# stuckPenalty = 1.7

		# # Makes moves that merge the highest tile happen more often.
		# score += self.get_highest_tile() * highestTileWeight

		# # Gives a boost to the score if the top 4 tiles are in the correct spot, otherwise it penalises.
		# topFour = self.get_4highest_tiles()
		# for i in range(4):
		# 	if (self.matrix[0][i] == topFour[i]):
		# 		score += topFour[i] * highestTileWeight
		# 	else:
		# 		penalty += topFour[i] * highestTileWeight

		# # Small values getting stuck in top right corner penalises.
		# topFour = self.get_4highest_tiles()
		# if (self.matrix[0][3] != topFour[3]):
		# 	penalty += self.get_highest_tile() * stuckPenalty

	# Checks whether a position is in bounds.
	def is_in_bounds(self, position) -> bool:
		if (0 <= position[0] < 4 and 0 <= position[1] < 4):
			return True
		else:
			return False

	# Insert a specific tile, used for AI.
	def insert_tile(self, position, value) -> None:
		self.matrix[position[0]][position[1]] = value

	# Returns all available cells, used for AI.
	def get_empty_spots(self) -> list:
		cells = []																	
		for i in range(4):
			for n in range(4):
				if (self.matrix[i][n] == 0):
					cells.append([i, n])
		return cells

	# function to add a new 2 or 4 in grid at any random empty cell
	def add_random_tile(self) -> None:
		# Getting a 4 has a 10% chance
		if random.random() < 0.9:
			number = 2
		else:
			number = 4

		# choosing a random index for row and column.
		r = random.randint(0, 3)
		c = random.randint(0, 3)

		# while loop will break as the random cell chosen will be empty (or contains zero)
		while(self.matrix[r][c] != 0):
			r = random.randint(0, 3)
			c = random.randint(0, 3)

		# we will place a 2 or 4 at that empty random cell.
		self.matrix[r][c] = number

	# function to get the current state of game
	def get_current_state(self) -> str:

		# if we are still left with at least one empty cell game is not yet over
		for i in range(4):
			for j in range(4):
				if(self.matrix[i][j]== 0):
					return 'GAME NOT OVER'

		# or if no cell is empty now but if after any move left, right, up or down, if any two cells
		# gets merged and create an empty cell then also game is not yet over
		for i in range(3):
			for j in range(3):
				if(self.matrix[i][j]== self.matrix[i + 1][j] or self.matrix[i][j]== self.matrix[i][j + 1]):
					return 'GAME NOT OVER'

		for j in range(3):
			if(self.matrix[3][j]== self.matrix[3][j + 1]):
				return 'GAME NOT OVER'

		for i in range(3):
			if(self.matrix[i][3]== self.matrix[i + 1][3]):
				return 'GAME NOT OVER'

		# else we have lost the game
		return 'LOST'

	# all the functions defined below are for left swap initially.

	# function to compress the grid after every step before and after merging cells.
	def compress(self) -> bool:
		# bool variable to determine any change happened or not
		changed = False
		# empty grid
		new_mat = []
		# with all cells empty
		for i in range(4):
			new_mat.append([0] * 4)
		# here we will shift entries of each cell to it's extreme left row by row
		for i in range(4):
			pos = 0
			# loop to traverse each column in respective row
			for j in range(4):
				if(self.matrix[i][j] != 0):
					# if cell is non empty then we will shift it's number to previous empty cell in that row denoted by pos variable
					new_mat[i][pos] = self.matrix[i][j]
					if(j != pos):
						changed = True
					pos += 1
		self.matrix = new_mat
		# returning the flag variable.
		return changed

	# function to merge the cells in matrix after compressing
	def merge(self) -> bool:
		changed = False
		for i in range(4):
			for j in range(3):
				# if current cell has same value as next cell in the row and they are non empty then
				if(self.matrix[i][j] == self.matrix[i][j + 1] and self.matrix[i][j] != 0):
					# double current cell value and empty the next cell
					self.matrix[i][j] = self.matrix[i][j] * 2
					self.matrix[i][j + 1] = 0
					# make bool variable True indicating the new grid after merging is different.
					changed = True
		return changed

	# function to reverse the matrix means reversing the content of each row (reversing the sequence)
	def reverse(self) -> None:
		new_mat =[]
		for i in range(4):
			new_mat.append([])
			for j in range(4):
				new_mat[i].append(self.matrix[i][3 - j])
		self.matrix = new_mat

	# function to get the transpose of matrix means interchanging rows and column
	def transpose(self) -> None:
		new_mat = []
		for i in range(4):
			new_mat.append([])
			for j in range(4):
				new_mat[i].append(self.matrix[j][i])
		self.matrix = new_mat

	# function to update the matrix if we move / swipe left
	def move_left(self) -> bool:
		# first compress the grid
		changed1 = self.compress()
		# then merge the cells.
		changed2 = self.merge()
		changed = changed1 or changed2
		# again compress after merging.
		temp = self.compress()
		# return bool changed telling whether the grid is same or different
		return changed

	# function to update the matrix if we move / swipe right
	def move_right(self) -> bool:
		# to move right we just reverse the matrix
		self.reverse()
		# then move left
		changed = self.move_left()
		# then again reverse matrix will give us desired result
		self.reverse()
		return changed

	# function to update the matrix if we move / swipe up
	def move_up(self) -> bool:
		# to move up we just take transpose of matrix
		self.transpose()
		# then move left (calling all included functions)
		changed = self.move_left()
		# again take transpose will give desired results
		self.transpose()
		return changed

	# function to update the matrix if we move / swipe down
	def move_down(self) -> bool:
		# to move down we take transpose
		self.transpose()
		# move right and then again
		changed = self.move_right()
		# take transpose will give desired results.
		self.transpose()
		return changed
