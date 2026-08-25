# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
find the max diameter of the binary tree
diameter is length from left node to other leaf node
does not need to pass through root

diameter is max depth of left subtree + max depth of right subtree

assume leaf node has diameter 0
assume None root node has diameter of 0
'''
class Solution:
    def __init__(self):
        self.max_diameter = 0

    # runtime: O(n) where n is number of nodes where dfs visits each node once
    # space: O(h) where h is height of tree O(n) for skewed tree and O(logn) for balanced tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        self.depth(root)

        return self.max_diameter
        

    def depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)

        # constraint
        self.max_diameter = max(self.max_diameter, left_depth + right_depth)

        return max(left_depth, right_depth) + 1
        