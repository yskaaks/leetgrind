# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even = head
        count = 0
        while even:
            odd = even.next
            if even.val > odd.val:
                count += 1
            elif even.val < odd.val:
                count -= 1
            even = odd.next
        
        if count == 0:
            return "Tie"
        elif count > 0:
            return "Even"
        return "Odd"