# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        t = head
        r = 0
        while t is not None:
            r += 1
            t = t.next

        t = head
        r = r >> 1
        while r > 0:
            t = t.next
            r -= 1
        return t
