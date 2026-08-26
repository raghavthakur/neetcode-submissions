# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Recursive DFS Approach
given root and subRoot of two binary trees, return true if there is a subtree in root with same nodes and structure as subRoot
otherwise return false

Assumptions
if subRoot is none then it is a subtree of root and return true
if root is none then false

Edge Cases
duplicate values in the root tree
                            1                           1
                        1
return true

                                1                           2
                            2       3                    4      5
                        4   5

return true

                                1                            2
                            2       3                     4     5
                        4   5
                    6

return false since node 6 does not match null child of node 4


Approach
first need to find when root node and subRoot node values match to begin same tree match
dfs on root to find when values match
if values match then dfs on both subtree of root and subRoot to check all node values match
return false if root dfs had no matches or return false if nested dfs had incorrect match otherwise return true
'''
class Solution:

    # runtime: O(n * m) where n is number of nodes in root and m is nodes in subRoot
    # space: O(h of n + h of m) where h is O(n + m) for skewed tree or O(logn + logm) for balanced tree   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base cases
        if root is None:
            return False

        if subRoot is None:
            return True

        # contraint
        if root.val == subRoot.val:
            # nested dfs to check if two trees are the same
            if self.same_tree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same_tree(self, node_1: Optional[TreeNode], node_2: Optional[TreeNode]) -> bool:
        # base cases
        if node_1 is None and node_2 is None:
            return True # both are leaf nodes

        if node_1 is None or node_2 is None or node_1.val != node_2.val:
            return False
        
        return self.same_tree(node_1.left, node_2.left) and self.same_tree(node_1.right, node_2.right)

        
# Optimal Solution
# serialize the two trees into a string format contianing node values using bfs pre-order which is O(n) time and # for null values
# then linearly search the root list for the subRoot list which has total runtime O(n + m) using KMP algo




        