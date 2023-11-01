from treenode import TreeNode, sample_root_node, print_path, print_tree

print_tree(sample_root_node)

def dfs(root, target, path=()):
    path = path + (root,)

    if root.value == target:
        return path

    for child in root.children:
        path_found = dfs(child, target, path)
        if path_found:
            return path_found

    return None

path = dfs(sample_root_node, "F")
print(path)