# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack = root, []
        res = []
        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return res


        # res = []
        # if not root:
        #     return []
        # res.append(root.val)
        # left = self.preorderTraversal(root.left)
        # right = self.preorderTraversal(root.right)
        # res.extend(left)
        # res.extend(right)
        # return res