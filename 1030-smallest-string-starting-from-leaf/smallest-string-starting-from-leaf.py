# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        smallest = None

        def dfs(node, path):
            nonlocal smallest
            if node:
                char = chr(node.val + ord("a"))
                new_path = char + path

                if not node.left and not node.right:
                    if smallest is None or new_path < smallest:
                        smallest = new_path
                
                if node.left:
                    dfs(node.left, new_path)
                
                if node.right:
                    dfs(node.right, new_path)
        dfs(root, "")
        return smallest