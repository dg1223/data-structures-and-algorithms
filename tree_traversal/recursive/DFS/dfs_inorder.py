def recursive_inorder_dfs(structure, current_vertex):
    if current_vertex in structure:
        left_child, right_child = structure[current_vertex]
        if left_child:
            recursive_inorder_dfs(structure, left_child)
        print(current_vertex)
        if right_child:
            recursive_inorder_dfs(structure, right_child)

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