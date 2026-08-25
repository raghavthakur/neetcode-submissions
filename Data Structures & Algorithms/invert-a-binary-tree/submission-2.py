# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
invert the binary tree; swap the child nodes from left to right
dfs
'''
class Solution:
    # runtime: O(n) where n is number of nodes in the tree since dfs visits each node once
    # space: O(h) where h is height of tree and O(n) for skewed tree and O(logn) for balanced tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # swap the nodes
        root.left, root.right = root.right, root.left

        left_tree = self.invertTree(root.left)
        right_tree = self.invertTree(root.right)

        return root
        