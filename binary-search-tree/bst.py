'''
BST methods:
initialize, insert, search value, dfs traversal
-> if value_to_add == parent_node, add it to 
   the right child

*No need to learn to remove a node from a BST.
We generally use it to search for a value.
'''
class BST:
    def __init__(self, value, depth=0):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value, self.depth+1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                # iterate because current node has value
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value, self.depth+1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        if value == self.value:
            return self
        elif self.left and value < self.value:
            self.left.get_node_by_value(value)
        elif self.right and value >= self.value:
            self.right.get_node_by_value(value)
        else:
            return None

    def traverse_dfs(self):
        if self.left:
            self.left.traverse_dfs()
        print(f"Depth = {self.depth}, Value = {self.value}")
        if self.right:
            self.right.traverse_dfs()


# Test 1
tree = BST(48)
tree.insert(24)
tree.insert(55)
tree.insert(26)
tree.insert(38)
tree.insert(56)
tree.insert(74)

# Print depth-first traversal:
tree.traverse_dfs()