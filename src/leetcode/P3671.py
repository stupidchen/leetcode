# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int):
        p = ListNode(0, head)
        a = []
        t = p
        while t is not None:
            a.append(t)
            t = t.next

        q = a[-k]
        a[-k] = a[k]
        a[k] = q

        for i in range(len(a) - 1):
            a[i].next = a[i + 1]
        a[-1].next = None

        return p.next
