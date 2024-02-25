# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, res=0) -> bool:
        if not root:
            return False
        def dfs(node, cur_sum):
            if not node:
                return False
            cur_sum += node.val
            if not node.left and not node.right:
                return cur_sum == targetSum
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)
        return dfs(root, 0)