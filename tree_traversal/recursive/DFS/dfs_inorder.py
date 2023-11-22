def recursive_inorder_dfs(graph, current_vertex):
    if current_vertex in graph:
        left_neighbour, right_neighbour = graph[current_vertex]
        if left_neighbour:
            recursive_inorder_dfs(graph, left_neighbour)
        print(current_vertex)
        if right_neighbour:
            recursive_inorder_dfs(graph, right_neighbour)

def inorder_dfs(graph, start):
    recursive_inorder_dfs(graph, start)

tree = {
    'B': ['D', 'E'],
    'A': ['B', 'C'],
    'C': ['F', 'G'],
    'D': [None, None],
    'E': [None, None],
    'F': [None, None],
    'G': [None, None]
}

# Call in-order DFS starting from node 'A'
inorder_dfs(tree, 'A')