# pre-order: PLR (parent, left, right)
def preorder_dfs(tree, start_vertex, visited=None):
    if not visited:
        visited = []
    print(start_vertex)

    visited = visited + [start_vertex]    
    
	# Avoid leaf nodes because they have no neighbour
    if start_vertex in tree:
        for neighbour in tree[start_vertex]:
            if neighbour not in visited:
                path = preorder_dfs(tree, neighbour, visited)
                if path:
                    return path


tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Call DFS starting from node 'A'
preorder_dfs(tree, 'A')