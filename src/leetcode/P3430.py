# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        tmp = []
        i = head
        while i is not None:
            tmp.append(i)
            i = i.next
        n = len(tmp)
        if n <= 2:
            return
        for k in range(n >> 1):
            if k < n - 1 - k:
                tmp[k].next = tmp[n - 1 - k]
                if n - 1 - k > k + 1:
                    tmp[n - 1 - k].next = tmp[k + 1]
                else:
                    tmp[n - 1 - k].next = None
            else:
                break
        tmp[n >> 1].next = None
