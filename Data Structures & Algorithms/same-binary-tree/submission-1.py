# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
given two trees p and q return true if both trees are the same otherwise return false

use bfs to traverse both trees at the same time
check if node_p and node_q is none then continue bfs
check if either node_p or node_q is none or node_p and node_q values differ return False
continue with bfs
'''
from collections import deque
class Solution:
    # runtime: O(n)
    # space: O(n)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p and queue_q:
            for _ in range(len(queue_p)):

                node_p = queue_p.popleft()
                node_q = queue_q.popleft()

                # continue if both nodes are None
                if node_p is None and node_q is None:
                    continue
                
                # return False if either node is None or values differ
                if node_p is None or node_q is None or node_p.val != node_q.val:
                    return False

                queue_p.append(node_p.left)
                queue_p.append(node_p.right)

                queue_q.append(node_q.left)
                queue_q.append(node_q.right)

        return True
        