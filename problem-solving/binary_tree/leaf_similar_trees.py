# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves_of_tree_1 = []
        leaves_of_tree_2 = []
        
        leaves_1 = self.leaf_nodes_1(root1, leaves_of_tree_1)
        leaves_2 = self.leaf_nodes_2(root2, leaves_of_tree_2)

        return leaves_1 == leaves_2

    def leaf_nodes_1(self, root1, leaves_of_tree_1):
        if not root1:
            return None

        if not root1.left and not root1.right:
            leaves_of_tree_1.append(root1.val)

        self.leaf_nodes_1(root1.left, leaves_of_tree_1)
        self.leaf_nodes_1(root1.right, leaves_of_tree_1)

        return leaves_of_tree_1

    def leaf_nodes_2(self, root2, leaves_of_tree_2):
        if not root2:
            return None

        if not root2.left and not root2.right:
            leaves_of_tree_2.append(root2.val)

        self.leaf_nodes_2(root2.left, leaves_of_tree_2)
        self.leaf_nodes_2(root2.right, leaves_of_tree_2)

        return leaves_of_tree_2
