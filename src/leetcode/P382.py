# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import randint


class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        """
        ret = -1
        c = 0
        t = self.head
        while t:
            r = randint(0, c)
            if r == 0:
                ret = t.val
            t = t.next
            c += 1
        return ret

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()