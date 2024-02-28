# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        res = root
        while q:
            res = q.popleft()
            if res.right:
                q.append(res.right)
            if res.left:
                q.append(res.left)
        return res.val