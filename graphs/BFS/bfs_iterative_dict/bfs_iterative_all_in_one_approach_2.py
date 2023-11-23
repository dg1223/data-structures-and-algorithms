from collections import deque

class Vertex:
	def __init__(self, value):
		self.value = value
		self.edges = {}

	def add_edge(self, value, weight=0):
		self.edges[value] = weight

	def get_edges(self):
		return list(self.edges.keys())

class BFS:
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
			return True

		path = deque()
		path.append(start)
		seen = set()		
		while path:
			current_vertex = path.pop()
			if current_vertex not in seen:
				print(f"Visiting {current_vertex}")
				seen.add(start)
			for neighbour in self.graph[current_vertex].get_edges():				
				if neighbour not in seen:					
					print(f"Visiting {neighbour}")
					if neighbour == target:					
						return True
					seen.add(neighbour)
					path.appendleft(neighbour)
		return False

if __name__ == "__main__":
	railway = BFS()

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