# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,next=head)
        curr = dummy
        prefix_sum = 0
        sum_to_node = {0: dummy}

        while curr:
            prefix_sum += curr.val
            sum_to_node[prefix_sum] = curr
            curr = curr.next
        curr = dummy
        prefix_sum = 0 
        while curr:
            prefix_sum += curr.val
            curr.next = sum_to_node[prefix_sum].next
            curr = curr.next
        return dummy.next