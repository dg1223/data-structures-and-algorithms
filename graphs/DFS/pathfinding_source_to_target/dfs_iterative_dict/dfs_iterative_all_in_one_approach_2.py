# Pre-order DFS

class Vertex:
	def __init__(self, value):
		self.value = value
		self.edges = {}

	def add_edge(self, value, weight=0):
		self.edges[value] = weight

	def get_edges(self):
		return list(self.edges.keys())

class DFS:
	def __init__(self, directed=False):
		self.graph = {}
		self.directed = directed

	def add_vertex(self, vertex):
		self.graph[vertex.value] = vertex

	def add_edge(self, from_vertex, to_vertex):
		self.graph[from_vertex.value].add_edge(to_vertex.value)
		if not self.directed:
			self.graph[to_vertex.value].add_edge(from_vertex.value)

	def find_path(self, start, target):
		if not self.graph:
			print("Graph is empty")
			return False

		if start == target:
			print(f"Visiting {start}")	
			return True

		'''
		For undirected graphs, we need to keep track of already 
		visited vertices. Otherwise, recursion will run infinitely
		on a previously visited neighbour.
		'''
		seen = set()

		return self.dfs_recursive(start, target, seen)

	def dfs_recursive(self, start, target, seen):
		print(f"Visiting {start}")	
		if start == target:
			return True
		seen.add(start)
		for neighbour in self.graph[start].get_edges():
			if neighbour not in seen:				
				'''
				The function returns immediately after checking the 
				first neighboUr, which leads to premature termination 
				of the search. Instead, the function should explore 
				all neighbors and only return True if any of them 
				leads to the target.
				'''
				#return self.dfs_recursive(neighbour, target, seen)
				if self.dfs_recursive(neighbour, target, seen):
					return True
		return False


if __name__ == "__main__":
	railway = DFS()

	A = Vertex('A')
	B = Vertex('B')
	C = Vertex('C')
	D = Vertex('D')
	E = Vertex('E')
	F = Vertex('F')
	G = Vertex('G')

	railway.add_vertex(A)
	railway.add_vertex(B)
	railway.add_vertex(C)
	railway.add_vertex(D)
	railway.add_vertex(E)
	railway.add_vertex(F)
	railway.add_vertex(G)

	railway.add_edge(A, B)
	railway.add_edge(A, C)
	railway.add_edge(B, D)
	railway.add_edge(B, E)
	railway.add_edge(C, F)
	railway.add_edge(C, G)

	start = 'A'
	target = 'G'
	path = railway.find_path(start, target)

	if path:
		print(f"Path exists from {start} to {target}")
	else:
		print(f"No path exists from {start} to {target}")