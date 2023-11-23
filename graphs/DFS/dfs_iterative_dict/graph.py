class Graph:
	def __init__(self, directed=False):
		self.graph_dict = {}
		self.directed = directed

	def add_vertex(self, vertex):
		self.graph_dict[vertex.value] = vertex

	def add_edge(self, from_vertex, to_vertex):
		print(f"Adding edge from {from_vertex.value} to {to_vertex.value}")
		self.graph_dict[from_vertex.value].add_edge(to_vertex.value)
		if not self.directed:
			self.graph_dict[to_vertex.value].add_edge(from_vertex.value)

	'''    
	Depth-first search: We search through the entire depth of a branch
	before backtracking to the other branch
	'''
	def find_path(self, start_vertex, end_vertex):
		start = [start_vertex]
		seen = {}
		while start:
			current_vertex = start.pop()
			seen[current_vertex] = True
			print("Visiting " + current_vertex)
			if current_vertex == end_vertex:
				return True
			else:
				vertex = self.graph_dict[current_vertex]
				next_vertices = vertex.get_edges()
				next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
				start += next_vertices
		return False

