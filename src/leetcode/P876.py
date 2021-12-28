# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        len = 0
        tmp = head
        while tmp is not None:
            len += 1
            tmp = tmp.next

        len = len >> 1
        for i in range(len):
            head = head.next
        return head
