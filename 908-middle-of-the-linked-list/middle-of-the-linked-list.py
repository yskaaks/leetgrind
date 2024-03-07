# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


        # curr = head
        # count = 0
        # while curr:
        #     count += 1
        #     curr = curr.next
        # mid = count // 2
        
        # count = 0
        # curr = head
        # while count < mid:
        #     curr = curr.next
        #     count += 1
        # return curr


        # # slow, fast = head, head

        # # while fast and fast.next:
        # #     slow = slow.next
        # #     fast = fast.next.next 
        # # return slow