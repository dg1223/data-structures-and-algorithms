def recursive_inorder_dfs(structure, current_node):
    if current_node in structure:
        left_child, right_child = structure[current_node]
        if left_child:
            recursive_inorder_dfs(structure, left_child)
        print(current_node)
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