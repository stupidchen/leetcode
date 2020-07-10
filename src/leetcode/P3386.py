"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


def tail(node):
    if node is None:
        return None
    t = node
    while t.next is not None:
        t = t.next
    return t


class Solution:
    def flatten(self, head):
        if head is None:
            return None

        c = self.flatten(head.child)
        n = self.flatten(head.next)
        if c is not None:
            head.child = None
            head.next = c
            c.prev = head
            t = tail(c)
            t.next = n
            if n is not None:
                n.prev = t
        return head
