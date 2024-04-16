# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        q = collections.deque([root])
        curr_level = 1
        while q:
            if curr_level == depth - 1:
                while q:
                    node = q.popleft()
                    new_left = TreeNode(val, left=node.left, right=None)
                    new_right = TreeNode(val, left=None, right=node.right)
                    node.left = new_left
                    node.right = new_right
                return root
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            curr_level += 1
        return root
