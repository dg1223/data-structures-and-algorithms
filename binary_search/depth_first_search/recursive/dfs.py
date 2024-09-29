#from treenode import TreeNode, sample_root_node, print_path, print_tree
#
#print_tree(sample_root_node)

class DFS:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def dfs(self, root, target, path=[]):        
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
        
        print("Traversing path:", [node.value for node in path])
        
        for child in root.children:
            path_found = self.dfs(child, target, path)
            
            if path_found:
                return path_found

        return None        
        

sample_root_node = DFS("A")
two = DFS("B")
three = DFS("C")

sample_root_node.children = [three, two]

four = DFS("D")
five = DFS("E")
six = DFS("F")
seven = DFS("G")

two.children = [five, four]
three.children = [seven, six]

path = sample_root_node.dfs(sample_root_node, "F")

if not path:
    print("\nNo path found")
else:
    print("\nPath found!\n")
    for node in path:
        print(node.value)