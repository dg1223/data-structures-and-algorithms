# pre-order: PLR (parent, left, right)
def preorder_dfs(graph, start_vertex, visited=None):
    if not visited:
        visited = []
    print(start_vertex)

    visited = visited + [start_vertex]    
    
	# Avoid leaf nodes because they have no neighbour
    if start_vertex in graph:
        for neighbour in graph[start_vertex]:
            if neighbour not in visited:
                path = preorder_dfs(graph, neighbour, visited)
                if path:
                    return path

## Create a graph represented as an adjacency list
#graph = {
#    'A': ['B', 'C'],
#    'B': ['A', 'D', 'E'],
#    'C': ['A', 'F'],
#    'D': ['B'],
#    'E': ['B', 'F'],
#    'F': ['C', 'E']
#}
#preorder_dfs(graph, 'A')

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Call DFS starting from node 'A'
preorder_dfs(tree, 'A')