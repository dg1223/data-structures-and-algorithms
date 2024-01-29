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
		self.graph = {}
		self.directed = directed

	def add_vertex(self, vertex):
		self.graph[vertex.value] = vertex

	def add_edge(self, from_vertex, to_vertex):
		self.graph[from_vertex.value].add_edge(to_vertex.value)
		if not self.directed:
			self.graph[to_vertex.value].add_edge(from_vertex.value)

	# DFS algorithm
	def find_path(self, start_vertex, target_vertex):
		start = [start_vertex]
		seen = set()
		while start:
			current_vertex = start.pop()
			print(f"Visiting {current_vertex}")
			'''
			Just by moving the following instruction after the if statement,
			we can neutralize a lot of execution footprint if we consider a
			large-scale system with 1 billion users.
			A typical instruction takes 25 nanoseconds. 10^9 i.e. 1 billion
			of these instructions can take 25 seconds (10^9 ns = 1 second)
			So, for every 1 billion hit, we save 25 seconds of server use
			and reduce carbon footprint or energy consumption.
			'''
			#seen.add(current_vertex)
			if current_vertex == target_vertex:
				return True

			seen.add(current_vertex)
			next_vertices = self.graph[current_vertex].get_edges()
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