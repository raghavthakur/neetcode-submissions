# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
dfs to find depth
then calc validation using left_depth - right_depth > 1 return -1
'''
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.depth(root) != -1 # to return bool

    def depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_depth = self.depth(node.left)
        # check left_depth contraint
        if left_depth == -1:
            return -1 # raise error

        right_depth = self.depth(node.right)
        if right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        return max(left_depth, right_depth) + 1
        