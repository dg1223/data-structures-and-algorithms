from collections import deque

class Graph:
	def __init__(self, directed=False):
		self.graph_dict = {}
		self.directed = directed

	def add_vertex(self, vertex):
		self.graph_dict[vertex.value] = vertex

	def add_edge(self, from_vertex, to_vertex):
		self.graph_dict[from_vertex.value].add_edge(to_vertex.value)
		if not self.directed:
			self.graph_dict[to_vertex.value].add_edge(from_vertex.value)

	def find_path(self, start_vertex, end_vertex):
		start = deque()
		start.append(start_vertex)
		seen = set()
		while start:
			current_vertex = start.pop()
			seen.add(current_vertex)
			print("Visiting " + current_vertex)
			if current_vertex == end_vertex:
				return True
			else:
				vertex = self.graph_dict[current_vertex]
				next_vertices = vertex.get_edges()
				next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
				'''
				With appendleft(), you are trying to append a list of vertices (next_vertices)
				to the start deque using appendleft. However, in BFS, you should add 
				individual vertices to the deque, not a list of vertices.
				To fix this, you should use the extendleft method instead of appendleft.
				'''
				#start.appendleft(next_vertices)
				start.extendleft(next_vertices)
		return False

