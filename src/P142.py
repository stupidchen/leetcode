# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        if head is None:
            return
        x = head
        y = head
        c = False
        while x.next is not None and y.next is not None and y.next.next is not None:
            x = x.next
            y = y.next.next
            if x == y:
                c = True
                break

        if not c:
            return
        x = head
        while x != y:
            x = x.next
            y = y.next
        return x
