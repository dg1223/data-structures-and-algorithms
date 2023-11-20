class Vertex:
	def __init__(self, value):
		self.value = value
		self.edges = {}

	def add_edge(self, vertex, weight=0):
		self.edges[vertex] = weight

	def get_edges(self):
		return list(self.edges.keys())

class DFS:
	def __init__(self, directed=False):
		self.graph_dict = {}
		self.directed = directed

	def add_vertex(self, vertex):
		self.graph_dict[vertex.value] = vertex

	def add_edge(self, from_vertex, to_vertex):
		self.graph_dict[from_vertex.value].add_edge(to_vertex.value)
		if not self.directed:
			self.graph_dict[to_vertex.value].add_edge(from_vertex.value)

	# DFS algorithm
	def find_path(self, start_vertex, target_vertex):
		start = [start_vertex]
		seen = set()
		while start:
			current_vertex = start.pop()
			print(f"Visiting {current_vertex}")
			seen.add(current_vertex)
			if current_vertex == target_vertex:
				return True
			else:
				next_vertices = self.graph_dict[current_vertex].get_edges()
				next_vertices = [item for item in next_vertices if item not in seen]
				start += next_vertices
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
	target = 'D'
	path = railway.find_path(start, target)

	if path:
		print(f"Path exists from {start} to {target}")
	else:
		print(f"No path exists from {start} to {target}")