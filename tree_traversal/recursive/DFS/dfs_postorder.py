# post-order: LRP (left, right, parent)
def postorder_dfs(tree, start_vertex, visited=None):
	if not visited:
		visited = []

	visited  = visited + [start_vertex]

	if start_vertex in tree:
		for neighbour in tree[start_vertex]:
			if neighbour not in visited:
				new_path = postorder_dfs(tree, neighbour, visited)
				if new_path:
					return new_path

	print(start_vertex)


tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Call DFS starting from node 'A'
postorder_dfs(tree, 'A')