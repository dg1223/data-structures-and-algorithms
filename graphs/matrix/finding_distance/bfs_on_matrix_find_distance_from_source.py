from collections import deque

'''
Generally used to find shortest path or distance 
from source to target
'''

class BFS:
	def __init__(self, matrix):
		self.rows = len(matrix)
		self.cols = len(matrix[0])
		self.visited = [ [False] * self.cols for _ in range(self.rows) ]
		self.distance = [ [-1] * self.cols for _ in range(self.rows) ]
		self.DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
		self.matrix = matrix

	# check corners and edges
	def is_valid(self, child_i, child_j):
		return child_i >= 0 and child_i < self.rows and child_j >= 0 and child_j < self.cols

	# inputs are index [x, y]
	def bfs(self, source_i, source_j):
		queue = deque()
		queue.appendleft((source_i, source_j))

		self.visited[source_i][source_j] = True
		self.distance[source_i][source_j] = 0

		while queue:
			first, second = queue.pop()

			#print(self.matrix[first][second])

			for direction in self.DIRECTIONS:
				child_i = first + direction[0]
				child_j = second + direction[1]
				#breakpoint()

				if self.is_valid(child_i, child_j) and not self.visited[child_i][child_j]:
					queue.appendleft((child_i, child_j))
					self.visited[child_i][child_j] = True
					self.distance[child_i][child_j] = self.distance[first][second] + 1

		print(f"Disntance of cells from source [0, 0] = {self.distance}")


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

bfs_traversal_on_matrix = BFS(matrix)
bfs_traversal_on_matrix.bfs(0, 0)
print(f"\nDistance of cell [2, 2] = {bfs_traversal_on_matrix.distance[2][2]}")
'''
BFS traversal
A -> B -> E -> C -> F -> I -> D -> G -> J -> H -> K -> L

    1
 (0, 0) (0, 1) (0, 2) (0, 3)
      2.1    3.1    5.1
    A ---> B ---> C ---> D
2.2 |  3.2 |  5.2 | 
    ⌄      ⌄      ⌄

 (1, 0) (1, 1) (1, 2) (1, 3)
                    7.1
    E      F      G ---> H
  4 |	 6 |  7.2 |    8 |
    ⌄      ⌄      ⌄      ⌄

(2, 0) (2, 1) (2, 2) (2, 3)

   I      J      K 	   L

'''
