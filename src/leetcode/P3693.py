# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tmp = head
        last = None
        while tmp is not None:
            this = ListNode(tmp.val)
            this.next = last
            last = this
            tmp = tmp.next
        tmp = head
        while tmp is not None:
            if tmp.val != last.val:
                return False
            tmp = tmp.next
            last = last.next
        return True
