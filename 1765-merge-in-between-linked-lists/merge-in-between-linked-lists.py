# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr1 = list1
        count = 0
        merge_lst = []
        while curr1:
            if a == count:
                break
            merge_lst.append(curr1.val)
            count += 1
            curr1 = curr1.next
        
        curr2 = list2
        while curr2:
            merge_lst.append(curr2.val)
            curr2 = curr2.next
        
        while curr1:
            if b != count:
                count += 1
                curr1 = curr1.next
            else:
                break
        curr1 = curr1.next
        while curr1:
            merge_lst.append(curr1.val)
            curr1 = curr1.next    

        res = None
        for i in range(len(merge_lst)):
            new_node = ListNode(merge_lst.pop(), res)
            res = new_node
        return res
