# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        level_count = 0
        while q:
            levels = []
            for i in range(len(q)):
                node = q.popleft()
                levels.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_count % 2 == 0: # even level
                for i in range(len(levels)):
                    if levels[i] % 2 == 0 or (i > 0 and levels[i] <= levels[i-1]):
                        return False
            else: # odd level
                for i in range(len(levels)):
                    if levels[i] % 2 != 0 or (i > 0 and levels[i] >= levels[i-1]):
                        return False
            level_count += 1
        return True



        return res