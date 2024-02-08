class DFS:
	def __init__(self, matrix):		
		self.rows = len(matrix)
		self.cols = len(matrix[0])
		self.visited = [ [False] * self.cols for _ in range(self.rows) ]
		self.DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
		self.matrix = matrix

	def is_valid(self, child_i, child_j):
		return child_i >= 0 and child_i < self.rows and child_j >= 0 and child_j < self.cols

	def dfs(self, source_i, source_j):
		## Perform your task here
		#print(f"({source_i}, {source_j})")

		self.visited[source_i][source_j] = True

		for direction in self.DIRECTIONS:
			child_i = source_i + direction[0]
			child_j = source_j + direction[1]

			if self.is_valid(child_i, child_j) and not self.visited[child_i][child_j] and self.matrix[child_i][child_j] != '#':
				self.dfs(child_i, child_j)

	def count_components(self):
		num_components = 0
		for row in range(self.rows):
			for col in range(self.cols):				
				if not self.visited[row][col] and self.matrix[row][col] != '#':
					self.dfs(row, col)
					num_components += 1

		return num_components

'''
input matrix

A B C D
E F G H
I J K L

'''

matrix_1 = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L']
]

dfs_on_matrix = DFS(matrix_1)
components = dfs_on_matrix.count_components()
print(f"{components = }")


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

matrix_2 = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '#', '.', '.', '.', '#'],
	['#', '#', '#', '#', '.', '#', '.', '#'],
	['#', '.', '.', '#', '.', '.', '.', '#'],
	['#', '#', '#', '#', '#', '#', '#', '#'],
]

dfs_on_matrix = DFS(matrix_2)
components = dfs_on_matrix.count_components()
print(f"{components = }")


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

'''

matrix_3 = [
    ['.', '#', '.', '#', '#', '#', '#', '#'],
    ['.', '#', '.', '#', '#', '#', '.', '.'],
	['#', '.', '.', '#', '.', '.', '.', '#'],
	['#', '.', '#', '#', '.', '.', '.', '.'],
	['.', '.', '#', '#', '.', '#', '#', '#'],
	['#', '.', '#', '.', '#', '#', '.', '#']
]

dfs_on_matrix = DFS(matrix_3)
components = dfs_on_matrix.count_components()
print(f"{components = }")