# post-order: LRP (left, right, parent)
def postorder_dfs(graph, start_vertex, visited=None):
	if not visited:
		visited = []

	visited  = visited + [start_vertex]

	if start_vertex in graph:
		for neighbour in graph[start_vertex]:
			if neighbour not in visited:
				new_path = postorder_dfs(graph, neighbour, visited)
				if new_path:
					return new_path

	print(start_vertex)

## Create a graph represented as an adjacency list
#graph = {
#    'A': ['B', 'C'],
#    'B': ['A', 'D', 'E'],
#    'C': ['A', 'F'],
#    'D': ['B'],
#    'E': ['B', 'F'],
#    'F': ['C', 'E']
#}
#postorder_dfs(graph, 'A')

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Call DFS starting from node 'A'
postorder_dfs(tree, 'A')