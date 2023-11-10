# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)

            self.diameter = max(left_height + right_height, self.diameter)

            return 1 + max(left_height, right_height)

        height(root)
        return self.diameter
