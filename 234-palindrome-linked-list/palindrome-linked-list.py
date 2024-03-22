# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # curr = head
        # prev = None
        # while curr is not None:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev == save
        curr = head
        prev = None
        lst = []
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next

        return lst == lst[::-1]
        # n = 0
        # while n < len(lst) and len(lst) == len(lst2):
        #     if lst[n] != lst2[n]:
        #         break
        #     n += 1
        # if n == len(lst):
        #     return True
        # return False


