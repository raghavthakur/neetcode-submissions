# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
given two tree nodes root and subroot return true if subroot is a subtree of root
otherwise return false

Assumptions:
if subroot is null then is subroot a subtree of root? yes

TODO: Edge cases with examples!

Approach:
use dfs to traverse root
check if root val match subroot val if doesnt match continue dfs on root
if match then use dfs on both root and subroot
then if at any node values don't match return false
if finish dfs on subroot with no mismatch then return true

'''
class Solution:
    # runtime: O(n * m) since dfs on root and then nested dfs on subroot
    # space: O(n) since using stack for dfs   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == subRoot.val:
                # dfs on subRoot with root
                if self.same_tree(node, subRoot):
                    return True # only return True if found match otherwise continue with dfs
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False # dfs returns and no subtree found
        
    def same_tree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None or root1.val != root2.val:
            return False
        
        return self.same_tree(root1.left, root2.left) and self.same_tree(root1.right, root2.right)
        





