# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return [] 
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        res.extend(left)
        res.extend(right)
        res.append(root.val)
        return res


        return res