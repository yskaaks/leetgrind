# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node, curr_num):
            if not node:
                return 0
            curr_num = curr_num * 10 + node.val
            if not node.left and not node.right:
                return curr_num            
            if node.left:
                left_sum = dfs(node.left, curr_num) 
            else:
                left_sum = 0
            if node.right:
                right_sum = dfs(node.right, curr_num)
            else:
                right_sum = 0
            return left_sum + right_sum
        return dfs(root, 0)
            
        