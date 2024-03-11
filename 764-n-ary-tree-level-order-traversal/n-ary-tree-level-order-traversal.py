"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        q = collections.deque([root])
        if not root:
            return []
        while q:
            levels = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    levels.append(node.val)
                    for j in node.children:
                        q.append(j)
            res.append(levels)
        return res                    