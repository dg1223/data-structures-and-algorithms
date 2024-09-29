from treenode import TreeNode, sample_root_node, print_path, print_tree

print_tree(sample_root_node)

def dfs(root, target, path=[]):
    '''
    path = path + [start] creates a new list called
    path on each recursive call and stores the path
    from the child node (current start node) to 
    possible target node.
    If we do path.append(start) or path += [start],
    every new path will be added to the previously
    found path. As a result, we won't be able to 
    track distinct paths for each child.
    '''
    path = path + [root]

    if root.value == target:
        return path

    for child in root.children:
        path_found = dfs(child, target, path)
        if path_found:
            return path_found

    return None

path = dfs(sample_root_node, "F")
print(path)