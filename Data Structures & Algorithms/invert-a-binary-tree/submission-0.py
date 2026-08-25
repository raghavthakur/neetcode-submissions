# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
invert the binary tree given root

assume if root is none then return empty list

bfs
for each level reverse the nodes and add to result list
'''
from collections import deque
class Solution:
    # runtime: O(n) where n is number of nodes in the tree since bfs visits each node once
    # space: O(w) where w is length of level list which is at most O(n/2) for balanced tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        queue = deque([root])

        while queue:
            level_list = deque()

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                # invert nodes
                left_child = node.left
                node.left = node.right
                node.right = left_child
        
        return root











                
        