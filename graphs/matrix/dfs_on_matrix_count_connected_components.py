class DFS:
	def __init__(self, matrix, MAX_ROW=20, MAX_COL=20):
		self.MAX_ROW = MAX_ROW
		self.MAX_COL = MAX_COL
		self.matrix = matrix
		self.length_x = len(self.matrix)
		self.length_y = len(self.matrix[0])
		self.num_single_cell = 0
		self.visited = [ [False for _ in range(MAX_ROW)] for _ in range(MAX_COL) ]
		self.DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]		

	def is_valid(self, child_i, child_j):
		return child_i >= 0 and child_i < self.length_x and child_j >= 0 and child_j < self.length_y

	def dfs(self, source_i, source_j):
		## Perform your task here
		#print(f"({source_i}, {source_j})")
		#print(self.matrix[source_i][source_j])

		self.visited[source_i][source_j] = True

		# find cells that act as single nodes
		# we ignore isoated cells as they are not connected
		self.is_cell_single(source_i, source_j)

		for direction in self.DIRECTIONS:
			child_i = source_i + direction[0]
			child_j = source_j + direction[1]

			if self.is_valid(child_i, child_j) and not self.visited[child_i][child_j] and self.matrix[child_i][child_j] != '#':
				self.dfs(child_i, child_j)

	def is_cell_single(self, source_i, source_j):
		isolated_cell = True
		for direction in self.DIRECTIONS:
			child_i = source_i + direction[0]
			child_j = source_j + direction[1]

			if self.is_valid(child_i, child_j) and self.matrix[child_i][child_j] == '.':
				isolated_cell = False				
				break

		if isolated_cell:
			self.num_single_cell += 1

	def count_components(self):
		num_components = 0
		for row in range(self.length_x):
			for col in range(self.length_y):				
				if not self.visited[row][col] and self.matrix[row][col] != '#':
					self.dfs(row, col)
					num_components += 1

		return num_components - self.num_single_cell

'''
input matrix

A dot '.' represents a room and '#' represents a wall.
You can walk left, right, up, and down through the rooms. 
You can't pass through walls.

########
#..#...#
####.#.#
#..#...#
########

'''

matrix_1 = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '#', '.', '.', '.', '#'],
	['#', '#', '#', '#', '.', '#', '.', '#'],
	['#', '.', '.', '#', '.', '.', '.', '#'],
	['#', '#', '#', '#', '#', '#', '#', '#'],
]

dfs_on_matrix = DFS(matrix_1)
connected_components = dfs_on_matrix.count_components()
print(f"{connected_components = }")


'''
input matrix

A dot '.' represents a room and '#' represents a wall.
You can walk left, right, up, and down through the rooms. 
You can't pass through walls.

.#.#####
.#.###..
#..#...#
#.##....
..##.###
#.#.##.#
   ^  ^
   |  |
isolated cells -> components that are not connected

'''

matrix_2 = [
    ['.', '#', '.', '#', '#', '#', '#', '#'],
    ['.', '#', '.', '#', '#', '#', '.', '.'],
	['#', '.', '.', '#', '.', '.', '.', '#'],
	['#', '.', '#', '#', '.', '.', '.', '.'],
	['.', '.', '#', '#', '.', '#', '#', '#'],
	['#', '.', '#', '.', '#', '#', '.', '#']
]

dfs_on_matrix = DFS(matrix_2)
connected_components = dfs_on_matrix.count_components()
print(f"{connected_components = }")