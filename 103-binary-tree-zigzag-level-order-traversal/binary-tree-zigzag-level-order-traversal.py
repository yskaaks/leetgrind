# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = collections.deque([root])
        zigzag = False
        while q:
            level_size = len(q)
            level = []
            for i in range(level_size):
                node = q.popleft()
                if not zigzag:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
            zigzag = not zigzag
        return res
