# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        left, right = dummy, head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next            
        # fast = slow = head

        # for i in range(n):
        #     fast = fast.next

        # if not fast:
        #     return head.next

        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next
        # slow.next = slow.next.next
        # return head