def recursive_inorder_dfs(graph, current_vertex):
    if current_vertex in graph:
        left_child, right_child = graph[current_vertex]
        if left_child:
            recursive_inorder_dfs(graph, left_child)
        print(current_vertex)
        if right_child:
            recursive_inorder_dfs(graph, right_child)

def inorder_dfs(structure, start):
    recursive_inorder_dfs(structure, start)

tree = {
    'A': ('B', 'C'),
    'B': ('D', 'E'),
    'C': ('F', 'G'),
    'D': (None, None),
    'E': (None, None),
    'F': (None, None),
    'G': (None, None)
}

# Call in-order DFS starting from node 'A'
inorder_dfs(tree, 'A')