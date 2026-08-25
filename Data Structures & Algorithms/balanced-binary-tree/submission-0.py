# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
return true if binary tree is balanced otherwise return false
height is balanced if height of left and righ subtree is not > 1

assume if root is none return True (balanced tree)

dfs to find heights
'''
class Solution:
    # runtime: O(n)
    # space: O(h)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.depth(root) != -1
    
    def depth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_depth = self.depth(node.left)
        if left_depth == -1:
            return -1

        right_depth = self.depth(node.right)
        if right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1
        
        return max(left_depth, right_depth) + 1




        