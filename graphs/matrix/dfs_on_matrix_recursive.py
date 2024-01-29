class DFS:
	def __init__(self, matrix, MAX_ROW=20, MAX_COL=20):
		self.MAX_ROW = MAX_ROW
		self.MAX_COL = MAX_COL
		self.visited = [ [False for _ in range(MAX_ROW)] for _ in range(MAX_COL) ]
		self.DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	def is_valid(self, child_i, child_j):
		return child_i >= 0 and child_i < len(matrix) and child_j >= 0 and child_j < len(matrix[0])

	def dfs(self, source_i, source_j):
		# Perform your task here
		print(f"({source_i}, {source_j})")
		print(matrix[source_i][source_j])

		self.visited[source_i][source_j] = True

		for direction in self.DIRECTIONS:
			child_i = source_i + direction[0]
			child_j = source_j + direction[1]

			if self.is_valid(child_i, child_j) and not self.visited[child_i][child_j]:
				self.dfs(child_i, child_j)

'''
input matrix

A B C D
E F G H
I J K L

'''

matrix = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L']
]

dfs_traversal_on_matrix = DFS(matrix)
dfs_traversal_on_matrix.dfs(0, 0)

'''
DFS traversal
A -> B -> C -> D -> H -> G -> F -> E -> I -> J -> K -> L

    1
 (0, 0) (0, 1) (0, 2) (0, 3)
        2      3      4
    A ---> B ---> C ---> D
					   5 |
					     ⌄

 (1, 0) (1, 1) (1, 2) (1, 3)
        8      7      6
    E <--- F <--- G <--- H
  9 |
    ⌄

 (2, 0) (2, 1) (2, 2) (2, 3)
       10     11     12
    I ---> J ---> K ---> L

'''