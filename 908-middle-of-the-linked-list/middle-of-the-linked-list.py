# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        mid = count // 2
        
        count = 0
        curr = head
        while count < mid:
            curr = curr.next
            count += 1
        return curr







        # curr = head
        # count = 0
        # while curr is not None:
        #     count += 1
        #     curr = curr.next
        # mid_index = count // 2

        # curr = head  # Reset curr to head
        # for _ in range(mid_index):
        #     curr = curr.next

        # return curr


        # # slow, fast = head, head

        # # while fast and fast.next:
        # #     slow = slow.next
        # #     fast = fast.next.next 
        # # return slow