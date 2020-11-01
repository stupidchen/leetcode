# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head):
        t = head
        r = 0
        while t is not None:
            r = (r << 1) + t.val
            t = t.next
        return r
