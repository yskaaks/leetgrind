# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return root.val != 0
        left_subtree = self.evaluateTree(root.left)
        right_substre = self.evaluateTree(root.right)

        if root.val == 2:
            non_leaf = left_subtree or right_substre
        else:
            non_leaf = left_subtree and right_substre
        return non_leaf