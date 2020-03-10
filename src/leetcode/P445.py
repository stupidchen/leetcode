# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_arr(l):
    r = []
    while l is not None:
        r.insert(0, l.val)
        l = l.next
    return r


def arr_to_list(a):
    r = ListNode(-1)
    t = r
    for i in reversed(a):
        t.next = ListNode(i)
        t = t.next
    if r.next is None:
        r.next = ListNode(0)
    return r.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a, b = list_to_arr(l1), list_to_arr(l2)
        n = max(len(a), len(b)) + 1
        c = [0] * n
        t = 0
        for i in range(len(c)):
            c[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) + t
            t = c[i] // 10
            c[i] %= 10
        if c[-1] == 0:
            c = c[:-1]
        return arr_to_list(c)
