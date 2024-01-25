# matrix should be given as input
#matrix = [ ['.' for _ in range(MAX_ROW)] for _ in range(MAX_COL)]

class Solution:
	def __init__(self, matrix, MAX_ROW=20, MAX_COL=20, visited=None):
		self.MAX_ROW = MAX_ROW
		self.MAX_COL = MAX_COL
		self.visited = [ [False for _ in range(MAX_ROW)] for _ in range(MAX_COL) ]
		self.DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
		self.matrix = matrix

	def is_valid(self, child_i, child_j):
		return child_i >= 0 and child_i < len(self.matrix) and child_j >= 0 and child_j < len(self.matrix[0])

	def dfs(self, source_i, source_j):
		# Perform your task here
		print(f"{source_i = }, {source_j = }")

		self.visited[source_i][source_j] = True

		for direction in self.DIRECTIONS:
			child_i = source_i + direction[0]
			child_j = source_j + direction[1]

			if self.is_valid(child_i, child_j) and not self.visited[child_i][child_j]:
				self.dfs(child_i, child_j)
