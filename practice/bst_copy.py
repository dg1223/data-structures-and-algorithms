class BST:
    def __init__(self, value, depth=0):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BST(value, self.depth + 1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BST(value, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        if value == self.value:
            return self
        # must check if left and right nodes exist
        elif self.left and value < self.value:
            self.left.get_node_by_value(value)
        elif self.right and value >= self.value:
            self.right.get_node_by_value(value)
        else:
            return "Value not found in tree"

    def dfs_traversal(self):
        if self.left:
            self.left.dfs_traversal()
        print(f"Depth: {self.depth}, Value: {self.value}")
        if self.right:
            self.right.dfs_traversal()

root = BST(100)

# Test 1
tree = BST(48)
tree.insert(24)
tree.insert(55)
tree.insert(26)
tree.insert(38)
tree.insert(56)
tree.insert(74)

# Print depth-first traversal:
tree.dfs_traversal()