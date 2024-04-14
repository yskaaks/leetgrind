# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
            if not node:
                return 0
            left = node.left
            right = node.right
            if not left and not right:
                return node.val if is_left else 0
            res = 0
            if left:
                res += dfs(node.left, True)
            if right:
                res += dfs(node.right, False)
            return res
        return dfs(root, False)
