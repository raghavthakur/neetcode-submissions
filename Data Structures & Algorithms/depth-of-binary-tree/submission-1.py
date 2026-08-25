# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
find the max depth of the tree

bfs to find the depth
'''
from collections import deque
class Solution:
    # runtime: O(n) where n is number of nodes in the tree since bfs visits each node once
    # space: O(w) where w is the size of the queue and at most n/2 nodes
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_depth = 0

        queue = deque([root])

        while queue:
            max_depth += 1

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max_depth
        