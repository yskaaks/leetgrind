# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return []
        def dfs(node, cur_sum, lst):
            if not node:
                return
            cur_sum += node.val
            lst.append(node.val)
            if not node.left and not node.right and cur_sum == targetSum:
                res.append(list(lst))
            else:
                dfs(node.left, cur_sum, lst)
                dfs(node.right, cur_sum, lst)
            lst.pop()
        dfs(root, 0, [])
        return res