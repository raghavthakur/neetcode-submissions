# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
given two trees, return true if two trees are the same otherwise return false

trees are the same if each node in the two trees are the same

use bfs to create a list of nodes from the two trees
then compare the two lists and return true if both are same
'''
from collections import deque
class Solution:

    # runtime: O(p + q) where p and q are the nodes from the trees p and q since bfs visits each node once
    # space: O(p + q) since returning result list with nodes from each tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use bfs to get list of nodes from tree p
        # use bfs to get list of nodes from tree q
        # compare the two lists and return true if same otherwise return false
        p_nodes = self.bfs(p)
        q_nodes = self.bfs(q)

        return p_nodes == q_nodes

    def bfs(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if root is None:
            return result

        queue = deque([root])
        
        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    result.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append(None)
                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append(None)

                else:
                    result.append(None)

        return result

'''
TESTS

                    1                   1
                
                2       3           2       3


t1 = [1,2,3]
t2 = [1,2,3]

return True
'''
        
        