# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        d = {}
        while curr:
            if curr.val in d:
                d[curr.val] += 1
            else:
                d[curr.val] = 1
            curr = curr.next
        dummy = ListNode()
        curr = dummy
        for i in d.values():
            new_node = ListNode(i)
            curr.next = new_node
            curr = curr.next
        return dummy.next