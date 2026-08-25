# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
find the max depth
assume tree with single node has depth of 1
longest path from root to leaf


[1,2,3,null,null,4]

                        1
                    2       3
                                4

return 3

use bfs to find max depth
use dfs to find max depth
'''
class Solution:
    # runtime: O(n) where n is number of nodes in the tree since dfs visits each node once
    # space: O(h) where h is height of tree and O(n) for skewed tree and O(logn) for balanced tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return 0
        
        # recursive calls to child nodes
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # return to parent
        return max(left_depth, right_depth) + 1

'''
TESTS
[1,2,3,null,null,4]

                        1
                    2       3
                                4

return 3



'''